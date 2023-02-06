from pybit import inverse_perpetual
from config import *
import redis
import time
# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# sudo fuser -k 6379/tcp


# Bybit
invpcl = inverse_perpetual.HTTP(endpoint=endpoint, api_key=api_key, api_secret=api_secret)
ws = inverse_perpetual.WebSocket(test=False, domain=domain)
symbol = 'BTCUSD'
# Redis
# redis_host = '192.168.1.4'
redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_trade_ttl = 60 * 6
r = redis.Redis(host=redis_host,port=redis_port,db=redis_db)


def get_trades(trades):
    # print(trades)
    # tid             = trades['data'][0]['trade_id']
    symbol          = trades['data'][0]['symbol']
    price           = trades['data'][0]['price']
    # size            = trades['data'][0]['size']
    # timestamp       = trades['data'][0]['timestamp']
    trade_time_ms   = trades['data'][0]['trade_time_ms']
    # side            = trades['data'][0]['side']

    # r.hset(str(trade_time_ms), 'trade_id', tid)
    r.hset(str(symbol), 'price', price)
    r.hset(str(trade_time_ms), 'price', price)
    # r.hset(str(trade_time_ms), 'size', size)
    # r.hset(str(trade_time_ms), 'timestamp', timestamp)
    # r.hset(str(trade_time_ms), 'trade_time_ms', trade_time_ms)
    # r.hset(str(trade_time_ms), 'side', side)
    r.execute_command('expire',str(symbol), redis_trade_ttl)
    r.execute_command('expire',str(trade_time_ms), redis_trade_ttl)

    print(trade_time_ms)

ws.trade_stream(get_trades, symbol)

while True:

    time.sleep(1)