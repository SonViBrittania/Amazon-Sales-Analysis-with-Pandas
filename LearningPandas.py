import pandas as pd
import matplotlib.pyplot as plt


amazon_sales = pd.read_csv("/Users/arhaann/Documents/code/Python/Amazon Sales.csv")

amazon_sales["discounted_price"] = amazon_sales["discounted_price"].str.replace("₹", "", regex=False)
amazon_sales["discounted_price"] = amazon_sales["discounted_price"].str.replace(",", "", regex=False)
amazon_sales["discounted_price"] = pd.to_numeric(amazon_sales["discounted_price"], errors="coerce") * 0.011

amazon_sales["discount_percentage"] = amazon_sales["discount_percentage"].str.replace("%", "", regex=False)
amazon_sales["discount_percentage"] = pd.to_numeric(amazon_sales["discount_percentage"], errors="coerce") * 0.07
amazon_sales["actual_price"] = amazon_sales["actual_price"].str.replace("₹", "", regex=False)
amazon_sales["actual_price"] = amazon_sales["actual_price"].str.replace(",", "", regex=False)

amazon_sales["actual_price"] = pd.to_numeric(amazon_sales["actual_price"], errors="coerce") * 0.011
amazon_sales["rating"] = pd.to_numeric(amazon_sales["rating"], errors="coerce")


small_df = amazon_sales[["discount_percentage", "rating"]]
small_df = small_df[small_df["discount_percentage"] >= 5]
small_df = small_df[small_df["rating"] >= 4.5]

small_df = small_df.reset_index(drop=True)
small_df.index = range(1, len(small_df)+1)

small_df.plot(kind="line", marker="x")
plt.title = ("Discount Percentage vs Rating")
plt.xlabel = ("Discount Percentage")
plt.ylabel = ("Rating")
plt.show()

small_df = small_df.reset_index(drop=True)
small_df.index = range(1, len(small_df)+1)

small_df = small_df.reset_index(drop=True)
small_df.index = range(1, len(small_df)+1)

#This shows the correlation between rating an discount percentage
print(small_df["discount_percentage"].corr(small_df["rating"]))

