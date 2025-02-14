![image](https://github.com/user-attachments/assets/ff2a22d2-0405-41e8-84f4-a8869bcdf3c2)

# Announcement: Discontinuation of Free Bots for Bybit 
I regret to inform that I will no longer be updating or maintaining my free trading bots for the Bybit exchange. This decision comes after a deeply disappointing experience with Bybit's unethical practices, particularly regarding their affiliate program and their handling of user earnings.

Despite fully complying with Bybit's rules, including completing KYC (Know Your Customer) requirements, my affiliate earnings were abruptly terminated without valid justification. Bybit cited "one IP address" as the reason, a claim that is both unreasonable and unfair, especially for users in shared living environments or using shared internet connections. This behavior demonstrates a lack of transparency and fairness, and it has eroded my trust in Bybit as a reliable platform.

As a result, I have decided to shift my focus to [BingX](https://bingx.com/invite/HAJ8YQQAG/), a more transparent and user-friendly exchange that aligns with my values of fairness and integrity. Moving forward, I will be developing and updating trading bots exclusively for [BingX](https://bingx.com/invite/HAJ8YQQAG/), and I encourage my community to explore this platform as a viable alternative to Bybit.

I want to thank everyone who has supported my work and used my free bots for Bybit. Your trust and feedback have been invaluable, and I hope to continue providing value to the crypto community through my future projects on [BingX](https://bingx.com/invite/HAJ8YQQAG/). Stay tuned for updates, and feel free to reach out if you have any questions or need assistance during this transition.

Thank you for your understanding and support.

---

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

🐀 Join Bybit and receive up to $6,045 in Bonuses: https://www.bybit.com/invite?ref=P11NJW

😎 Register on BingX and get a **20% discount** on fees: https://bingx.com/invite/HAJ8YQQAG/


## VPS for bots and scripts
I prefer using DigitalOcean. 

To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04

