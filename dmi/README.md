# DMI data

## Dataset
This example is to demonstrate how to access the DMI dataset.

- [DMI Forecast Aggregated](https://dataplatform.energinet.dk/detail/2c844464-5872-4d60-dc2c-08d945e7e910)

## Retrieve data

This section describes how to retrieve data from the DMI sources from the Egress API.

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

[Egress]
url = <egress-url>
```

### List all station coordinates
To list all the stations coordinates (lon and lat) you can use the following code.

Notice, that it lists the stations available for a given month.
``` python
from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

egress = Egress(client_auth=client_auth,
                egress_url=config['Egress']['url'])

station_coord = egress.download_dmi_list('2021-01')
```
The code will return all the available data.

### Retrieve data for a station
To retrieve data for a given station (specified by lon and lat) use similar code,
which retrieves data for a given date interval.
``` python
from osiris.apis.egress import Egress
ffrom osiris.core.azure_client_authorization import ClientAuthorization
rom configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

egress = Egress(client_auth=client_auth,
                egress_url=config['Egress']['url'])

parquet_content = egress.download_dmi_file(15.19, 55.00, '2021-01', '2021-03')
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
