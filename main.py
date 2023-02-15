
# Выполнила Анастасия Догадина гр 108

print("******** Приложение для расчета депозита ********")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите ваш вклад: "))
print("Ваш вклад: %d" % money)

deposit = list(map(lambda v: money*v/100, per_cent.values()))
print(deposit)
print("Максимальная сумма, которую вы можете заработать —", round(max(deposit), 2))