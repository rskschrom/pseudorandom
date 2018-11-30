import numpy as np
from netCDF4 import Dataset
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as st

# normalize function
def norm(data):
    data_norm = (data-np.mean(data))/np.std(data)
    return data_norm

# get frequency histogram
def freq_hist(minb, maxb, nbin, data):
    bins = np.linspace(minb, maxb, nbin+1)
    freq = np.empty([nbin])

    for i in range(nbin):
        bin_data = data[(data>bins[i])&(data<=bins[i+1])]
        freq[i] = len(bin_data)/float(ndata)

    return bins, freq

# open file
data = np.genfromtxt('test_stats.txt')
ndata = len(data)

'''uniform data
# bin data
nbin = 100
minb = 0.
maxb = 1.
bins, freq = freq_hist(minb, maxb, nbin,  data)
f_ideal = np.full([nbin], 1./nbin)
'''

# bin data (normal)
nbin = 200
minb = -4.5
maxb = 4.5
bins, freq = freq_hist(minb, maxb, nbin,  data)

# get idealized values
f_ideal = np.empty([nbin])
for i in range(nbin):
    f_ideal[i] = st.norm.cdf(bins[i+1])-st.norm.cdf(bins[i])

# perform chi2 test
chi2, p = st.chisquare(freq, f_ideal)
print p, chi2

# change fonts
mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
mpl.rc('text', usetex=True)

# plot
plt.plot(bins[1:], freq, 'k-', label='data')
plt.plot(bins[1:], f_ideal, 'r-', label='normal CDF')
ax = plt.gca()
ax.set_xlim([minb, maxb])
ax.set_ylim([0., 0.04])
ax.set_xlabel('Bin')
ax.set_ylabel('Relative frequency')
ax.grid()

plt.text(2., 0.025, '$\chi^2$ = {:.4f}\np = {:.3f}'.format(chi2, p))
plt.legend()
plt.savefig('freq_test.png')
