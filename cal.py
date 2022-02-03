
# python script for DRM
day = input("What is the current day: ")
price = input("What is todays price: ")

_day = int(day)
_price = float(price)

print('----------')
start_amount = 913.90

drm = 5.577715
usd_bal = drm * _price
print(f"""Total drm: {drm}
 Price in dollars: {usd_bal}""")

hourly_earns = 0.061527
print(f'Total earned each hour: {hourly_earns * _price}')

total_hourly_earns = (hourly_earns * 3)
print(f'Total day earned: {total_hourly_earns * _price}')

