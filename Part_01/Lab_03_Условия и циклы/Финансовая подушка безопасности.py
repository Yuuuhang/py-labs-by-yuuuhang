money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
while money_capital + salary >= spend:
    money_capital += salary - spend
    months += 1
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
