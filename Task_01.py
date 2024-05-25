import pulp


# Модель оптимізації
model = pulp.LpProblem("Максимізація_виробництва", pulp.LpMaximize)

# Оголошення змінних рішення - кількість одиниць "Лимонаду" та "Фруктового соку"
x1 = pulp.LpVariable("Лимонад", 0, None, pulp.LpInteger)
x2 = pulp.LpVariable("Фруктовий_сік", 0, None, pulp.LpInteger)

# Обмеження ресурсів
model += 2 * x1 + 1 * x2 <= 100, "Вода"
model += 1 * x1 <= 50, "Цукор"
model += 1 * x1 <= 30, "Лимонний_сік"
model += 2 * x2 <= 40, "Фруктове_пюре"

# Загальна_кількість_напоїв
model += x1 + x2

# Розв'язок задачі
model.solve()

# Виведення результатів
print("Виробництво Лимонаду:", x1.varValue)
print("Виробництво Фруктового соку:", x2.varValue)
print("Максимальна загальна кількість напоїв:", pulp.value(model.objective))