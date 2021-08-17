from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from osiris.core.enums import Horizon
from configparser import ConfigParser


def example_delfin_daily():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'])

    json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01", "2020-02")

    print(json_content)


def example_delfin_hourly():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'])

    json_content = egress.download_delfin_file(Horizon.HOURLY, "2020-01-01T00", "2020-01-01T06")

    print(json_content)


def example_delfin_minutely():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'])

    json_content = egress.download_delfin_file(Horizon.MINUTELY, "2021-07-15T00:00", "2021-07-15T00:59")

    print(json_content)


def example_delfin_daily_table_indices():
    config = ConfigParser()
    config.read('conf.ini')

    client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                      client_id=config['Authorization']['client_id'],
                                      client_secret=config['Authorization']['client_secret'])

    egress = Egress(client_auth=client_auth,
                    egress_url=config['Egress']['url'])

    json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01-15T03:00", "2020-01-16T03:01",
                                               table_indices=[1, 2])

    print(json_content)


if __name__ == '__main__':
    example_delfin_daily()
    example_delfin_hourly()
    example_delfin_minutely()
    example_delfin_daily_table_indices()
