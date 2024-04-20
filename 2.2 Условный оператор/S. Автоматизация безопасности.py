x = float(input())
y = float(input())
island_circle_radius = 10
danger_zone_radius = 5
expedition_coordinates_projection = (x ** 2 + y ** 2) ** 0.5 
if expedition_coordinates_projection > island_circle_radius:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
elif x >= 0 and y >= 0 and expedition_coordinates_projection < danger_zone_radius:
        print("Опасность! Покиньте зону как можно скорее!")
        
else: 
        print("Зона безопасна. Продолжайте работу.")

