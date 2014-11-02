Campaign Fianance Data Stuff
=====


#Overview

The Federal Election Committee (FEC) makes campaign finance data available, updated once a week. 

http://www.fec.gov/finance/disclosure/ftpdet.shtml

Unfortunately, the data is normalized across six files. This is fine if you plan on loading the data into a relational database like MySQL or Microsoft Access. However, if you're interested in loading this data into a modern data store such as Elasticsearch or MongoDB, you'll need to do some work to denormalize the data, since these NoSQL systems are optimized for low-latency, view-oriented queries, along with the inclusion of full-text search capabilities.

This repository currently just contains a simple Python script to denormalize the FEC pipe-delimited data files into JSON documents. 

In the future, I'll add a Logstash config for loading the data into Elasticsearch using Logstash, an Elasticsearch index template, etc.

#Data Model

TBD -- Describe how the normalized files are joined, assumptions made, etc.