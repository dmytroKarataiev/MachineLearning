import math

days = 60
daily_rets = 0.001
daily_rf = 0.0002
std_daily = 0.001
k = math.sqrt(252)


def sharpe_daily(daily_rets, daily_rf, std_daily):
    """
    Sharpe ration: square root of 252 days (frequency of sampling)
    multiplied by mean of daily returns minus daily risk free returns
    divided by std deviation of daily returns
    :param daily_rets: mean of daily returns
    :param daily_rf: mean of risk free returns
    :param std_daily: std deviation of daily returns
    :return: share ratio
    """
    return k * (daily_rets - daily_rf) / std_daily


if __name__ == '__main__':
    print "Sharpe ration:", sharpe_daily(daily_rets, daily_rf, std_daily)
