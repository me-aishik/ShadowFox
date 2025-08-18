Australia=['Sydney', 'Melbourne', 'Brisbane', 'Perth']
UAE=['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman']
India=['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
city1 = input("Enter the name of the city: ")
city2 = input("Enter another city name: ")
if city1 and city2 in Australia:
    print(f"{city1} and {city2} are both in Australia.")
elif city1 and city2 in UAE:
    print(f"{city1} and {city2} are both in the UAE.")
elif city1 and city2 in India:
    print(f"{city1} and {city2} are both in India.")
else:
    print(f"{city1} and {city2} are not belonging to the same country.")