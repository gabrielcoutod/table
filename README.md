# Table
Table class for printing tables in python.

# Examples
Example code:
```python
from table import Table
    
headers = ['header 1', 'header 2','header 3']
data = [['data 1.1 ','data 2.1  ','data 3.1   '], 
    ['data 1.1','data 2.2','data 3.2'], 
    ['data 1.3','data 2.3','data 3.3']]
```
```python
print("Normal table:\n")
print(Table.get_table(headers, data))
'''
Expected Output:
Normal table:

header 1  header 2   header 3
--------- ---------- -----------
data 1.1  data 2.1   data 3.1
data 1.1  data 2.2   data 3.2
data 1.3  data 2.3   data 3.3
'''
```
```python
print("fixed_space=True:\n")
print(Table.get_table(headers, data, fixed_space=True))
'''
Expected Output:
fixed_space=True:

header 1    header 2    header 3
----------- ----------- -----------
data 1.1    data 2.1    data 3.1
data 1.1    data 2.2    data 3.2
data 1.3    data 2.3    data 3.3
'''
```
```python
print("separator_headers_data='~':\n")
print(Table.get_table(headers, data, separator_headers_data='~'))
'''
Expected Output:
separator_headers_data='~':

header 1  header 2   header 3
~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~~
data 1.1  data 2.1   data 3.1
data 1.1  data 2.2   data 3.2
data 1.3  data 2.3   data 3.3
'''
```
```python
print("separator_for_data='~':\n")
print(Table.get_table(headers, data, separator_for_data='~'))
'''
Expected Output:
separator_for_data='~':

header 1  header 2   header 3
--------- ---------- -----------
data 1.1  data 2.1   data 3.1
~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~~
data 1.1  data 2.2   data 3.2
~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~~
data 1.3  data 2.3   data 3.3
'''
```
```python
print("separator_between_cols='|':\n")
print(Table.get_table(headers, data, separator_between_cols='|'))
'''
Expected Output:
separator_between_cols='|':

header 1 |header 2  |header 3
---------|----------|-----------
data 1.1 |data 2.1  |data 3.1
data 1.1 |data 2.2  |data 3.2
data 1.3 |data 2.3  |data 3.3
'''
```
```python
print("separator_around_lines='-':\n")
print(Table.get_table(headers, data, separator_around_lines='-'))
'''
Expected Output:
separator_around_lines='-':

--------- ---------- -----------
header 1  header 2   header 3
--------- ---------- -----------
data 1.1  data 2.1   data 3.1
data 1.1  data 2.2   data 3.2
data 1.3  data 2.3   data 3.3
--------- ---------- -----------
'''
```
```python
print("separator_around_cols='|':\n")
print(Table.get_table(headers, data, separator_around_cols='|'))
'''
Expected Output:
separator_around_cols='|':

|header 1  header 2   header 3   |
|--------- ---------- -----------|
|data 1.1  data 2.1   data 3.1   |
|data 1.1  data 2.2   data 3.2   |
|data 1.3  data 2.3   data 3.3   |
'''
```
