import pandas as pd
from io import BytesIO
from osiris.apis.egress import Egress
from osiris.core.azure_client_authorization import ClientAuthorization
from configparser import ConfigParser


config = ConfigParser()
config.read('conf.ini')

client_auth = ClientAuthorization(tenant_id=config['Authorization']['tenant_id'],
                                  client_id=config['Authorization']['client_id'],
                                  client_secret=config['Authorization']['client_secret'])

egress = Egress(client_auth=client_auth,
                egress_url=config['Egress']['url'],
                dataset_guid=config['Egress']['guid'])

data = egress.download_parquet_file(from_date='2019-02-01',
                                    to_date='2019-02-02')
data_df = pd.read_parquet(BytesIO(data), engine='pyarrow')

data_df.to_csv('data.csv', index=False)
