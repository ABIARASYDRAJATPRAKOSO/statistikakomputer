import numpy as np
apel = [100,200,150,100,120,80,90,160,110,170]
med_apel=np.median(apel)
apel.sort()
apel_urut=' '.join(map(str,apel))
print('Apel Urut : {:s}'.format(apel_urut))
print (med_apel)