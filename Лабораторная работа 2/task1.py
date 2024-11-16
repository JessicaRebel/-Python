money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0  # Число месяцев без долгов

while True:
    money_capital += salary - spend
    if money_capital >= 0:
        month += 1
        spend *= 1 + increase
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)
