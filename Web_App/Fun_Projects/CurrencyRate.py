#pip install forex-python
from forex_python.converter import CurrencyRates
c=CurrencyRates()

from_currency=input("Currently currency:").upper()
amount=int(input("exchange amount:"))
to_currency=input("Exchange to:").upper()

print(from_currency," to ",to_currency,amount)
result=c.convert(from_currency,to_currency,amount)
print(result)
