# Neptun data

## Dataset
This example is to demonstrate how to access the DMI dataset.

- [Neptun Daily](https://dataplatform.energinet.dk/detail/5466d7cc-77cb-4cd1-1155-08d925bcbaf2)
- [Neptun Hourly](https://dataplatform.energinet.dk/detail/0d80b6fc-fcfb-4848-1153-08d925bcbaf2)
- [Neptun Minutely](https://dataplatform.energinet.dk/detail/0d80b6fc-fcfb-4848-1153-08d925bcbaf2)

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

### Get data from Netpun
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

json_content = egress.download_neptun_file(Horizon.DAILY, "2020-01", "2020-02")
```
The code will return all the available data.

The available horizons are **Horizon.DAILY**, **Horizon.HOURLY**, and **Horizon.MINUTELY**.

