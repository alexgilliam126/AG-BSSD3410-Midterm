# Find Me a Car - Algorithms Midterm
# BSSD 3410
#
# Dataset Source:
# Sports Car Prices Dataset - Kaggle
# https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset
#
import csv
from SortFunctions import quick_sort

cars = []
seen = set()

# Reads the sports car dataset
with open("Sport car price.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # see duplicate cars
        car_id = (
            row["Car Make"],
            row["Car Model"],
            row["Year"],
            row["Horsepower"],
            row["Price (in USD)"]
        )

        if car_id not in seen:
            seen.add(car_id)
            cars.append(row)

print("===== FIND ME A CAR =====")
print("Total unique cars:", len(cars))

# Allow the user to search again
while True:
    print()
    max_price = int(input("Enter your maximum price ($): "))
    min_hp = int(input("Enter minimum horsepower: "))

    matches = []

    # Linear search through the cars
    for car in cars:
        try:
            price = int(car["Price (in USD)"].replace(",", ""))
            horsepower = int(car["Horsepower"].replace(",", ""))

            if price <= max_price and horsepower >= min_hp:
                matches.append(car)

        except (ValueError, TypeError):
            continue

    print()
    print("===== MATCHING CARS =====")
    print("Total matches:", len(matches))

    if len(matches) > 0:
        # Sort matching cars using Quicksort
        matches = quick_sort(matches)

        print()
        print("===== SORTED CARS (LOWEST PRICE FIRST) =====")

        for car in matches[:10]:
            print(
                car["Car Make"],
                car["Car Model"],
                "| Year:", car["Year"],
                "| HP:", car["Horsepower"],
                "| Price: $", car["Price (in USD)"]
            )

    else:
        print("No cars found. Try a different budget or horsepower.")

    # Ask if the user wants to search again
    print()
    again = input("Would you like to search again? (y/n): ")

    if again.lower() != "y":
        print("Thanks for using Find Me a Car!")
        break
