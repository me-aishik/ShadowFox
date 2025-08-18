Australia=['Sydney', 'Melbourne', 'Brisbane', 'Perth']
UAE=['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman']
India=['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
city = input("Enter the name of the city: ")
if city in Australia:
    print(f"{city} is in Australia.")
elif city in UAE:
    print(f"{city} is in the UAE.")
elif city in India:
    print(f"{city} is in India.")
else:
    print(f"{city} is not in the list.")    