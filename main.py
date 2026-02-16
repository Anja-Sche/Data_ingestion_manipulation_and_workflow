import pandas as pd

# Read the csv file and set delimiter -> ;
products_df = pd.read_csv("lab 1 - csv.csv", sep = ";")


# Clean data in 'name'
products_df["name"] = (products_df["name"]
                       .str.strip()
                       .str.title())

# Turn 'price' into numeric -> non-numeric values into NaN
products_df["price"] = pd.to_numeric(products_df["price"], errors="coerce")

# Clean data in currency
products_df["currency"] = products_df["currency"].str.strip()

# Clean data in 'created_at', turn into datetime -> non datetime values into 'NaT'
products_df["created_at"] = products_df["created_at"].str.replace("/", "-")
products_df["created_at"] = pd.to_datetime(products_df["created_at"], errors="coerce",format = "%Y-%m-%d")


print(products_df)