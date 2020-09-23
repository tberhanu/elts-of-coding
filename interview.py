def get_tickers(datas, apples_ipo_date):
    lst = []
    for data in datas:
        if data["exchange"] == "NASDAQ" or data["ipo"] >= apples_ipo_date:
            lst.append(data["ticker"])
    return lst
