storage_point = int(input())
shop_point = int(input())
car_speed = int(input())
delivery_time = (shop_point - storage_point) / car_speed
formatted_delivery_time = f"{delivery_time:.2f}"
print(formatted_delivery_time)
