# Data Ingestion, manipulation & workflow

---
In this README you will find information about this project, information about the code and choices in the project. 

- You can find the code in [main.py](main.py).
- You can find the theoretical in [theory](theory.md).


---

# Laboration
By working with Pandas I have followed the flow of reading a csv-file with data such as id, name, price and so on.
Some information in the file is missing or is inconsistent. For the data to be ready for analysis it has to be
cleaned, flagged and rejected to know which data us usable.


## Read the file
The first step is to read the file and get the data, this by using the 'read_csv()' function. 
The csv-file uses ';' as its delimiter instead of a comma. To be able to work with the data we set the delimiter in the read_csv function.
```python
products_df = pd.read_csv("lab 1 - csv.csv", sep = ";")
```
---
## Clean the data
For an analysis to be as accurate as possible the data needs to be cleaned. If not, the data could show  wrong results.
In this case some cleaning is not necessary for this data, but if a new file was provided it can contain other inconsistencies.

When working with a larger amount of data you will need to clean the data even more. More data == more inconsistencies.

---

## Conditions
Conditions is a great way checking the data to see what data is missing information or might be off in its value.
One example in the code is when looking at the price. Data is flagged when the price is over 10 000 or equal to zero, 
at the same time as prices below zero or a missing price is to be rejected.

When having a database it is easier to check flagged data. In this case there is data tha have all the information 
except for the column 'name'. With a database one can check the id and see what product is connected to it.
The data is usable to do calculations due to the other information.

In the analyses the price is necessary for the calculations. I have chosen to do two different analyses, one including flagged data and one with only valid data.
Flaggd data contains a price and currency but might miss other information. 
---

## Status message
A clear way to see information about the data is a status message or reason. It can be if something is missing like price or currency.
It can also show a flagging that a price is really high in contrast to the other products. 

Example of reject message:
```python
products_df.loc[products_df["price"].isna(), "status"] = "MISSING PRICE"
products_df.loc[products_df["price"] < 0, "status"] = "NEGATIVE PRICE"
```
---

## Separera data
When separating the data further in to the code, the reject and flagged conditions makes it easy.


```python
df_rejected = products_df[reject_conditions].copy()
```
This code shows how the data that fulfills the conditions in 'reject_conditions' is copied into 'df_rejected'. 
It is possible to use the DataFrame to create a new csv-file with the rejected data.
To get the data that is valid we use '~reject_conditions', this gives us th opposite data. 

When analyzing you some only want correct data and some want to include the flagged data. Flagged data can be correct, 
you won't know until it has been checked.
Due to not having that possibility in this exercise, I have done different analyses as mentioned above.
---
## Analysis

### Analytics Summary
In the first analytic file we are to show mean/average, median, amount of products and products without price.
By creating a DataFrame with these columns and putting in calculation of the request (mean, median...)
you will then get the result in its own dataframe.
```python
    df_summary = pd.DataFrame({
        "Mean Price": [df_valid["price"].mean()],
        "Median Price": [df_valid["price"].median()],
        "Product Amount": [len(df_valid)],
        "Products Without Price": [len(df_valid[df_valid["price"] == 0])]
    })
```

When using the flagged and not flagged data the average price of the two has a difference of 23 549 SEK.
This shows the importance of checking the data before using it, depending on what you are looking for. 
If the flagged data shows to not be correct, the average price will seem much higher than it actually is.


### Price Analysis
The second analysis is to show the ten most expensive products and the top ten most deviating prices. 
I started with creating new columns, "Most Expensive" and "Most Deviating". Instead of just putting 'Top 10' on each
row that was included in the top ten I chose to do a for loop with enumerate. I did get some tips from LLM on where to 
put 'enumerate' but most of the code in this pice is not from LLM: 

```python
for i, n in enumerate(df_valid.nlargest(10, "price").index, start=1):
        df_valid.loc[n, "Most Expensive"] = f"ME {i}"
```
By using the for loop each row gets a number. Highest price gets 'ME 1' (Most Expensive).

I used the same loop for the most deviating price, there the tex would read MD (Most Deviating). The calculation is using
the median of the prices to compare to. 

When comparing the valid data and the flagged data, the major difference is that we get a low price in the top ten
deviating prices due to not having as many high prices.
---
### Skapa csv-filer
When the analyses are done they are written into a csv-file. For analytics summary, price analysis and the rejected data.
You can find them under [data](data)