
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

## License
[MIT](https://choosealicense.com/licenses/mit/)
