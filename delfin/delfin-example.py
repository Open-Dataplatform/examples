from osiris.apis.egress import Egress
from configparser import ConfigParser
from osiris.core.enums import Horizon


def example_delfin_daily():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_delfin_file(Horizon.DAILY, "2020-01", "2020-02")

    print(json_content)


def example_delfin_hourly():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_delfin_file(Horizon.HOURLY, "2020-01-01T00", "2020-01-01T06")

    print(json_content)


def example_delfin_minutely():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_delfin_file(Horizon.MINUTELY, "2021-01-02T00", "2021-01-04T06")

    print(json_content)


if __name__ == '__main__':
    example_delfin_daily()
    example_delfin_hourly()
    example_delfin_minutely()
