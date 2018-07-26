# BinanceArbitrageBot
Arbitrage Bot for Binance Cryptocurrency Exchange

Performs Triangular Arbitrage.  
All trades are in one of the two following forms:
    
    ETH -> Alt Coin -> BTC
    
    BTC -> Alt Coin -> ETH
    
    
    
    
## Quickstart:

  Go to your binance account and create a new API
  
  Make sure your API has "Read Info" and "Enable Trading" checked
  
  Copy and paste your API key and secret key into arbitrageBot.py
  
  Run arbitrageBot.py and then call transact()
  
  the function transact() causes the bot to start.  It runs through all the alt coins on binance and whenver it sees a profitable arbitrage opportunity it executes the necessary trades
    
    
    
  ## Notice:  
  If you don't have any BNB in your account to decrease fees you will want to change FEE in arbitrageBot.py from 0.9995 to 0.999.  Doing so will likely cause the bot to find much fewer trades so I recommend loading your accound with a small amount of BNB.
  
  
  
## Disclaimer:  
Use this bot at your own risk.  I take no responsibility for any losses you may incur as a result of this bot.  Losses and gains will largely be determined by response time, which will take into accound how fast your machine opperates and how close you are to 
binance's API servers. 

## Acknowledgements
Some of the code in binance.py is forked from @toshima's binance API wrapper: https://github.com/toshima/binance
