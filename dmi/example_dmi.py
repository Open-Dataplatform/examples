import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser


def example_dmi():
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


def example_dmi_list():
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
