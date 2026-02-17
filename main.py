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


    # Create: Conditions for flagging data
    flagged_conditions = (
            (products_df["price"] > 10000) |
            (products_df["price"] == 0)
    )

    # Create: Conditions for rejecting data
    reject_conditions = (
            (products_df["id"].isna()) |
            (products_df["name"].isna()) |
            (products_df["price"].isna()) |
            (products_df["price"] < 0) |
            (products_df["currency"].isna()) |
            (products_df["created_at"].isna())
    )

    # Reason for flagg
    products_df["reason"] = ""

    products_df.loc[products_df["price"] > 10000, "reason"] = "HIGH PRICE"
    products_df.loc[products_df["price"] == 0, "reason"] = "NO COST"


    # Separate the data
    df_rejected = products_df[reject_conditions].copy()
    df_flagged = products_df[flagged_conditions].copy()
    df_valid = products_df[~reject_conditions & ~flagged_conditions].copy()

    # For calculations with flagged data, show the difference with high/no price products
    df_valid_with_flaggs = products_df[~reject_conditions].copy()



    #print(df_valid)

    #Create:
    df_summary = pd.DataFrame({
        "Mean Price": [df_valid["price"].mean()],
        "Median Price": [df_valid["price"].median()],
        "Product Amount": [len(df_valid)],
        "Products Without Price": [len(df_valid[df_valid["price"] == 0])]
    })

    df_summary.to_csv("data/analytic_summary.csv", index=False)


    # Show the difference in analytics with high/no price products
    df_summary_with_flaggs = pd.DataFrame({
        "Mean Price": [df_valid_with_flaggs["price"].mean()],
        "Median Price": [df_valid_with_flaggs["price"].median()],
        "Product Amount": [len(df_valid_with_flaggs)],
        "Without Price Not Counted": [len(df_flagged)]
    })

    df_summary_with_flaggs.to_csv("data/analytic_summary_with_flaggs.csv", index=False)





    # Reason for rejection
    df_rejected["reason"] = ""

    df_rejected.loc[products_df["id"].isna(), "reason"] = "MISSING ID"
    df_rejected.loc[products_df["name"].isna(), "reason"] = "MISSING NAME"
    df_rejected.loc[products_df["price"].isna(), "reason"] = "MISSING PRICE"
    df_rejected.loc[products_df["price"] < 0, "reason"] = "NEGATIVE PRICE"
    df_rejected.loc[products_df["currency"].isna(), "reason"] = "MISSING CURRENCY"
    df_rejected.loc[products_df["created_at"].isna(), "reason"] = "MISSING CREATED_AT"


    #print(df_rejected)

    # Create: csv-file for rejected data
    df_rejected.to_csv("data/rejected_products.csv", index=False)
