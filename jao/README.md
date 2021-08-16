# JAO data

## Dataset
This example is to demonstrate how to access the JAO datasets.

- [JAO Monthly](https://dataplatform.energinet.dk/detail/48c22d75-940a-41e9-adff-08d8fda4ba53)
- [JAO Yearly](https://dataplatform.energinet.dk/detail/2d20ccdc-d9f3-4a99-a7a9-08d91a00b8e7)

## Retrieve data

This section describes how to retrieve data from the JAO sources from the Egress API.

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

### List JAO data
``` python
from osiris.apis.egress import Egress
from configparser import ConfigParser
from osiris.core.enums import Horizon


config = ConfigParser()
config.read('conf.ini')

egress = Egress(egress_url=config['Egress']['url'],
                tenant_id=config['Authorization']['tenant_id'],
                client_id=config['Authorization']['client_id'],
                client_secret=config['Authorization']['client_secret'])

json_content = egress.download_jao_file(Horizon.MONTHLY, "2020-01", "2020-02")
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

The available horizons are **Horizon.MONTHLY** and **Horizon.YEARLY**.