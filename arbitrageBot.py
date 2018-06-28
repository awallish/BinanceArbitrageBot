import binance
import math



keys = {"api" : "Your API Key", "secret" : "Your Secret Key"}

FEE = 0.9995    # fee adjustment

binance.set(keys["api"], keys["secret"])
binance.initializeLotInfo()
lots = binance.lots

# coins which contain both eth and btc trading pairs
selectCoins = ['SC',  'LSK', 'LTC', 'QTUM', 'EOS', 'BNT', 'BCC', 'HSR', 'OAX', 
               'DNT', 'MCO', 'ICN', 'ZRX', 'OMG', 'WTC', 'LRC', 'YOYO', 'TRX', 'STRAT', 
               'SNGLS', 'KNC', 'BQX', 'SNM', 'FUN', 'LINK', 'XVG', 'SALT', 'MDA', 'IOTA', 
               'SUB', 'ETC', 'MTL', 'ARK', 'MTH', 'ENG', 'AST', 'DASH', 'BTG', 'EVX', 'REQ', 
               'VIB', 'POWR', 'BNB', 'XRP', 'MOD', 'ENJ', 'STORJ', 'VEN', 'KMD', 'RCN', 'NULS', 
               'RDN', 'XMR', 'DLT', 'AMB', 'BAT', 'ZEC', 'BCPT', 'ARN', 'CDT', 'GXS', 'POE', 
               'QSP', 'BTS', 'NEO', 'XZC', 'TNT', 'FUEL', 'MANA', 'BCD', 'DGD', 'ADX', 'ADA', 
               'PPT', 'CMT', 'XLM', 'CND', 'LEND', 'WABI', 'WAVES', 'TNB', 'GTO', 'ICX', 'OST', 
               'ELF', 'AION', 'SYS', 'LOOM', 'BRD', 'VIA','NANO','GRS','IOST','DATA','NXS',
               'WPR','INS','XEM','QKC','CHAT','ZIL','THETA','POA','ZEN','VIBE','RPX','BCN',
               'NEBL','BLZ','AE','CLOAK','STEEM','QLC','AGI','GNT','WAN','REP','RLC','STORM',
               'CVC','IOTX','ONT','SKY','LUN','NCASH','TUSD','EDO','WINGS','NAV','TRIG','APPC',
               'PIVX'
               ]



def getMin(symbol):
    """ minimum quantity of asset required by binance for trade """
    
    return float(lots[symbol]['minQty'])


def getStepSize(symbol):
    """ step size required for asset """
    
    return float(lots[symbol]['stepSize'])
    

def getDigits(symbol):
    """ decimal precision supported by binance for asset """
    
    return float(lots[symbol]['digits'])


def checkArbitrage(token):
    """ usdt -> eth -> token -> btc -> usdt 
        returns the one to one value of your investment after running through the trades outlined above
        if the value is greater than one then there is profit to be made through arbitrage
    """
    
    return 1/float(binance.prices()['ETHUSDT'])*FEE*1/float(binance.prices()[token+'ETH'])*FEE*float(binance.prices()[token+'BTC'])*FEE*float(binance.prices()['BTCUSDT'])
    


def executeTrades(token):
    """
    carries out the trades identified and specified in checkArbitrage(token)
    
    Flooring and rounding is used in the quantity calculations so as to make sure that the amount
    matches the step size and minimum quantities required by binance for the given asset
    """
    binance.marketBuy("ETHUSDT", binance.BUY, round(math.floor(100000*int(float(binance.balances()["USDT"]['free'])))*1/float(binance.prices()["ETHUSDT"]) / 100000, 5), test=False)
    binance.marketBuy(token+"ETH", binance.BUY, math.floor((10**getDigits(token)*int(float(binance.balances()["ETH"]['free'])*1/float(binance.prices()[token+"ETH"]))))/(10**getDigits(token)), test=False)
    binance.marketBuy(token+"BTC", binance.SELL, math.floor((10**getDigits(token))*float(binance.balances()[token]["free"]))/(10**getDigits(token)), test=False)
    binance.marketBuy("BTCUSDT", binance.SELL, math.floor(float(binance.balances()["BTC"]['free'])*1000000) / 1000000, test=False) # precision will always be 10^6 for BTC

  
  
def viewOpportunities(coins):
    """scans market for arbitrage opportunites using the two strategies defined in route3 and route4
    prints out any profitable trades
    for research use
    """
    for tick in coins:
        val = checkArbitrage(tick)
        if val > 1:
            print(str(val) + " usdt -> eth -> " + tick + " -> btc -> usdt")

            
            
def transact():
    """
    Main loop of the program:
        runs through all of the cryptocurrencies listed abouve and determines if arbitrage will be profitable
        and makes the transactions if it will be.
    """
    while True:
        for tick in selectCoins:
            
            val = checkArbitrage(tick)
            if val >= 1.003:
                executeTrades(tick)
                print(str(val) + " usdt -> eth -> " + tick + " -> btc -> usdt")