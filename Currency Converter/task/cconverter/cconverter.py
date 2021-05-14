import requests

my_currency = input().lower()
my_dict = {}
while True:
    target_currency = input().lower()
    if target_currency == '':
        break
    amount = float(input())
    url = "http://www.floatrates.com/daily/" + my_currency +".json"
    r = requests.get(url).json()
    if my_currency == "eur":
        usd_rate = r["usd"]["rate"]
        my_dict["usd"] = usd_rate
    elif my_currency == "usd":
        eur_rate = r["eur"]["rate"]
        my_dict["eur"] = eur_rate
    else:
        usd_rate = r["usd"]["rate"]
        eur_rate = r["eur"]["rate"]
        my_dict["usd"] = usd_rate
        my_dict["eur"] = eur_rate
    print('Checking the cache...')
    total = round(amount * r[target_currency]["rate"], 2)
    for key in my_dict.keys():
        if key == target_currency:
            print("Oh! It is in the cache!")
            print(f"You received {total} {target_currency.upper()}")
    if target_currency not in my_dict.keys():
        print('Sorry, but it is not in the cache!')
        print(f"You received {total} {target_currency.upper()}")
        my_dict[target_currency] = r[target_currency]["rate"]








