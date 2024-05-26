
total_cost = 0
продукт = []

with open('93.txt', newline='') as f:
    reader = f.read
    for row in reader:
        if len(row) == 3:
            продукт, количество, цена = row
            total_cost += int(количество) * int(цена)
            продукт.append(f"{продукт} - {количество} шт. за {цена} руб.")

print("Нужно купить:")
for продукт in продукт:
    print(продукт)

print(f"Итоговая сумма: {total_cost} руб.")