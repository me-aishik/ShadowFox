total_jumping_jacks = 100
set_size = 10
completed = 0

while completed < total_jumping_jacks:
    # Perform a set
    completed += set_size
    print(f"You have completed {completed} jumping jacks.")

    # Check if workout is done
    if completed >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask if tired
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks are remaining.")
    elif tired in ["no", "n"]:
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks are remaining.")
    else:
        print("Invalid input! Continuing the workout...")

