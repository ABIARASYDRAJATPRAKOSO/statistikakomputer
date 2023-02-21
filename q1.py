import numpy as np
import pandas as pd

data_baru = np.array([23,56,45,65,59,55,62,54,85,25,55])
print(pd.DataFrame(data_baru).describe())