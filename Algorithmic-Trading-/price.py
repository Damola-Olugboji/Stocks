import yahoo_fin.stock_info as si
import sys

print(si.get_live_price(sys.argv[1]))
