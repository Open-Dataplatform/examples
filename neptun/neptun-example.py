from osiris.apis.egress import Egress
from configparser import ConfigParser
from osiris.core.enums import Horizon


def example_neptun_daily():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_neptun_file(Horizon.DAILY, "2020-01", "2020-02")

    print(json_content)


def example_neptun_hourly():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_neptun_file(Horizon.HOURLY, "2020-01-15T03:00", "2020-01-15T03:01")

    print(json_content)


def example_neptun_minutely():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_neptun_file(Horizon.MINUTELY, "2020-01-15T03", "2020-01-15T04")

    print(json_content)


def example_neptun_daily_tags():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    json_content = egress.download_neptun_file(Horizon.DAILY, "2020-01-15T03:00", "2020-01-16T03:01",
                                               tags=['MW00001', 'MW00002'])

    print(json_content)


if __name__ == '__main__':
    example_neptun_daily()
    example_neptun_hourly()
    example_neptun_minutely()
    example_neptun_daily_tags()