f = open('Input/21.txt')

nutrition_facts = []
ingredients_for_allergens = {}

for line in f.read().splitlines():
    parts = line.split(' (contains ')
    ingredients = set(parts[0].split())
    allergens = set(parts[1][:-1].split(', '))
    for allergen in allergens:
        ingredients_for_allergens[allergen] = None
    nutrition_facts.append((ingredients, allergens))

def match_allergen_to_ingredient():
    for allergen, ingredient in ingredients_for_allergens.items():
        if ingredient:
            continue
        just_starting = True
        for ingredients, allergens in nutrition_facts:
            if allergen in allergens:
                if just_starting:
                    possible_ingredients = ingredients
                    just_starting = False
                else:
                    possible_ingredients = possible_ingredients.intersection(ingredients)
        if len(possible_ingredients) == 1:
            return allergen, possible_ingredients.pop()

while None in ingredients_for_allergens.values():
    allergen, ingredient = match_allergen_to_ingredient()
    ingredients_for_allergens[allergen] = ingredient
    for ingredients, allergens in nutrition_facts:
        ingredients.discard(ingredient)
        allergens.discard(allergen)

for allergen, ingredient in ingredients_for_allergens.items():
    print(allergen, "is in", ingredient)

print("answer:", sum([len(ingredients) for ingredients, allergens in nutrition_facts]))
