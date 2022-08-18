import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """

        csv_path = '/home/ewa/code/mewa-rewa/data-challenges/04-Decision-Science/data/csv/'
        root_dir = os.path.dirname(os.path.dirname(__file__))

        file_names = ['olist_sellers_dataset.csv',
            'olist_order_reviews_dataset.csv',
            'olist_order_items_dataset.csv',
            'olist_customers_dataset.csv',
            'olist_orders_dataset.csv',
            'olist_order_payments_dataset.csv',
            'product_category_name_translation.csv',
            'olist_products_dataset.csv',
            'olist_geolocation_dataset.csv']

        key_names = ['sellers',
            'order_reviews',
            'order_items',
            'customers',
            'orders',
            'order_payments',
            'product_category_name_translation',
            'products',
            'geolocation']

        data_frames = []
        for name in file_names:
            data_frames.append(pd.read_csv(os.path.join(root_dir, csv_path, name)))
        data = {}
        for i in range(9):
            data[key_names[i]]= data_frames[i]

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
