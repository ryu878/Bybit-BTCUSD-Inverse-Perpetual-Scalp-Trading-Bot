⛔    BYBIT Exchange Affiliate Program SCAM ALERT ⛔ 

I have received a letter from Bybit Exchange:

* "After a thorough internal investigation conducted by our risk team, your account was being flagged out from receiving Referral commissions due to a violation of our Terms of Service and Bonus...                                                            Let it be clear that this decision is final and we will not accommodate any further appeals regarding the matter."   

I must admit that this is totally scam behaviour from the exchange. I have a lot of referees and as I know a lot of them have passed KYC. Sometimes I help traders with trades on their accounts but I neved registered another account for myself to receive comission. But Bybit say that "According to our statistics, we found out that most users who have successfully registered using your referral link created their accounts using the same IP address." This is total lie. I can't register account for users.

Also I sent email to them regargind my ref id P11NJW. But there is no answer as well.

So then let it be CLEAR, that since 
* Bybit violate their own rules
* Bybit scam users
* I'll not receive a Referral commission anymore
* They don't reply and there is no support

this project is closed and there will be no more updates. I'll move all my code to Binance, OKX etc soon.

By their actions they undermine my authority and I can no longer recommend trading on this platform.

⛔    BYBIT Exchange Affiliate Program SCAM ALERT ⛔ 



`

`

`

`

`

`

`

`

# Bybit BTCUSD Inverse Perpetual Scalp Trading Bot <a href="https://github.com/ryu878/bybit_scalp_bot/blob/main/LICENSE.MD">[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://aadresearch.xyz) [![Generic badge](https://img.shields.io/badge/Python-3.8+-<COLOR>.svg)](https://aadresearch.xyz) 
  
[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)


Trading bot for Bybit exchange to trade BTCUSD perpetual contract. It use Redis database to cache the trades data.

That bot will only open shorts, because there are no liquidation price for 1x short on inverse contract and because in most cases funding rates for shorts are positive. If you want to make the bot trade longs you can just copy-paste the logic.

![image](https://user-images.githubusercontent.com/81808867/217010448-9f05188e-284c-4307-ac92-a2627f39dbc5.png)
  
Bot logic: bot collects trades from Bybit websocket and calculates high, low and average values for the last 6 minutes. It opens the trade always at higher price and adds more if average price higher the entry.
  

## Requirements

Install libraries:
  
Run <code>python3 -m venv .bot && source .bot/bin/activate</code> to create virtual env and activate it.  
  
<code>pip install pybit==2.4.1</code>

<code>pip install redis</code>



## How to run

1. Rename config-sample.py to config.py, open it and add your API key credentials. Save it.
2. Run
<code>docker-compose up -d</code> to download and run Redis server for you. Don't forget to limit access to port 8001 on your server. If you don't have docker-compose just run <code>docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest</code> to run Redis.
3. Run
<code>python3 ws_trades_inverse_redis.py</code> to run the script that will collect the data using Bybit websockets and save it to the Redis database. 
4. Run
<code>python3 inverse_bot_v5.0.py</code>


## Disclaimer

This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

  
## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch

Join me at Bybit and earn exclusive rewards with Bybit's Referral Program! 
Up to 1,025 USDT in rewards await you. https://www.bybit.com/invite?ref=P11NJW

## VPS for bots and scripts
I prefer using DigitalOcean. 

To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04

