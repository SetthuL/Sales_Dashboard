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

def value_labels(values, is_currency=False):
    for i, v in enumerate(values):
        label = f"R{v/1000:.0f}k" if is_currency else str(v)
        plt.text(i, v * 1.02, str(v), ha="center", va="bottom", fontsize=8)
        
plt.figure(figsize=(12, 8))

plt.suptitle("Electronic Products Sales Analysis for the year - 2025", fontsize=16, weight="bold")

def plot_daily_sales(products, daily_sales):
    plt.subplot(2, 2, 1)
    plt.title("Daily Sales of Electronic Products")
    plt.xlabel("Products")
    plt.ylabel("Number of Sales")
    plt.bar(products, daily_sales, color='skyblue')
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.ylim(0, max(daily_sales) * 1.35)
    value_labels(daily_sales)
    plt.xticks(rotation=45, ha='right')
 
def plot_sales_charts(products, prices, daily_sales):
   rev = []
   
   for price, sales in zip(prices, daily_sales):
    rev.append(price * sales)

   plt.subplot(2, 2, 2)
   plt.title("Revenue from Electronic Products")
   plt.xlabel("Products")
   plt.ylabel("Revenue (R)")
   plt.bar(products, rev , color="orange", width=0.5)
   plt.grid(axis="y", linestyle="--", alpha=0.4)
   plt.ylim(0, max(rev) * 1.35)
   value_labels(rev, is_currency=True)
   plt.xticks(rotation=45, ha='right')

   
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
    plt.title("Top 3 Products Revenue")
    plt.xlabel("Products")
    plt.ylabel("Revenues (R)")
    plt.bar(top_products, top_revenue, color="Green")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    value_labels(top_revenue)
    plt.ylim(0, max(top_revenue) * 1.35)
    plt.xticks(rotation=45, ha='right')
    
    '''
    print("Top 3 Products by Revenue:")
    for prod, rev in prod_rev[:3]:
        print(f"{prod}: R{rev:.2f}") # Display revenue with two decimal
    '''
save_charts()
plot_sales_charts(products, prices, daily_sales)
plot_daily_sales(products, daily_sales)
top_3_products_by_rev(products, prices, daily_sales)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('charts/electronic_products_sales_analysis_2025.png')
plt.show()