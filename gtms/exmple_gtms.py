from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser


def print_description(json_data):
    print(f'Number of events returned: {len(json_data)}')
    if len(json_data) > 0:
        print('Event entries:')
        print('  Field name                     Sample')
        print('-' * 50)
        for field_name, field_example in json_data[0].items():
            print(f'  {field_name:30} {field_example}')


def example_gtms_date_range():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'],
                    dataset_guid=config['Egress']['guid'])

    json_response = egress.download_json_file('2014', '2015')

    print_description(json_response)


def example_gtms_full_data():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'],
                    dataset_guid=config['Egress']['guid'])

    json_response = egress.download_json_file()

    print_description(json_response)


if __name__ == '__main__':
    example_gtms_date_range()
    example_gtms_full_data()
