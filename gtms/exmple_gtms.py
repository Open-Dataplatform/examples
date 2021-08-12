import requests
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser


def print_description(json_data):
    print(f'Number of events returned: {len(json_data)}')
    if len(json_data) > 0:
        print('Event entries:')
        print('  Field name                    Sample')
        print('-' * 50)
        for field_name, field_example in json_data[0].items():
            print(f'  {field_name:30} {field_example}')


def example_gtms_data():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    guid = config['Dataset']['guid']

    response = requests.get(
        url=f'https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/{guid}/test_json',
        params={'from_date': '2014-01', 'to_date': '2015-05'},
        headers={'Authorization': client_auth.get_access_token()}
    )

    print(response.status_code)
    print_description(response.json())


if __name__ == '__main__':
    example_gtms_data()