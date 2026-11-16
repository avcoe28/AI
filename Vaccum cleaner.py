def vacuum_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

room = {
    "A": input("Enter status of Room A (Dirty/Clean): "),
    "B": input("Enter status of Room B (Dirty/Clean): ")
}
location = input("Enter starting location (A/B): ")
print("\n--- Vacuum Cleaner Simulation ---")

while True:
    print("\nCurrent Location:", location)
    print("Room Status:", room)
    action = vacuum_reflex_agent(location, room[location])
    print("Action:", action)
    
    if action == "Suck":
        room[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
        
    if room["A"] == "Clean" and room["B"] == "Clean":
        print("\nBoth rooms are clean!")
        print("Agent stops.")
        break
