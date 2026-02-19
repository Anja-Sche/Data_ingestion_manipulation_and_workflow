import pandas as pd

if __name__ == '__main__':

    # Read the csv file and set delimiter -> ;
    products_df = pd.read_csv("lab 1 - csv.csv", sep = ";")

    """ 
    Clean the data
    """
    # Clean data in 'name'
    products_df["name"] = (products_df["name"]
                            .str.strip()
                            .str.title()
                            .str.replace(r"\s+", " ", regex=True)
    )

    # Turn 'price' into numeric -> non-numeric values into NaN
    products_df["price"] = (products_df["price"]
                            .str.replace("free", "0")
                            .str.strip()
                            )
    products_df["price"] =pd.to_numeric(products_df["price"], errors="coerce")

    # Clean data in currency
    products_df["currency"] = (products_df["currency"]
                               .str.strip()
                               .str.upper()
                               )

    # Clean data in 'created_at', turn into datetime -> non datetime values into 'NaT'
    products_df["created_at"] = products_df["created_at"].str.replace("/", "-")


    """ 
    Create conditions for flagging and rejecting data
    """


    # Create: Conditions for flagging data
    flagged_conditions = (
            ((products_df["name"].isna()) & (products_df["price"] >= 0)) |
            (products_df["created_at"].isna()) |
            (products_df["price"] > 10000) |
            (products_df["price"] == 0)
    )

    # Create: Conditions for rejecting data
    reject_conditions = (
            ((products_df["id"].isna()) & (products_df["price"].isna())) |
            (products_df["price"].isna()) |
            (products_df["currency"].isna() |
            (products_df["price"] < 0))
    )


    """ 
    Create status messages
    """

    # Status message
    products_df["status"] = ""

    products_df.loc[products_df["id"] != "NaN", "status"] = "VALID"


    # Reject reasons
    products_df.loc[~products_df["id"].str.contains("^SKU-"), "status"] = "Wrong ID"
    products_df.loc[products_df["id"].isna(), "status"] = "MISSING ID"
    products_df.loc[products_df["price"].isna(), "status"] = "MISSING PRICE"
    products_df.loc[products_df["price"] < 0, "status"] = "NEGATIVE PRICE"
    products_df.loc[products_df["currency"].isna(), "status"] = "MISSING CURRENCY"

    # Flagg reasons
    products_df.loc[products_df["name"].isna(), "status"] = "MISSING NAME"
    products_df.loc[products_df["price"] > 10000, "status"] = "HIGH PRICE"
    products_df.loc[products_df["created_at"].isna(), "status"] = "MISSING CREATED_AT"
    products_df.loc[products_df["price"] == 0, "status"] = "NO COST"


    """ 
    Separating the data
    """

    df_rejected = products_df[reject_conditions].copy()
    df_flagged = products_df[flagged_conditions].copy()
    df_valid = products_df[~reject_conditions & ~flagged_conditions].copy()

    # For calculations with flagged data, show the difference with high/no price products
    df_valid_fl = products_df[~reject_conditions].copy()


    """ 
    Create file for analytic summary:
        - analytics with only valid data
        - analytics with valid data AND flagged data for comparison 
    """

    #Create:
    df_summary = pd.DataFrame({
        "Mean Price": [df_valid["price"].mean().round(3)],
        "Median Price": [df_valid["price"].median()],
        "Product Amount": [len(df_valid)],
        "Products Without Price": [len(df_valid[df_valid["price"] == 0])]
    })

    df_summary.to_csv("data/analytic_summary.csv", index=False)


    # Show the difference in analytics with high/no price products
    df_summary_fl = pd.DataFrame({
        "Mean Price": [df_valid_fl["price"].mean().round(3)],
        "Median Price": [df_valid_fl["price"].median()],
        "Product Amount": [len(df_valid_fl)],
        "Without Price Not Counted": [len(df_flagged)]
    })

    df_summary_fl.to_csv("data/analytic_summary_fl.csv", index=False)

    """ 
    Create file for price analysis:
        - analysis with only valid data
        - analysis with valid data AND flagged data for comparison 
    """

    # Create column for most expensive products
    df_valid["Most Expensive"] = ""
    df_valid.loc[df_valid["currency"] == "SEK", "Most Expensive"] = "N"

    # Calculate the most expensive products
    # For loop and enumerate to give each a nr, highest == 1 ...
    for i, n in enumerate(df_valid.nlargest(10, "price").index, start=1):
        df_valid.loc[n, "Most Expensive"] = f"ME {i}"

    # Create column for most deviated products comparing to median
    df_valid["Most Deviating"] = ""
    median = df_valid["price"].median()

    df_valid["difference from median"] = (df_valid["price"] - median).abs()
    df_valid.loc[df_valid["currency"] == "SEK", "Most Deviating"] = "N"

    # For loop and enumerate to give a nr, furthest from median == 1 ...
    for i, n in enumerate(
            df_valid.sort_values(by=["difference from median", "price"], ascending=[False, True]).head(10).index,
            start=1):
        df_valid.loc[n, "Most Deviating"] = f"MD {i}"

    # Put the result in csv-file
    df_valid.to_csv("data/price_analysis.csv", index=False)



    # Same code including flagged products
    df_valid_fl["Most Expensive"] = ""
    df_valid_fl.loc[df_valid_fl["currency"] == "SEK", "Most Expensive"] = "N"
    for i, n in enumerate(df_valid_fl.nlargest(10, "price").index, start=1):
        df_valid_fl.loc[n, "Most Expensive"] = f"ME {i}"

    # Create column for most deviated products comparing to median
    df_valid_fl["Most Deviating"] = ""
    median = df_valid_fl["price"].median()

    df_valid_fl["difference from median"] = (df_valid_fl["price"] - median).abs()
    df_valid_fl.loc[df_valid_fl["currency"] == "SEK", "Most Deviating"] = "N"

    for i, n in enumerate(
            df_valid_fl.sort_values(by=["difference from median", "price"], ascending=[False, True]).head(10).index,
            start=1):
        df_valid_fl.loc[n, "Most Deviating"] = f"MD {i}"

    df_valid_fl.to_csv("data/price_analysis_fl.csv", index=False)


    """ 
    Create file for rejected data 
    """

    # Create: csv-file for rejected data
    df_rejected.to_csv("data/rejected_products.csv", index=False)