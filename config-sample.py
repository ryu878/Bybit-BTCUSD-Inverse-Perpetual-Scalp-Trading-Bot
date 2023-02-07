# Bybit settings
domain      = 'bybit'
endpoint    = 'https://api.bybit.com'
api_key     = ''                      # paste your API key here
api_secret  = ''                      # paste your API secret here

# Trading settings
symbol = 'BTCUSD'                     # asset to trade. Never tested on another asset.
csize = 1                             # lot size
min_fee = 0.17                        # min distance to take profit
divider = 7                           # deleverage divider
timeout = 3                           # pause in seconds between loops

# Database settings
# redis_host = '192.168.1.4'
redis_host = 'localhost'
redis_port = 6379
redis_db = 0
