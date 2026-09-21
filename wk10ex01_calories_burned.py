def calculate_calories(minutes, calories_per_minute):
    return minutes * calories_per_minute


sessions = int(input("How many exercise sessions do you want to record? "))

calories_burned = []
total_calories = 0

for i in range(sessions):
    print(f"\nSession {i + 1}")

    minutes = float(input("Enter exercise minutes: "))
    calories_per_minute = float(input("Enter calories burned per minute: "))

    calories = calculate_calories(minutes, calories_per_minute)

    calories_burned.append(calories)
    total_calories += calories

print("\nCalories Burned Per Session:")

for i, calories in enumerate(calories_burned, 1):
    print(f"Session {i}: {calories:.2f} calories")

print(f"\nTotal Calories Burned: {total_calories:.2f} calories")
