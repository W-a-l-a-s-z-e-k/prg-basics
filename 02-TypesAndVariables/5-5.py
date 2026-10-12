price = float(input("enter price "))
discount = int(input("enter discount "))
reduction = price * discount/100
price_discount = price - reduction
print(f'original price {price} disocunt {discount}% price after discount {round(price_discount,2)} reduction {round(reduction,2)}')