import time
import pyupbit
import datetime

access = "my"
secret = "key"

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_ma5(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        
        # ETC Box
        if end_time - datetime.timedelta(seconds=2) < now < end_time :
            ma15 = get_ma15("KRW-ETC")
            ma5 = get_ma5("KRW-ETC")
            current_price = get_current_price("KRW-ETC")
            
            if  ma5 < current_price and ma5 > ma15:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETC", krw*0.9)
             
            if ma5 > current_price and ma5 < ma15:
                etc = get_balance("ETC")
                upbit.sell_market_order("KRW-ETC", etc)
                      
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)
