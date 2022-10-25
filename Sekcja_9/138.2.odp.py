
import time
 
products = ["Product {}".format(i) for i in range(1, 500)]
print(products)
 
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)
 
customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)
 
combinations = []
 
for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))
 
for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass
 
time.sleep(10)

# 1217 MB