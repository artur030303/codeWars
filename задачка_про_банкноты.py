BANKNOTES =[1,2,5,10,20,50,100,200,500,1000]
MAX_AMOUNT = 10
amount = int(input('Введите сумму: '))
result = dict.fromkeys(BANKNOTES, 0)
used_banknotes = []
for i in range(len(BANKNOTES)+1):
    cutted_banknotes = BANKNOTES[:i]
    if sum(cutted_banknotes) * MAX_AMOUNT >= amount:
        used_banknotes = cutted_banknotes
        break   
while amount:
    amount -= used_banknotes[-1]
    result[used_banknotes[-1]] += 1
    if amount <= sum(used_banknotes[:-1]) * MAX_AMOUNT:
        used_banknotes = used_banknotes[:-1]
print(result)  



BANKNOTES = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Начинаем с крупных банкнот
MAX_AMOUNT = 10

amount = int(input("Введите сумму: "))
result = dict.fromkeys(BANKNOTES, 0)

for banknote in BANKNOTES:
    if amount == 0:
        break
    count = min(amount // banknote, MAX_AMOUNT)  # Берём максимум банкнот, но не больше MAX_AMOUNT
    result[banknote] = count
    amount -= count * banknote

print(result)