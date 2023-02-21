from scipy import stats
import statistics as s

nilai = [70,80,70,70,90,100]

mode_nilai=stats.mode(nilai)
modus=s.mode(nilai)
print(modus)
print(mode_nilai)
print(mode_nilai.mode)