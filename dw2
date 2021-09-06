import time
import pyupbit
import datetime

access = "m9PVAYixUCUOwVR2lhZ9xrELAH19APSompiAR5XC"
secret = "qfHmtWmV3xnK5T6MwxUH1LFwLNGERChabMrmMHBQ"

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

        # BTC Coin 8:59:59초에 1번 매수/매도 판단 Logic
        if end_time - datetime.timedelta(seconds=2) < now < end_time :
            ma15 = get_ma15("KRW-BTC")
            ma5 = get_ma5("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            # 현재가가 5일 추세보다 높고 5일 추세가 15일 추세보다 높은 경우 매수
            if  ma5 < current_price and ma5 > ma15:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", int(krw*0.03))
            # 현재가가 5일추세보다 낮고 5일 추세가 15일 추세보다 낮은 경우 매도        
            if ma5 > current_price and ma5 < ma15:
                btc = get_balance("BTC")
                upbit.sell_market_order("KRW-BTC", btc*0.9995)

        # SAND Box
        if end_time - datetime.timedelta(seconds=2) < now < end_time :
            ma15 = get_ma15("KRW-SAND")
            ma5 = get_ma5("KRW-SAND")
            current_price = get_current_price("KRW-SAND")
            # 현재가가 5일 추세보다 높고 5일 추세가 15일 추세보다 높은 경우 매수
            if  ma5 < current_price and ma5 > ma15:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.03)
            # 현재가가 5일추세보다 낮고 5일 추세가 15일 추세보다 낮은 경우 매도        
            if ma5 > current_price and ma5 < ma15:
                sand = get_balance("SAND")
                upbit.sell_market_order("KRW-SAND", sand)                      
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)
