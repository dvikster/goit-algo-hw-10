import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення інтегрованої функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0   # нижня межа
b = 2   # верхня межа

# ----------- Метод Монте-Карло -----------
def monte_carlo_integration(f, a, b, N=1000000):
    x_rand = np.random.uniform(a, b, N)
    avg_value = np.mean(f(x_rand))
    integral_estimate = (b - a) * avg_value
    return integral_estimate

# Обчислення інтегралу методом Монте-Карло
N = 1000000
integral_mc = monte_carlo_integration(f, a, b, N)

# ----------- Інтеграл за допомогою SciPy (quad) -----------
integral_quad, error_quad = spi.quad(f, a, b)

# Виведення результатів
print("Результат інтегрування методом Монте-Карло:", integral_mc)
print("Результат інтегрування за допомогою quad:", integral_quad)
print("Абсолютна похибка:", abs(integral_mc - integral_quad))
print("Оцінка похибки (quad):", error_quad)

# ----------- Побудова графіка -----------
# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання графіка функції
ax.plot(x, y, 'r', linewidth=2, label=r'$f(x)=x^2$')

# Заповнення області під кривою на відрізку [a, b]
ix = np.linspace(a, b, 400)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Область інтегрування')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
ax.legend()
plt.grid()
plt.show()
