from osiris.apis.egress import Egress
from configparser import ConfigParser


def print_description(json_data):
    print(f'Number of events returned: {len(json_data)}')
    if len(json_data) > 0:
        print('Event entries:')
        print('  Field name                    Sample')
        print('-' * 50)
        for field_name, field_example in json_data[0].items():
            print(f'  {field_name:30} {field_example}')


def example_gtms_daily():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress API']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'],
                    dataset_guid=config['Egress API']['guid'])

    json_data = egress.download_json_file('2021-01-01', '2021-01-02')

    print_description(json_data)


def example_gtms_monthly():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress API']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'],
                    dataset_guid=config['Egress API']['guid'])

    json_data = egress.download_json_file('2021-06', '2021-08')

    print_description(json_data)


def example_gtms_no_horizon():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress API']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'],
                    dataset_guid=config['Egress API']['guid'])

    json_data = egress.download_json_file()

    print_description(json_data)


if __name__ == '__main__':
    # example_gtms_monthly()
    example_gtms_no_horizon()
    # example_gtms_daily()
