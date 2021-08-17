# Delfin data

## Datasets
This example is to demonstrate how to access the Delfin dataset.

- [Delfin DAILY](https://dataplatform.energinet.dk/detail/bc870e52-f1fe-4df8-1156-08d925bcbaf2)
- [Delfin HOURLY](https://dataplatform.energinet.dk/detail/cb2c7313-58be-460f-9be8-08d90a4e650d)
- [Delfin MINUTELY](https://dataplatform.energinet.dk/detail/55b1a30b-06e6-45d1-9be9-08d90a4e650d)

## Retrieve data

This section describes how to retrieve data from the Delfin sources from the Egress API.

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

### Get Delfin content
This lists content of Delfin data on a DAILY horizon
``` python
from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from osiris.core.enums import Horizon
from configparser import ConfigParser


config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

egress = Egress(client_auth=client_auth,
                egress_url=config['Egress']['url'])

json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01", "2020-02")
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


The available horizons are **Horizon.DAILY**, **Horizon.HOURLY**, and **Horizon.MINUTELY**.

See examples in the source code provided here.

### Get Delfin content for specific table indices
An example where the **table_indices** is set.
``` python
from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from osiris.core.enums import Horizon
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

egress = Egress(client_auth=client_auth,
                egress_url=config['Egress']['url'])

json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01-15T03:00", "2020-01-16T03:01",
                                           table_indices=[1, 2])
```
The **table_indices** takes a list of indices you want to return. The list can have arbitrary length.
