
# Vennam

Vennam is a Python library for converting Python DataFrame to List of Python Dictionary items .

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Vennam.

```bash
pip install vennam
```

## version

```bash
vennam.__version__ # return current version of Package
```

## Usage of Package

```python
from vennam import DataFrameToDict as dd

list_dict=dd.dftodict(DataFrame) # returns the list of dictionary items

```
## Word Analysis on DataFrame Data

```python

from vennam import Analysis 

freqency=Analysis.WordAnalysis(< DataFrame >,< DataFrame Column >)

```

## Example


```python
from vennam import Analysis 

freqency=Analysis.WordAnalysis(data,'description')


```

## Word Cloud on DataFrame Data


```python

from vennam import Analysis 

WordClound=Analysis.WordCloud(< DataFrame >,< DataFrame Column >)

```


## Example


```python

from vennam import Analysis 

WordClound=Analysis.WordCloud(data,'description')

```

## DataBase Connection 

```python

from vennam.DataBase import create_engine

connection=create_engine(user,password,host,port,database)


```

## Example 

```python

from vennam.DataBase import create_engine

connection=create_engine(user="VVVVV",
        password="VVVVV",
        host="VVVVV",
        port="VVVVV",
        database="VVVVV")
		
```


## Dumping DataFrame into existing database table 

```python

from vennam.DataBase import insert_dict

Data_dump=insert_dict(connection,schemaname,tablename,dataframe)

```

## Example 

```python 

from vennam.DataBase import insert_dict

Data_dump=insert_dict(schemaname="VVVVV",tablename="VVVVV",connection=connection,dataframe=dataframe) 

```

## License
[MIT](https://choosealicense.com/licenses/mit/)