money = 1600
price = 1000

change=money-price
print("잔돈",change,"원")

c500=change//500
change=change%500

c100=change//100

print("coin500",c500,"개")
print("c100",c100,"개")