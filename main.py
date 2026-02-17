import pandas as pd

if __name__ == '__main__':

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
    products_df["created_at"] = pd.to_datetime(products_df["created_at"],
                                               errors="coerce",
                                               format = "%Y-%m-%d")


    #print(products_df)


    # Flagga:

    # Höga priser

    # Låga priser


    # Avvisa:

    # Minusbelopp



    # Visar endast ut True värden/flaggar
    missing_id = products_df[products_df["id"].isna()]
    missing_name = products_df[products_df["name"].isna()]
    missing_price = products_df[products_df["price"].isna()]
    missing_currency = products_df[products_df["currency"].isna()]
    missing_created_at = products_df[products_df["created_at"].isna()]

    ########################
    ######## Reject ########
    ########################

    # Lägger till data som ska avvisas i ny csv-fil
    missing_id.to_csv("rejected_products.csv", index = False)
    missing_name.to_csv("rejected_products.csv", mode="a", index = False)
    missing_price.to_csv("rejected_products.csv", mode="a", index = False)
    missing_currency.to_csv("rejected_products.csv", mode="a", index = False)
    missing_created_at.to_csv("rejected_products.csv", mode="a", index = False)

    # Läser rejected_products.csv, tar bort dubbletter och skriver över i filen
    remove_duplicates = pd.read_csv("rejected_products.csv")
    remove_duplicates.drop_duplicates(inplace = True)

    # mode='w' == overwrite the file
    remove_duplicates.to_csv("rejected_products.csv", mode="w", index = False)


