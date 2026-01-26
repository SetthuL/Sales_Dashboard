import os
import matplotlib.pyplot as plt
from data import products, prices, daily_sales

def save_charts():
    if not os.path.exists('charts'):
        os.makedirs('charts')

'''
def calculate_daily_sales():
    products = []
    daily_sales = []
'''
plt.figure()

def plot_daily_sales(products, daily_sales):
    plt.subplot(2, 2, 1)
    plt.title("Daily Sales of Electronic Products")
    plt.xlabel("Products")
    plt.ylabel("Number of Sales")
    plt.bar(products, daily_sales, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    
    plt.savefig('charts/daily_sales.png')
    
def plot_sales_charts(products, prices, daily_sales):
   rev = []
   
   for price, sales in zip(prices, daily_sales):
    rev.append(price * sales)

   plt.subplot(2, 2, 2)
   plt.title("Revenue from Electronic Products")
   plt.xlabel("Products")
   plt.ylabel("Revenue (R)")
   plt.bar(products, rev)
   plt.xticks(rotation=45, ha='right')
   plt.savefig('charts/revenue.png')

   
def sort_by_rev(item):
    return item [1]
   
def top_3_products_by_rev(products, prices, daily_sales):
    revenue = [p * s for p, s in zip(prices, daily_sales)]
    prod_rev = list(zip(products, revenue))
    
    prod_rev.sort(key=sort_by_rev, reverse=True) # Sort by revenue descending
    
    top_3 = prod_rev[:3]
    
    top_products = []
    top_revenue = []
    
    for product, rev in top_3:
        top_products.append(product)
        top_revenue.append(rev)
        
    plt.subplot(2, 2, 3)
    plt.title("Top 3 Products Revanue")
    plt.xlabel("Products")
    plt.ylabel("Revanues (R)")
    plt.bar(top_products, top_revenue, color="Green")
    
    plt.savefig('charts/top_3_revenue.png')
    
    '''
    print("Top 3 Products by Revenue:")
    for prod, rev in prod_rev[:3]:
        print(f"{prod}: R{rev:.2f}") # Display revenue with two decimal
    '''
save_charts()
plot_sales_charts(products, prices, daily_sales)
plot_daily_sales(products, daily_sales)
top_3_products_by_rev(products, prices, daily_sales)

plt.tight_layout()
plt.show()