data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有 %d 筆資料' % len(data))
sum = 0
for leng in data:
	sum += len(leng)
average = sum / len(data)
print('留言的平均長度為: %5.2f' % average)

new = []
for leng in data:
	if len(leng) < 100:
		new += leng
print('留言小於100筆的一共為: %d ' % len(new))