# JAO data

## Dataset
This example is to demonstrate how to access the JAO datasets.

- [JAO Monthly](https://dataplatform.energinet.dk/detail/48c22d75-940a-41e9-adff-08d8fda4ba53)
- [JAO Yearly](https://dataplatform.energinet.dk/detail/2d20ccdc-d9f3-4a99-a7a9-08d91a00b8e7)

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
The code will return all the available data.

The available horizons are **Horizon.MONTHLY** and **Horizon.YEARLY**.