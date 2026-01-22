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

def plot_daily_sales(products, daily_sales):
    plt.title("Daily Sales of Electronic Products")
    plt.xlabel("Products")
    plt.ylabel("Number of Sales")
    plt.bar(products, daily_sales, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig('charts/daily_sales.png')
    
    plt.show()
    
def plot_sales_charts(products, prices, daily_sales):
   rev = []
   
   for price, sales in zip(prices, daily_sales):
    rev.append(price * sales)

   plt.figure()
   plt.title("Revenue from Electronic Products")
   plt.xlabel("Products")
   plt.ylabel("Revenue (R)")
   plt.bar(products, rev)
   plt.xticks(rotation=45, ha='right')
   plt.tight_layout()
   plt.savefig('charts/revenue.png')

   plt.show()

plot_sales_charts(products, prices, daily_sales)
save_charts()
plot_daily_sales(products, daily_sales)
