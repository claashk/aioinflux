import aioinflux.testing_utils as utils
from aioinflux.client import logger


def test_write_dataframe(df_client):
    assert df_client.write(utils.random_dataframe(),
                           measurement='test_measurement', mytag='foo', tag_columns=['tag'])


def test_read_dataframe(df_client):
    df = df_client.select_all(measurement='test_measurement')
    logger.debug(df.head())
    assert df.shape == (50, 7)
