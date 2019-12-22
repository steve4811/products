products =[]

#讀入CSV file ,去掉抬頭 ，加入 product 清單
products = []
with open('products.csv' ,'r' ,encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		product_name ,product_price = line.strip().split(',')
		products.append([product_name ,product_price])
	print(products)

#製作二維的清單，商品/價格
while True:
	product_name = input('請輸入你買過的商品 ：')
	if product_name == 'q':
		break
	else:
		product_price = input('請輸入商品價格 ：')
		products.append([product_name ,product_price])

#印出商品的價格
print(products)
for p in products:
	print(p[0] ,'的價格是' ,p[1])

#將商品價格寫入csv檔案
with open('products.csv' ,'w' ,encoding = 'utf-8') as f:
	f.write('商品,價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] +'\n')
