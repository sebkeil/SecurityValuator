from django.shortcuts import render

from scrapy import Selector

import requests
import numpy as np
import pandas as pd


# Create your views here.

def yahoo_spider_index_view(request):
    return render(request, 'yahoo_spider/yahoo_spider_index.html', context={})

def yahoo_spider_balance_sheet_view(request):

    ticker_symbol = request.POST.get('stock_ticker')

    url = "https://finance.yahoo.com/quote/" + ticker_symbol + "/financials?p=" + ticker_symbol

    html = requests.get(url).content

    sel = Selector(text=html)

    table_rows = sel.xpath('//div[contains(@class,"D(tbr)")]')

    assert len(table_rows) > 0

    parsed_rows = []

    for table_row in table_rows:
        parsed_row = []
        el = table_row.xpath("./div")

        none_count = 0

        for rs in el:
            try:
                (text,) = rs.xpath('.//span/text()[1]').extract()
                parsed_row.append(text)
            except ValueError:
                parsed_row.append(np.NaN)
                none_count += 1

        if (none_count < 4):
            parsed_rows.append(parsed_row)

    df = pd.DataFrame(parsed_rows)
    df = df.set_index(0)
    df = df.transpose()

    cols = list(df.columns)
    cols[0] = 'Date'
    df = df.set_axis(cols, axis='columns', inplace=False)

    # convert data types to numeric

    numeric_cols = list(df.columns)[1::]

    for column_name in numeric_cols:
        df[column_name] = df[column_name].str.replace(',', '')  # Remove the thousands separator
        df[column_name] = df[column_name].astype(np.float64)  # Convert the column to float64

    df = df.transpose(copy=True).round(0)

    print(df)
    print(df.dtypes)

    context = {
        'ticker_symbol': ticker_symbol,
        'balance_sheet_df': df.to_html()
    }

    return render(request, 'yahoo_spider/yahoo_spider_balance_sheet.html', context=context)


