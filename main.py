import os
import matplotlib.pyplot as plt
from data import products, daily_sales

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
    
plot_daily_sales(products, daily_sales)
