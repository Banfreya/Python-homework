weight_both = int(input())
price_average = int(input())
first_price = int(input())
second_price = int(input())
second_weight = int(weight_both * (price_average -
                    first_price) / (second_price - first_price))
first_weight = int(weight_both - second_weight)
print(first_weight, second_weight, sep=" ")
