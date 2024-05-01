N = int(input())
ingredients = set()
for i in range(N):
    ingredient = input()
    ingredients.add(ingredient)
M = int(input())
counter = 0
recipes = []

for j in range(M):
    recipe_name = input()
    recipe = set()
    how_many = int(input())
    for o in range(how_many):
        need = input()
        recipe.add(need)
    check = recipe & ingredients
    if len(check) == len(recipe):
        recipes.append(recipe_name)
    else:
        counter += 1
if counter == M:
    print("Готовить нечего")
else:
    final_list = sorted(recipes)
    print("\n".join(final_list))
