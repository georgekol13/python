import requests
from datetime import date, timedelta

def get_winning_numbers(date: str):
    url = f'https://api.opap.gr/draws/v3.0/1100/draw-date/{date}/{date}' # petaei error an valoume pano apo mia mera diafora, opote pairnoume ena ena ta apotelesmata gia kathe mera
    
    data = requests.get(url).json()
    winning_numbers = data['content'][0]['winningNumbers']['list'] # vazoume to 0 epeidi theloume tin proti klirosi mono
    return winning_numbers

def get_dates_for_one_month(delta=-1):
	today = date.today()
	m, y = (today.month+delta) % 12, today.year + ((today.month)+delta-1) // 12
	if not m: m = 12
	d = min(today.day, [31,
		29 if y%4==0 and (not y%100==0 or y%400 == 0) else 28,
		31,30,31,30,31,31,30,31,30,31][m-1])
	dates = []
	delta = today - today.replace(day=d,month=m, year=y) 
	for i in range(delta.days + 1):
		day = today - timedelta(days=i)
		dates.append(str(day))
	return dates


countOccurrences = [0] * 80

dates = get_dates_for_one_month()

for day in dates:
	draw = get_winning_numbers(str(day))
	for number in draw:
		countOccurrences[number-1] += 1

for index,number in enumerate(countOccurrences):
	print(f'In {len(dates)} days, number {index+1} appeared at the first draw {number} times.')

# PIGES
# https://stackoverflow.com/questions/65583482/extract-specific-keys-from-multiple-jsons-by-multiple-urls-through-apis
# https://stackoverflow.com/questions/3424899/whats-the-simplest-way-to-subtract-a-month-from-a-date-in-python
