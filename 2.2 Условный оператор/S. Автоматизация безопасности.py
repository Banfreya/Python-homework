x = float(input())
y = float(input())
island_circle_radius = 10
expedition_coordinates_projection = (x**2 + y**2) ** 0.5 
in_danger_zone_1 = x >= 0 and y >= 0 and expedition_coordinates_projection < 5
in_danger_zone_2 = x < 0 and y <= 5 and y <= ((5 * x) + 35) / 3
in_danger_zone_3_4 = y <= 0 and y < (0.25 * (x ** 2)) + (0.5 * x) + 8.75
if expedition_coordinates_projection > island_circle_radius:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_danger_zone_1 or in_danger_zone_2 or in_danger_zone_3_4:
    print("Опасность! Покиньте зону как можно скорее!")
else: 
    print("Зона безопасна. Продолжайте работу.")

