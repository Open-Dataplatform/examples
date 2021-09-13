# GTMS data
- [Datasets](#datasets)
- [Overview](#overview)
- [Retrieve data](#retrieve-data)
  - [Installation and Config file](#installation-and-config-file)
  - [Retrieve Data from a Date Range](#retrieve-data-from-a-date-range)
  - [Retrieve full data](#retrieve-full-data)
 
## Datasets
The GTMS data consists of the following datasets.
- [GT Invoice Lines BI](https://dataplatform.energinet.dk/detail/2cb9c571-3a5a-4d5c-eed1-08d9628f61e5)
- [GT Biocertificate BI](https://dataplatform.energinet.dk/detail/ec135591-bbf6-4e69-eecd-08d9628f61e5)    
- [GT DATA H BI](https://dataplatform.energinet.dk/detail/726dd6be-c485-4cf9-eecf-08d9628f61e5) 
- [GT Nom BI](https://dataplatform.energinet.dk/detail/fecfb55e-4637-4ff6-af49-08d86c4300e8)
- [GT Player BI](https://dataplatform.energinet.dk/detail/adc8d96f-8e3d-4e3d-af48-08d86c4300e8)
- [GT Point BI](https://dataplatform.energinet.dk/detail/b1c9449c-a452-4308-af47-08d86c4300e8)
- [GT Contract Capacity BI](https://dataplatform.energinet.dk/detail/acfee9a5-fc82-4e4d-af46-08d86c4300e8)
- [GT Time BI](https://dataplatform.energinet.dk/detail/14e4bf94-afab-44b3-af45-08d86c4300e8)
- [GT Trade BI](https://dataplatform.energinet.dk/detail/3ab1b6f7-d0ec-4c16-7de5-08d86b849d90)
- [GT Balance System BI](https://dataplatform.energinet.dk/detail/55b1015a-e04e-442c-eed4-08d9628f61e5)
- [GT Alloc BI](https://dataplatform.energinet.dk/detail/6c460d49-a450-48c2-82ff-08d9661b40e3)

## Overview

| Name                    | Horizon | Index          | Start Date | Transformed |
| ----------------------- | ------- | -------------- | ---------- | ----------- | 
| GT Invoice Lines BI     | Monthly | GASMONTH       | 2004-01    |             |
| GT Biocertificate BI    | Daily   | GASDAY         | 2020-01-01 |             |
| GT DATA H BI            | Monthly | GASDAY         | 2004-01    |             |
| GT Nom BI               | Daily   | GASDAY         | 2009-01-01 |             |
| GT Player BI            | None    | REV_DATE       |            |             |
| GT Point BI             | None    | REV_DATE       |            |             |
| GT Contract Capacity BI | Monthly | CREATED_DATE   | 2006-04    |             |
| GT Time BI              | Monthly | ACTUAL_TIME(?) | 2009-01    |             |
| GT Trade BI             | Monthly | GASDAY         | 2009-01    |             |
| GT Balance System BI    | Monthly | GASDAY         | 2014-10    |             |
| GT Alloc BI             | Daily   | GASDAY         | 2004-01-01 |             |
 

## Example
See the Jupyter Notebook for code example
