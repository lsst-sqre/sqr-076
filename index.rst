#################################################################################
Shared Pydantic schemas as the basis for Kafka/Avro messages in SQuaRE Roundtable
#################################################################################

.. abstract::

   Many SQuaRE applications in Roundtable, notably the Squarebot Slack bot, use Kafka for sharing messages. Those Kafka messages are encoded in Avro, and those Avro schemas are shared between applications at runtime with the Confluent Schema Registry. This existing system lacks a story for sharing schemas between applications during development. In SQR-075 we described a monorepo architecture for publishing an application's Pydantic schemas in a Python library that an app's clients could use. This technote describes how shared Pydantic schemas can also support the development of Kafka consumers.

Background
==========

TK
