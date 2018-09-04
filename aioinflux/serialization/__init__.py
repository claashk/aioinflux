# flake8: noqa
from .. import pd

if pd:
    from . import dataframe
from . import mapping
from .datapoint import DataPoint


def parse_data(data, measurement=None, tag_columns=None, **extra_tags):
    """Converts input data into line protocol format"""
    if isinstance(data, bytes):
        return data
    elif isinstance(data, str):
        return data.encode('utf-8')
    elif isinstance(data, DataPoint):
        return data.to_lineprotocol()
    elif pd is not None and isinstance(data, pd.DataFrame):
        if measurement is None:
            raise ValueError("Missing 'measurement'")
        return dataframe.parse(data, measurement, tag_columns, **extra_tags)
    elif isinstance(data, dict):
        return mapping.parse(data, measurement, **extra_tags).encode('utf-8')
    elif hasattr(data, '__iter__'):
        return b'\n'.join([parse_data(i, measurement, tag_columns, **extra_tags) for i in data])
    else:
        raise ValueError('Invalid input', data)
