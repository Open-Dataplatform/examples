# DMI data

## Dataset
This example is to demonstrate how to access the DMI dataset.

- [DMI Forecast Aggregated](https://dataplatform.energinet.dk/detail/2c844464-5872-4d60-dc2c-08d945e7e910)

## Retrieve data

The way to access data depends on the structure of how data is stored.
There are 3 different structures given in the Horizon column.
Below we will go through the general setup and each of the 3 cases.
The full code is available here in the repo.

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
```

### List all station coordinates
To list all the stations coordinates (lon and lat) you can use the following code.

Notice, that it lists the stations available for a given month.
``` python
import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

response = requests.get(
    url='https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/dmi_list',
    params={'from_date': '2014-01'},
    headers={'Authorization': client_auth.get_access_token()}
)

print(response.status_code)
print(response.json())
```
The code will return all the available data.

### Retrieve data for a station
To retrieve data for a given station (specified by lon and lat) use similar code,
which retrieves data for a given date interval.
``` python
import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

response = requests.get(
    url='https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/dmi',
    params={'from_date': '2014-01', 'to_date': '2014-03', 'lon': '15.19', 'lat': '55.00'},
    headers={'Authorization': client_auth.get_access_token()}
)

print(response.status_code)
```
