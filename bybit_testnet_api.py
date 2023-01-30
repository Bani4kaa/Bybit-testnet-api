import ccxt
import config2
from pybit import account_asset
from pybit import spot





#custom imports




#end of custom imports

api_key = config2.api_key
secret = config2.secret

# initialize the Bybit exchange object
bybit = ccxt.bybit({
    'rateLimit': 3000,
    'enableRateLimit': True,
    'apiKey': api_key,
    'secret': secret,
    'urls': {
        'test': 'https://api-testnet.bybit.com',
        'logo': 'https://testnet.bybit.com/app/themes/dark/public/img/common/logo-bybit.svg',
    },
    'test': True,
})

session_auth = account_asset.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key=api_key,
    api_secret=secret)


session_unauth = spot.HTTP(
    endpoint="https://api-testnet.bybit.com"
)



exchange = ccxt.bybit(
    {
    'apiKey': api_key,
    'secret': secret,
    }
)


exchange = ccxt.bybit(
    {'enableRateLimit': True,
        'apiKey': api_key,
    'secret': secret,})
exchange.set_sandbox_mode(True)

# end of Authentication