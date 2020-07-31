import numpy as np
import pandas as pd
from sklearn import preprocessing

raw_data = {'patient': [1, 1, 1, 2, 2],
			'obs': [1, 2, 3, 1, 2],
			'treatment': [0, 1, 0, 1, 0],
			'score': ['strong', 'weak', 'normal', 'weak', 'strong']}
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])

	
