.. -*- mode: rst -*-

|PyPi|_ |License|_ |Python3|_

.. |PyPi| image:: https://badge.fury.io/py/tab-data.svg
.. _PyPi: https://badge.fury.io/py/tab-data
.. |License| image:: https://img.shields.io/pypi/l/tab-data.svg
.. _License: https://img.shields.io/pypi/l/tab-data.svg
.. |Python3| image:: https://img.shields.io/badge/python-3-green.svg
.. _Python3: https://www.python.org/download/releases/3.0/


Tab-Data
========

Tab-data is a Python module for tabular data preprocessing based on Pandas and sklearn.

This project was created by `Ben Dai <http://www.bendai.org>`_. If there is any problem and suggestion please contact me via <bdai@umn.edu>.

Installation
------------

Dependencies
~~~~~~~~~~~~

Tab-Data requires:

- Python
- Numpy
- Pandas
- sklearn
- SciPy

User installation
~~~~~~~~~~~~~~~~~

Install Deep-Inference using ``pip`` ::

	pip install tab-data

or ::

	pip install git+https://github.com/statmlben/tab-data.git

Source code
~~~~~~~~~~~

You can check the latest sources with the command::

    git clone https://github.com/statmlben/tab-data.git

Documentation
-------------

tab_le
~~~~~~

Function for label encoding for tabular data. 

.. code:: python

	def tab_le(*args, cate_feature)

- Example

.. code:: python

	import pandas as pd
	from tab-data import tab_le

	data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
	df = pd.DataFrame(data)
	## convert one dataframe
	df = tab_le(df, cate_feature = ['Name', 'Age'])
	## convert many dataframes
	df1, df2 = tab_le(df, df, cate_feature = ['Name', 'Age'])

- Parameters:
	
	- **one or many DataFrames**: target DataFrames | ``type=dataframes``

	- **cate_feature:** list of categorical columns | ``type=list``

- Return:
	
	- **one or many DataFrames**: return encoded labels for each categorical columns | ``type=dataframes``

tab_stat
~~~~~~~~

Return basic description for a tabular data. 

.. code:: python

	def tab_stat(df)

- Example

.. code:: python

	import pandas as pd
	from tab-data import tab_stat

	data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
	df = pd.DataFrame(data)
	## convert one dataframe
	df = tab_stat(df)

- Parameters:
	
	- **DataFrame**: target DataFrame | ``type=dataframe``

- Return:
	
	- **DataFrame**: basic description for a tabular data | ``type=dataframe``
