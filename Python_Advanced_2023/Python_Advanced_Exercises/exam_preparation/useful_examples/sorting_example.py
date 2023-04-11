companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125}

# sorted by value
sorted_companies_data = sorted(companies.items(), key=lambda x: x[1])

# sorted by key
sorted_companies_data = sorted(companies.items(), key=lambda x: x[0])

# sorted first by value then by key
companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125, 'Acea': 125}
companies_data = sorted(companies.items(), key=lambda x: (x[1], x[0]))
print(sorted_companies_data)

#sort by the number of values first in descending order then by its key
sorted_values = sorted(companies.items(), key=lambda x: (-len(x[1]), x[0]))

result = ''
for tuple_ in sorted_values:
    result += f"{tuple_[0]}:\n"
    sorted_product = sorted(tuple_[1])
    for product in sorted_product:
        result += f" - {product}\n"


sorted_result = {k: v for k,v in sorted(locations.items(), key=lambda x: (x[0]))}