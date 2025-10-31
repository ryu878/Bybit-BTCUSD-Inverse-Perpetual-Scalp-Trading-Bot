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


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📞 Contact Me

I develop trading bots of any complexity, dashboards, and indicators for crypto exchanges, forex, and stocks. 🚀

To contact me, please send a message:

*   **Telegram:** [https://t.me/ryu8777](https://t.me/ryu8777) ✈️
*   **Discord:** [https://discord.gg/zSw58e9Uvf](https://discord.gg/zSw58e9Uvf) 🤝

***

## 🤝 Become My Crypto Partner

Start your trading journey on Bybit! Join using my referral link below:

**Join Bybit:** [https://www.bybit.com/invite?ref=P11NJW](https://www.bybit.com/invite?ref=P11NJW)

***

## 🖥️ VPS for Your Bots and Scripts

Keep your bots running 24/7! I prefer and recommend using **DigitalOcean**.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

**Get $200 in credit over 60 days** by using my referral link:

👉 [https://m.do.co/c/3d7f6e57bc04](https://m.do.co/c/3d7f6e57bc04)
