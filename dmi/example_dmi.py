import pandas as pd
from io import BytesIO
from osiris.apis.egress import Egress
from configparser import ConfigParser


def example_dmi():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    parquet_content = egress.download_dmi_file(15.19, 55.00, '2021-01', '2021-03')

    result_df = pd.read_parquet(BytesIO(parquet_content))
    print(result_df)


def example_dmi_list():
    config = ConfigParser()
    config.read('conf.ini')

    egress = Egress(egress_url=config['Egress']['url'],
                    tenant_id=config['Authorization']['tenant_id'],
                    client_id=config['Authorization']['client_id'],
                    client_secret=config['Authorization']['client_secret'])

    station_coord = egress.download_dmi_list('2021-01')

    print(station_coord)


if __name__ == '__main__':
    example_dmi_list()
    example_dmi()
