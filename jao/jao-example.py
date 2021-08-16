from osiris.apis.egress import Egress
from configparser import ConfigParser
from osiris.core.enums import Horizon


def example_jao_monthly():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_jao_file(Horizon.MONTHLY, "2020-01", "2020-02")

    print(json_content)


def example_jao_yearly():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_jao_file(Horizon.YEARLY, "2020", "2021")

    print(json_content)


if __name__ == '__main__':
    example_jao_monthly()
    example_jao_yearly()