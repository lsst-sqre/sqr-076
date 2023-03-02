#################################################################################
Shared Pydantic schemas as the basis for Kafka/Avro messages in SQuaRE Roundtable
#################################################################################

.. abstract::

   Many SQuaRE applications in Roundtable, notably the Squarebot Slack bot, use Kafka for sharing messages. Those Kafka messages are encoded in Avro, and those Avro schemas are shared between applications at runtime with the Confluent Schema Registry. This existing system lacks a story for sharing schemas between applications during development. In SQR-075 we described a monorepo architecture for publishing an application's Pydantic schemas in a Python library that an app's clients could use. This technote describes how shared Pydantic schemas can also support the development of Kafka consumers.

Background
==========

SQuaRE's Roundtable Kubernetes cluster for internal observatory services includes a Kafka cluster.
One of the applications for this Kafka cluster is passing messages between applications.
The advantage of this approach over direct API calls between applications is that message buffering is built into Kafka.
Therefore in a real-time event driven system, like the Squarebot Slack bot, individual applications don't need to maintain their own internal queue systems.
As well, Kafka topics can be *partitioned* so that multiple instances of a consumer application can tackle an event queue in parallel.

Another benefit of using Kafka for message passing between services is that schema management is built in.
Messages are encoded in Avro, and the corresponding schemas are stored centrally in the Confluent Schema Registry.
We created a Python library, Kafkit_, that encodes and decodes Avro messages in conjunction with the Schema Registry.
With this schema management system, the format of any message is well-known, even if the schema of a messages in a given topic evolves over time.
Further, the manner in which a schema can evolve is regulated through the Schema Registry.
Specifically, Roundtable applications use "forward compatibility" so that a message send by a newer producer can still be read by older consumers that still rely on the older schema.

This schema information could be used much more powerfully during application development, though.
Modern SQuaRE Python applications use type annotations and static type checking to prevent bugs and improve development speed through in-editor documentation.
Pydantic_ is a Python library for creating data models with type annotations that also validate and normalize data during runtime.
We make extensive use of Pydantic_ in our web APIs to declare the schemas of HTTP request and response bodies.
It makes sense, then, to also seek to use Pydantic_ to represent data within our Kafka-based applications.
This technote explores this issue, including the specific questions of:

- How can Pydantic_ models be transformed into Avro schemas?
- How can Pydantic_ models sync to the Confluent Schema Registry with Kafkit?
- How can Pydantic_ models be shared between Python-based Kafka producers and consumers?

.. _Kafkit: https://kafkit.lsst.io
.. _Pydantic: https://docs.pydantic.dev
