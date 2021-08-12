# GTMS data
- [Datasets](#datasets)
- [Overview](#overview)
- [Retrieve data](#retrieve-data)
  - [Installation and Config file](#installation-and-config-file)
  - [Retrieve Data from a Date Range](#retrieve-data-from-a-date-range)
  - [Retrieve full data](#retrieve-full-data)
 
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

| Name                    | Horizon | Index          | Start Date | TEST API | Data Quality | Notes       |
| ----------------------- | ------- | -------------- | ---------- | -------- | ------------ | ----------- |
| GT Invoice Lines BI     | Monthly | GASMONTH       | 2004-01    | enabled  | Full         | |
| GT Biocertificate BI    | Daily   | GASDAY         | 2020-01-01 | enabled  | Partial      | Missing from 2021-07-01 -> |
| GT DATA H BI            | Monthly | GASDAY         | 2004-01    | enabled  | Partial      | Missing data throughout (140 months) |
| GT Nom BI               | Daily   | GASDAY         | 2009-01-01 | enabled  | Partial      | Missing from 2021-07-12 -> |
| GT Player BI            | None    | REV_DATE       |            | enabled  |              | |
| GT Point BI             | None    | REV_DATE       |            | enabled  |              | |
| GT Contract Capacity BI | Monthly | CREATED_DATE   | 2006-04    | enabled  | Partial      | Missing data, Only new format from 2021-06 -> |
| GT Time BI              | Monthly | ACTUAL_TIME(?) | 2009-01    |          | Partial      | Data from 2009-2044 (New format 2021-05 -> present day) |
| GT Trade BI             | Monthly | GASDAY         | 2009-01    | enabled  | Partial      | Data from 2009-2044 (New format 2021-05 -> 2021-07) |
| GT Balance System BI    | Monthly | GASDAY         | 2014-10    | enabled  | Full         | |
| GT Alloc BI             | Daily   | GASDAY         | 2004-01-01 | enabled  | Full         | |
 

## Retrieve data

This section describes how to retrieve data from the GTMS sources from the Egress API.

Notice: When the Osiris-SDK is updated to version 1.0 it will become easier.

### Config file
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

[Dataset]
guid = <dataset-guid>
```

### Retrieve data from a date range
To access the data from a dataset with no Horizon use the following code.
``` python
import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

guid = config['Dataset']['guid']

response = requests.get(
    url=f'https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/{guid}/test_json',
    params={'from_date': '2014-01', 'to_date': '2014-04'},
    headers={'Authorization': client_auth.get_access_token()}
)

print(response.status_code)
print(response.json())
```
The code will return all the available data between *from_date* (inclusive) to *to_date* (exclusive).

Examples:


| from_date        | to_date          | interval                                     |
| ---------------- | ---------------- | -------------------------------------------- |
| 2014-01-01T01:01 | 2014-01-01T01:06 | 2014-01-01T01:01 to 2014-01-01T01:05:59.9999 |
| 2014-01-01T01    | 2014-01-01T04    | 2014-01-01T01:00 to 2014-01-01T03:59:59.9999 |
| 2014-01-01       | 2014-01-04       | 2014-01-01T00:00 to 2014-01-04T23:59:59.9999 |
| 2014-01          | 2014-04          | 2014-01-01T00:00 to 2014-03-31T23:59:59.9999 |
| 2014             | 2016             | 2014-01-01T00:00 to 2015-12-31T23:59:59.9999 |

### Retrieve full data
The datasets with Horizon NONE (in the table above) can retrieve all data stored.
The example below shows how this can be done.
``` python
import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

guid = config['Dataset']['guid']

response = requests.get(
    url=f'https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/{guid}/test_json',
    headers={'Authorization': client_auth.get_access_token()}
)

print(response.status_code)
print(response.json())
```