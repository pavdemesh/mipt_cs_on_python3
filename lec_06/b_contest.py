try:
    start_amount, percent, dream_amount = map(int, input().split())
except:
    print(0)
    exit()

start_amount_kopeks = start_amount * 100
dream_amount_kopeks = dream_amount * 100
percent_float = percent / 100

number_years = 0

while start_amount_kopeks < dream_amount_kopeks:
    annual_increase = int(start_amount_kopeks * percent_float)
    start_amount_kopeks += annual_increase
    number_years += 1

print(number_years)
