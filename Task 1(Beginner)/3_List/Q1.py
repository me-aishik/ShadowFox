justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

print(f"Number of Justice League Members: {len(justice_league)}\n")

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"Updated Number of Justice League Members: {len(justice_league)}\n")

justice_league[0]='Wonder Woman'
justice_league[2]='Superman'
print(f"Updated Justice League Members: {justice_league}\n")

justice_league.remove('Green Lantern')
justice_league.insert(len(justice_league)-3, 'Green Lantern')
print(f"Updated Justice League Members: {justice_league}\n")

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League members:", justice_league)

justice_league.sort()
print("\nSorted Justice League members:", justice_league)
print("\nNow the new Leader of the Justice League is:", justice_league[0])