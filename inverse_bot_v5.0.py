# Bybit BTCUSD Inverse Perpetual Scalp Trading Bot
# ------------------------------------------------
# (C) 2022 Ryan Hayabusa, AAD Research
# Github: https://github.com/ryu878 
# Mail: ev4AR2xihu3xXcdbYy5djGpfe01@gmail.com
# Web: https://aadresearch.xyz
# Discord: https://discord.gg/zSw58e9Uvf
# Telegram channel: https://t.me/aadresearch
# ------------------------------------------------
# python3 -m venv .bot && source .bot/bin/activate
# pip install pybit redis
# ------------------------------------------------
# docker-compose up -d
# sudo fuser -k 6379/tcp

import time
import redis
from config import *
from inspect import currentframe
from pybit import inverse_perpetual



title = 'Ryuryu\'s Bybit BTCUSD Inverse Perpetual Scalp Trading Bot'
ver = 'v5.0'


terminal_title = title+ver
print(f'\33]0;{terminal_title}\a', end='', flush=True)

unauth = inverse_perpetual.HTTP(endpoint=endpoint)
invpcl = inverse_perpetual.HTTP(endpoint=endpoint, api_key=api_key, api_secret=api_secret)
r = redis.Redis(host=redis_host,port=redis_port,db=redis_db)


# symbol = input(' What Asset To trade? ')
# symbol = (symbol+'USD').upper()


def get_linenumber():
    cf = currentframe()
    global line_number
    line_number = cf.f_back.f_lineno


def query_symbols():
    get_symbols = unauth.query_symbol()
    for asset in get_symbols['result']:
        if asset['name'] == symbol:
            global price_scale, tick_size, min_price, min_trading_qty, qty_step
            price_scale     = asset['price_scale']
            tick_size       = float(asset['price_filter']['tick_size'])
            min_price       = asset['price_filter']['min_price']
            min_trading_qty = asset['lot_size_filter']['min_trading_qty']
            qty_step        = asset['lot_size_filter']['qty_step']


def get_inverse_balance():
    get_inverse_balance = invpcl.get_wallet_balance(coin='BTC')
    global inv_perp_equity, inv_perp_available_balance, inv_perp_used_margin, inv_perp_order_margin, inv_perp_order_margin, inv_perp_position_margin, inv_perp_occ_closing_fee, inv_perp_occ_funding_fee, inv_perp_wallet_balance, inv_perp_realised_pnl, inv_perp_unrealised_pnl, inv_perp_cum_realised_pnl
    inv_perp_equity = get_inverse_balance['result']['BTC']['equity']
    inv_perp_available_balance = get_inverse_balance['result']['BTC']['available_balance']
    inv_perp_used_margin = get_inverse_balance['result']['BTC']['used_margin']
    inv_perp_order_margin = get_inverse_balance['result']['BTC']['order_margin']
    inv_perp_position_margin = get_inverse_balance['result']['BTC']['position_margin']
    inv_perp_occ_closing_fee = get_inverse_balance['result']['BTC']['occ_closing_fee']
    inv_perp_occ_funding_fee = get_inverse_balance['result']['BTC']['occ_funding_fee']
    inv_perp_wallet_balance = get_inverse_balance['result']['BTC']['wallet_balance']
    inv_perp_realised_pnl = get_inverse_balance['result']['BTC']['realised_pnl']
    inv_perp_unrealised_pnl = get_inverse_balance['result']['BTC']['unrealised_pnl']
    inv_perp_cum_realised_pnl = get_inverse_balance['result']['BTC']['cum_realised_pnl']


def get_sell_position():
    position = invpcl.my_position(symbol=symbol)
    # print(position)
    if position['result']['side'] == 'None':
        global sell_position_size, sell_position_prce
        sell_position_size = 0
        sell_position_prce = 0
    if position['result']['side'] == 'Sell':
        sell_position_size = float(position['result']['size'])
        sell_position_prce = float(position['result']['entry_price'])


try:
    query_symbols()
    
except Exception as e:
    get_linenumber()
    print(line_number, 'exeception: {}'.format(e))
    pass
print(symbol,price_scale,tick_size,min_price,min_trading_qty,qty_step)

time.sleep(0.01)


try:
    get_inverse_balance()

except Exception as e:
    get_linenumber()
    print(line_number, 'exeception: {}'.format(e))
    pass
print(' Inverse Balance:',inv_perp_available_balance, inv_perp_equity, inv_perp_wallet_balance, inv_perp_realised_pnl, inv_perp_unrealised_pnl)
time.sleep(0.01)


limit_sell_order_id = 0


while True:

    start_time = time.time()
    print('')

    python_list = r.keys('*')

    my_list = []

    for items in python_list:
        # item = int(items)
        item = items
        # print(item)
        
        get_price = r.hgetall(item).get(b'price')
        if get_price is not None:
            get_price = float(get_price)
            
            # print(get_price)
            my_list.append(get_price)
        else:
            pass
    # print(my_list)

    max_price = max(my_list)
    min_price = min(my_list)
    avr_price = round((sum(my_list)/len(my_list)),2)
    print('         Max 6:',max_price)
    print('         Min 6:',min_price)
    print('     Average 6:',avr_price)

    end_time = time.time()
    elapsed_time = round((end_time - start_time),2)
    print('     Exec time:', elapsed_time, 'seconds')

    ask_price = max_price+tick_size
    print('')
    print('           Ask:',ask_price)
    
    try:
        current_price = r.hgetall('BTCUSD').get(b'price')
        current_price = float(current_price)

    except Exception as e:
        get_linenumber()
        print(line_number, 'exeception: {}'.format(e))
        pass
    
    print(' Current_price:',current_price)

    print('')

    try:
        get_sell_position()

    except Exception as e:
        get_linenumber()
        print(line_number, 'exeception: {}'.format(e))
        pass

    print(' Sell Pozition:',sell_position_size,sell_position_prce)


    # First Entry
    # -----------
    if sell_position_size == 0 and sell_position_prce == 0:
        # Cancel Sell Limit First if Exists
        if limit_sell_order_id != 0:
            try:
                cancel_limit_sell_entry = invpcl.cancel_active_order(
                    symbol      = symbol, 
                    order_id    = limit_sell_order_id
                )

            except Exception as e:
                get_linenumber()
                print(line_number, 'exeception: {}'.format(e))
                pass

        try:
            limit_sell = invpcl.place_active_order(
                side        = 'Sell',
                symbol      = symbol,
                order_type  = 'Limit',
                qty         = csize,
                price       = ask_price,
                reduce_only = False, time_in_force = 'GoodTillCancel', close_on_trigger = False, post_only = True
            )
            # print(limit_sell)
            limit_sell_order_id = limit_sell['result']['order_id']
            rate_limit          = limit_sell['rate_limit']
            print(' Limit Sell Placed')
            print('', limit_sell_order_id)
            print(' Rate limit:',rate_limit)

        except Exception as e:
            get_linenumber()
            print(line_number, 'exeception: {}'.format(e))
            pass
    

    # Additional Entry
    # ----------------

    if sell_position_size > 0 and\
       sell_position_prce > 0 and\
       avr_price > sell_position_prce:

        if limit_sell_order_id != 0:
            try:
                cancel_limit_sell_entry = invpcl.cancel_active_order(
                    symbol      = symbol, 
                    order_id    = limit_sell_order_id
                )
            except Exception as e:
                get_linenumber()
                print(line_number, 'exeception: {}'.format(e))
                pass

        try:
            limit_sell = invpcl.place_active_order(
                side        = 'Sell',
                symbol      = symbol,
                order_type  = 'Limit',
                qty         = csize,
                price       = ask_price,
                reduce_only = False, time_in_force = 'GoodTillCancel', close_on_trigger = False, post_only = True
            )
            # print(limit_sell)
            limit_sell_order_id = limit_sell['result']['order_id']
            rate_limit          = limit_sell['rate_limit']
            print(' Limit Sell Placed')
            print('', limit_sell_order_id)
        except Exception as e:
            get_linenumber()
            print(line_number, 'exeception: {}'.format(e))
            pass

    if sell_position_size > 0 and\
       sell_position_prce > 0 and\
       avr_price < sell_position_prce:

       print(' Average Price Lower than Entry Price.\n Waiting...')


    # Take Profit
    # -----------
    try:
        current_price = r.hgetall('BTCUSD').get(b'price')
        current_price = float(current_price)
    except Exception as e:
        get_linenumber()
        print(line_number, 'exeception: {}'.format(e))
        pass

    try:
        get_sell_position()
    except Exception as e:
        get_linenumber()
        print(line_number, 'exeception: {}'.format(e))
        pass

    # Define Deleverage Lot Size
    if sell_position_size / divider < min_trading_qty:
        lot_size_market_tp = sell_position_size
    
    if sell_position_size / divider < min_trading_qty * divider:
        lot_size_market_tp = sell_position_size


    tp_price = float((100 - min_fee) * sell_position_prce / 100)

    print(' TP Price:',tp_price)
    
    if float(current_price) < float(tp_price):
                  
        try:
            place_buy_market_tp_order = invpcl.place_active_order(
            side          = 'Buy',
            symbol        = symbol,
            order_type    = 'Market',
            qty           = lot_size_market_tp,
            time_in_force = 'GoodTillCancel', reduce_only = True, close_on_trigger = True
            )
        except Exception as e:
            get_linenumber()
            print(line_number, 'exeception: {}'.format(e))
            pass
    else:
        print(' No Time for Take Profit Yet')


    time.sleep(3)
