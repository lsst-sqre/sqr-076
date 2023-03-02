:tocdepth: 1

.. sectnum::

.. Metadata such as the title, authors, and description are set in metadata.yaml

.. TODO: Delete the note below before merging new content to the main branch.

.. note::

   **This technote is a work-in-progress.**

Abstract
========

Many SQuaRE applications in Roundtable, notably the Squarebot Slack bot, use Kafka for sharing messages. Those Kafka messages are encoded in Avro, and those Avro schemas are shared between applications at runtime with the Confluent Schema Registry. This existing system lacks a story for sharing schemas between applications during development. In SQR-075 we described a monorepo architecture for publishing an application's Pydantic schemas in a Python library that an app's clients could use. This technote describes how shared Pydantic schemas can also support the development of Kafka consumers.

Add content here
================

Add content here.
See the `reStructuredText Style Guide <https://developer.lsst.io/restructuredtext/style.html>`__ to learn how to create sections, links, images, tables, equations, and more.

.. Make in-text citations with: :cite:`bibkey`.
.. Uncomment to use citations
.. .. rubric:: References
.. 
.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa
