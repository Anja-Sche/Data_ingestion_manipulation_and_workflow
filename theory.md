# Theory:

# Ingest —> Storage —> Transform —> Access

## Ingest 
Collecting data from various sources. To compare with the project the ingestion is when reading the information from the 
csv-file. We gather the data to be able to use it.

## Storage 
The raw data is stored in a centralized location like a repository och data lake for example. 
In the project you could see it as storing the data temporarily in your computer, but is lost when the script is done.

## Transform 
The data gets cleaned, structured and refined. In the project we use cleaning to get accurate data, making sure the structure 
is the same. In the code there is also type conversion of the price. This to make the data analysis ready. 

## Acces
Here the data is made available for the users. It can e.g. be shown on a dashboard to visualize it. In the project 
we make the data ready for analysis when sorting out the transformed data into df_valid, but it is not accessible. When we 
write the data into csv-files we make it accessible for others to use and acquire.

<div style="margin-bottom: 3em;"></div>

# Technologies
## Psycopc3

Psycopc3 is a database adapter, and you can use it to create a database session using 'connect()'. 
You connect to a Postgresql database server through Python. Psycopg3 connection pools manages a set of connections
that you cann borrow. In case one connection is occupied, it will redirect you to another one so that you don't
have to wait as long. Psycopg3 also protects towards SQL injections which makes it more safe.

## Pandas
Pandas is a library for data manipulation and analysis i Python. It provides many functions for cleaning, sorting,
filtering and more. It uses easy syntax and can handle alot of data at the same time as it can read from
and write data into different formats. 

## Pydantic
Pydantic is a data validation library, it helps us to create and handle complex data structures. It is powered by typ hints,
what type the return value should be. It is a fast validation library. A Pydantic model is a class that inherits from 
BaseModel, it lets you define the schema or structure of the data and makes sure that the structure will be followed when receiving 
and sending data.

<div style="margin-bottom: 3em;"></div>

# ETL
This process helps to get high quality data, handel large amounts of data and makes it easy to maintain .

## Extract
Extracting data means gathering or collecting raw data, often from different sources. The data can be collected from e.g.
databases, APIs, file and is gathered.

## Transform
When transforming you want to clean, filter, aggregate and format the data. Beware of business rules to ensure the quality
and consistency and to make it usable. This usually happens in a staging area before the data is moved. That makes it important 
that the data is ready and done transforming before moving on.

## Load
The last step, loading data, is when moving data from the staging area into a database, data lake or data warehouse.
It can then be used for analytics and reporting.
