import pulp as pl

# Створення моделі оптимізації виробництва
production_model = pl.LpProblem("Production_Optimization", pl.LpMaximize)

# Визначення змінних: кількість одиниць "Лимонаду" та "Фруктового соку"
limonad = pl.LpVariable('Limonad', lowBound=0, cat='Integer')
fruit_juice = pl.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Максимізація загальної кількості вироблених продуктів
production_model += limonad + fruit_juice, "Total_Production"

# Обмеження ресурсів:
# 1. Вода: використовується для обох продуктів.
#    "Лимонад" потребує 2 од. води, а "Фруктовий сік" – 1 од. води.
production_model += 2 * limonad + fruit_juice <= 100, "Water_Constraint"

# 2. Цукор: використовується лише для "Лимонаду" (1 од. цукру на одиницю лимонаду).
production_model += limonad <= 50, "Sugar_Constraint"

# 3. Лимонний сік: використовується лише для "Лимонаду" (1 од. лимонного соку на одиницю лимонаду).
production_model += limonad <= 30, "Lemon_Juice_Constraint"

# 4. Фруктове пюре: використовується лише для "Фруктового соку" (2 од. фруктового пюре на одиницю фруктового соку).
production_model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі (без виводу solver'а в консоль)
production_model.solve(pl.PULP_CBC_CMD(msg=0))

print("Оптимальна кількість Лимонаду:", pl.value(limonad))
print("Оптимальна кількість Фруктового соку:", pl.value(fruit_juice))
print("Максимальна загальна кількість продуктів:", pl.value(production_model.objective))
