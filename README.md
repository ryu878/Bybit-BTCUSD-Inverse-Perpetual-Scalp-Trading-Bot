# Bybit BTCUSD Inverse Pepretual Scalp Trading Bot <a href="https://github.com/ryu878/bybit_scalp_bot/blob/main/LICENSE.MD">[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://aadresearch.xyz) [![Generic badge](https://img.shields.io/badge/Python-3.8+-<COLOR>.svg)](https://aadresearch.xyz) 
  
[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)


Trading bot for Bybit exchange to trade BTCUSD perpetual contract. It use Redis database to cashe the trades data.

That bot will only open shorts, because there are no liquidation price for 1x short on inverse contract and because in most cases funding rates for shorts are positive. If you want to make the bot trade longs you can just copy-paste the logic.

![image](https://user-images.githubusercontent.com/81808867/217010448-9f05188e-284c-4307-ac92-a2627f39dbc5.png)
  
Bot logic: bot collects trades from Bybit websocket and calculates high, low and average values for the last 6 minutes. It opens the trade always at higher price and adds more if average price higher the entry.
  

## Requirements
You need bybit and binance accounts and APIs.

Install libraries:
  
<code>pip install pybit</code>

<code>pip install redis</code>



## How to run
1. Rename config-sample.py to config.py, open it and add your API key credentials. Save it.
2. Run
<code>docker-compose up -d</code>
- it will download and run Redis server for you. Don't forget to limit access to port 8001 on your server.
3. Run
<code>python3 ws_trades_inverse_redis.py</code>
- it will run script that will collect the data using Bybit websockets and save it to the Redis database.
4. Run
<code>python3 inverse_bot_v5.0.py</code>


## Disclaimer
<hr>
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
<hr>

## Contacts
Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch


