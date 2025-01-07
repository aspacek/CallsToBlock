# CallsToBlock.py

# numpy module - math routine
import numpy as np

# csv module - read and write csv files
import csv

# pyplot module - plot out results
import matplotlib.pyplot as plt

# Input and output files

# BlockedCalls.txt - List of all blocked phone numbers
#input_file = 'BlockedCalls.txt'

# BlockedCalls_without296.txt - List of all blocked phone numbers not starting with area code 296
input_file = 'BlockedCalls_without296.txt'

# BlockedCalls_without296_last100.txt - The 100 most recent phone numbers not starting with area code 296
#input_file = 'BlockedCalls_without296_last100.txt'

# Name of output plot file
output_file = 'BlockedCalls.png'

# Read in data
with open(input_file) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	blocked_numbers = []
	for row in csv_reader:
		blocked_numbers = blocked_numbers+[row[0]]
# Change strings to integers
blocked_numbers = [int(i) for i in blocked_numbers]
# Print some details
print('')
print('You have read in '+str(len(blocked_numbers))+' values')
print('')

# Find desired bin width
# First we have possibilities from 650-000-0000 to 650-999-9999
full_range = 9999999+1
# Bin width of 100,000 means 650-[0-9][0-9]X-XXXX
bin_width = 40000
nbins = int(full_range/bin_width)
# Print some details
print('Full number range = '+str(full_range))
print('Bin width = '+str(bin_width))
print('Number of bins = '+str(nbins))
print('')

# Compute binned values
counts, bins = np.histogram(blocked_numbers,bins=nbins,range=(0,full_range))

# Print results
print('HISTOGRAM RESULTS')
print('X '+str(bins[0]))
for i in range(len(counts)):
	print(str(counts[i])+' '+str(bins[i+1]))
print('')

# Sort results high to low
endbins = bins[1:]
sorted_endbins = [arr_to_match for arr_to_sort, arr_to_match in sorted(zip(counts,endbins))]
sorted_endbins[:] = sorted_endbins[::-1]
counts.sort()
counts[:] = counts[::-1]

# Print results
print('Assuming 2,000,000 calls can be blocked')
blocked_bins = int(2000000/bin_width)
print('You can block the top'+' '+str(blocked_bins)+' bins')
blocked_counts = np.sum(counts[:blocked_bins])
print('This accounts for '+str(blocked_counts/np.sum(counts)*100)+' % of the blocked numbers')
print('')
print('SORTED RESULTS')
for i in range(len(counts)):
	print(str(counts[i])+' '+str(sorted_endbins[i]-bin_width)+' '+str(sorted_endbins[i]))
print('')

# Plot:
plt.hist(blocked_numbers,bins=nbins,range=(0,full_range))
plt.savefig(output_file)
