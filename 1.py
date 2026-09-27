prices = [500, 1500, 800, 2000, 1200]
expensive_products=[]
def find_expensive_products(prices):
    for price in prices:
        if price > 1000:
            expensive_products.append(price)
    return expensive_products
print(find_expensive_products(prices))