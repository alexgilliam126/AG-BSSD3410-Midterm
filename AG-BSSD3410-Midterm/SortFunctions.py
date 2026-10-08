# Quicksort - Sort cars by price
def quick_sort(cars):
    if len(cars) <= 1:
        return cars

    pivot = int(cars[len(cars) // 2]["Price (in USD)"].replace(",", ""))

    left = []
    middle = []
    right = []

    for car in cars:
        price = int(car["Price (in USD)"].replace(",", ""))

        if price < pivot:
            left.append(car)
        elif price > pivot:
            right.append(car)
        else:
            middle.append(car)

    return quick_sort(left) + middle + quick_sort(right)
