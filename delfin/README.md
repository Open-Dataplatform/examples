# Delfin data

## Datasets
This example is to demonstrate how to access the Delfin dataset.

- [Delfin DAILY](https://dataplatform.energinet.dk/detail/bc870e52-f1fe-4df8-1156-08d925bcbaf2)
- [Delfin HOURLY](https://dataplatform.energinet.dk/detail/cb2c7313-58be-460f-9be8-08d90a4e650d)
- [Delfin MINUTELY](https://dataplatform.energinet.dk/detail/55b1a30b-06e6-45d1-9be9-08d90a4e650d)

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

### Get Delfin content
This lists content of Delfin data on a DAILY horizon
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

json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01", "2020-02")
```
The code will return all the available data.

The available horizons are **Horizon.DAILY**, **Horizon.HOURLY**, and **Horizon.MINUTELY**.

See examples in the source code provided here.
