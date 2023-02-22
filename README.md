# External data scarpers

Repository for collecting data from publicly available data sources.

## Development

Using well known framework for extracting data from websites [Scrapy](https://scrapy.org/).

## Local development

Using OpenSearch cluster with docker-compose.yaml

```
docker-compose up -d
```

On Linux system there is problem starting the opensearch node, so you have to run:
``
sudo sysctl -w vm.max_map_count=262144
``

Ref
https://stackoverflow.com/questions/51445846/elasticsearch-max-virtual-memory-areas-vm-max-map-count-65530-is-too-low-inc

You can now visit http://lcoalhost:5601.


## About the Project

Project is part of DataScience@UL-FRI Project Competition 2023, organized by Medius d.o.o. and FRI. 
