#記帳買東西，用while loop比for loop 更好，因為不知道會買幾樣，for loop是固定去跑的
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':   #離開 quit
		break
	price = input('請輸入價格：')
	product = [] #小清單
	product.append(name)
	product.append(price)  #line8到line10可以簡寫成product = [name, price]
	products.append(product)   #更簡潔就是products.append([name, price])
	
print(products)

#現在要把清單跟價格儲存在同一個list裡，直接清單、價格、清單、價格這樣存不好，等於是每個記載的東西都交替
#所以要一個記載，裡面還有一個記載，裝產品與價格
#即為二維度(2 dimensions)
#那要怎麼做?: 在input完產品跟價格後再建立清單(prouct)

#如何列出清單裡的東西?
print(product[0][0]) 
#第一個0是表示第一個小清單
#第二個0是表示小清單內的第一個索引(index)

for p in products:
	print(p[0], '的價格是：', p[1]) #for loop是把每個引索"一個一個拿出來"
#所以打line26就會是把清單內所有東西都列出來，再包含價格