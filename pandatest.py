import pandas as pd
import random
import datetime

def random_dt_bw(start_date, end_date):
    days_between = (end_date - start_date).days
    random_num_days = random.randrange(days_between)
    random_dt = start_date + datetime.timedelta(days=random_num_days)
    return random_dt


def generate_data(n=1000):
    items = [f"i_{x}" for x in range(n)]
    start_dates = [random_dt_bw(datetime.date(
        2020, 1, 1), datetime.date(2020, 9, 1)) for x in range(n)]
    end_dates = [
        x + datetime.timedelta(days=random.randint(1, 10)) for x in start_dates]

    offerDf = pd.DataFrame({"Item": items,
                            "StartDt": start_dates,
                            "EndDt": end_dates})

    transaction_items = [f"i_{random.randint(0,n)}" for x in range(5*n)]
    transaction_dt = [random_dt_bw(datetime.date(
        2020, 1, 1), datetime.date(2020, 9, 1)) for x in range(5*n)]
    sales_amt = [random.randint(0, 1000) for x in range(5*n)]

    transactionDf = pd.DataFrame(
        {"Item": transaction_items, "TransactionDt": transaction_dt, "Sales": sales_amt})

    return offerDf, transactionDf

