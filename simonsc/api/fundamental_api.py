# -*- coding: utf-8 -*-
from simonsc.client import SimonsClient
from simonsc.utils import *


@assert_auth
@export_as_api
def get_table_data(query_object):
    sql = get_fundamentals_sql_from_query(query_object)
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)


@assert_auth
@export_as_api
def get_all_factor(order_book_ids: list(), bar_count: int, dt: datetime, fields: list(),
                   frequency='1d', data_type="balancesheet"):
    return SimonsClient.instance().get_all_factor(order_book_ids=order_book_ids, bar_count=bar_count, dt=dt,
                                                  fields=fields, frequency=frequency,
                                                  data_type=data_type)


if __name__ == '__main__':
    from simonsc import auth
    auth("quantresearch", "quantresearch")
    fs = ["MONETARY_CAP", "RIGHT_USE_ASSETS", ]
    data = get_all_factor(["000001.XSHE", "000002.XSHE", "000004.XSHE"], 20, "2021-03-01", fs, "1d")
    print(data)