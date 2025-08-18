import random

num_rolls = 20

count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0
previous_roll = None

for i in range(num_rolls):
    roll = random.randint(1, 6) 
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1
    previous_roll = roll

# Print statistics
print("\nStatistics:")
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_two_6s_in_a_row}")
