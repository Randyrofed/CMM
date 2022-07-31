import pandas as pd
#import numpy
import matplotlib.pyplot as plt
# import numpy as np
# from numpy import cov
# import csv
# from scipy.stats import pearsonr, spearmanr

# Чтение файла
df = pd.read_excel('DATA/180 (в купол обрушения).xlsx', sheet_name=None, usecols="D:F", skiprows=5, nrows=24,
                   header=None,
                   names=['CMM concentration', 'Mixture consumption, m3 / min', 'CH4 consumption, m3 / min'])

cdf = pd.concat(df, axis=0, join="inner", ignore_index=True, keys=None, levels=None, names=None, verify_integrity=False,
                copy=True)

cdf.to_csv('DATA_EXPORT/cdf.csv', index=False)

cdf.head(26)
print(cdf)
cdf.plot(figsize=(18, 5))



