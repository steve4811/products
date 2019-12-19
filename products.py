products =[]

while True:
	product_name = input('請輸入你買過的商品 ：')
	if product_name == 'q':
		break
	else:
		product_price = input('請輸入商品價格 ：')
		products.append([product_name ,product_price])

print(products)
for p in products:
	print(p[0] ,'的價格是' ,p[1])
