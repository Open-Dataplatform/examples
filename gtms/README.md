# GTMS data
- [Datasets](#datasets)
- [Overview](#overview)
- [Retrieve data](#retrieve-data)
  - [Installation and Config file](#installation-and-config-file)
  - [Horizon: None](#horizon:-one)
  - [Horizon: Daily](#horizon:-daily)
  - [Horizon: Monthly](#horizon:-monthly)

## Datasets
The GTMS data consists of the following datasets.
- [GT Invoice Lines BI](https://dataplatform.energinet.dk/detail/471d3e34-b843-4298-fc34-08d8b6fedea4)
- [GT Biocertificate BI](https://dataplatform.energinet.dk/detail/b133dd7a-f1e8-48db-fc33-08d8b6fedea4)    
- [GT DATA H BI](https://dataplatform.energinet.dk/detail/da650d2c-2780-44dc-6b3c-08d876589e90) 
- [GT Nom BI](https://dataplatform.energinet.dk/detail/fecfb55e-4637-4ff6-af49-08d86c4300e8)
- [GT Player BI](https://dataplatform.energinet.dk/detail/adc8d96f-8e3d-4e3d-af48-08d86c4300e8)
- [GT Point BI](https://dataplatform.energinet.dk/detail/b1c9449c-a452-4308-af47-08d86c4300e8)
- [GT Contract Capacity BI](https://dataplatform.energinet.dk/detail/acfee9a5-fc82-4e4d-af46-08d86c4300e8)
- [GT Time BI](https://dataplatform.energinet.dk/detail/14e4bf94-afab-44b3-af45-08d86c4300e8)
- [GT Trade BI](https://dataplatform.energinet.dk/detail/3ab1b6f7-d0ec-4c16-7de5-08d86b849d90)
- [GT Balance System BI](https://dataplatform.energinet.dk/detail/0f3897d5-0c57-4967-7de4-08d86b849d90)
- [GT Alloc BI](https://dataplatform.energinet.dk/detail/02480cbc-5361-43ab-e1d8-08d86464f17e)

## Overview

| Name                    | Horizon | Index          | Start Date | Data Quality | Notes       |
| ----------------------- | ------- | -------------- | ---------- | ------------ | ----------- |
| GT Invoice Lines BI     | Monthly | GASMONTH       | 2004-01    | Full         | |
| GT Biocertificate BI    | Daily   | GASDAY         | 2020-01-01 | Partial      | Missing from 2021-07-01 -> |
| GT DATA H BI            | Monthly | GASDAY         | 2004-01    | Partial      | Missing data throughout (140 months) |
| GT Nom BI               | Daily   | GASDAY         | 2009-01-01 | Partial      | Missing from 2021-07-12 -> |
| GT Player BI            | None    |                |            |              | |
| GT Point BI             | None    |                |            |              | |
| GT Contract Capacity BI | Monthly | TO_HOUR_UTC(?) | 2006-04    | Partial      | Missing data, Only new format from 2021-06 -> |
| GT Time BI              | Monthly | ACTUAL_TIME(?) | 2009-01    | Partial      | Data from 2009-2044 (New format 2021-05 -> present day) |
| GT Trade BI             | Monthly | CREATED_DATE(?)| 2009-01    | Partial      | Data from 2009-2044 (New format 2021-05 -> 2021-07) |
| GT Balance System BI    | Monthly | GASDAY         | 2014-10    | Full         | |
| GT Alloc BI             | Daily   | GASDAY         | 2004-01-01 | Full         | |


## Retrieve data

The way to access data depends on the structure of how data is stored.
There are 3 different structures given in the Horizon column.
Below we will go through the general setup and each of the 3 cases.
The full code is available here in the repo.

### Installation and Config file
First step is to install the Osiris-SDK to access data.
``` shell
$ pip install osiris-sdk
```

The configuration is advised to be done in a file.

The structure of **conf.ini**:
```
[Authorization]
tenant_id = <tenant_id>
client_id = <client_id>
client_secret = <client_secret>

[Egress API]
url = <url to egress-api>
guid = <dataset-guid>
```

### Horizon: None
To access the data from a dataset with no Horizon use the following code.
``` python
from osiris.apis.egress import Egress
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

egress = Egress(egress_url=config['Egress API']['url'],
                tenant_id=config['Authorization']['tenant_id'],
                client_id=config['Authorization']['client_id'],
                client_secret=config['Authorization']['client_secret'],
                dataset_guid=config['Egress API']['guid'])

json_data = egress.download_json_file()
```
The code will return all the available data.

### Horizon: Daily
To access the data from a dataset with daily Horizon use the following code.
``` python
from osiris.apis.egress import Egress
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

egress = Egress(egress_url=config['Egress API']['url'],
                tenant_id=config['Authorization']['tenant_id'],
                client_id=config['Authorization']['client_id'],
                client_secret=config['Authorization']['client_secret'],
                dataset_guid=config['Egress API']['guid'])

json_data = egress.download_json_file('2021-01-01', '2021-01-03')
```
The code will get all data from 2021-01-01 to 2021-01-03. Modify the dates to get a different time frame.

### Horizon: Monthly
To access the data from a dataset with monthly Horizon use the following code.
``` python
from osiris.apis.egress import Egress
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

egress = Egress(egress_url=config['Egress API']['url'],
                tenant_id=config['Authorization']['tenant_id'],
                client_id=config['Authorization']['client_id'],
                client_secret=config['Authorization']['client_secret'],
                dataset_guid=config['Egress API']['guid'])

json_data = egress.download_json_file('2021-06', '2021-08')
```
The code will get all data from 2021-06 to 2021-08. Modify the dates to get a different time frame.