from collections import Counter
import statistics
import math
import matplotlib.pyplot as plt
data = [ 2.31, 0.94, 1.55, 1.1, 1.68, -0.16, 0.48,
1.49, 1.2, 1.48, 0.85, 3.21, 1.71, 4.0,
2.1, 0.26, 1.97, 1.09, 2.72, 1.18, 0.28,
0.3, 1.4, 0.59, 1.99, 2.14, 1.59, 1.5,
0.48, 2.12, 1.15, 2.54, 0.7, 1.63, 1.47,
1.71, 1.41, 0.95, 1.55, 1.28, 0.44, -1.72,
0.19, 2.73, 0.45, 0.49, 1.23, 2.44, -1.62,
0.0, 1.33, -0.51, 1.62, 0.06, 2.2, 1.87,
0.66, 0.26, 2.36, 2.4, 1.0, 2.3, 1.74,
-1.27, 3.11, 1.03, 0.59, 1.37, 1.3, 0.78,
1.01, 0.99, 0.24, 2.18, 2.24, 0.22, 1.0,
-0.54, 0.24, 2.66, 1.14, 1.06, 1.09, 1.63,
1.7, 1.35, 1.0, 1.21, 1.75, 3.27, 1.62,
2.58, 0.6, 0.19, 1.43, 2.21, 0.49, 0.46,
0.56, 1.17, 2.28, 2.02, 1.71, 1.08, 2.0,
0.38, 1.12, 0.01, 1.82, 1.96, 0.77, 1.7,
0.77, 2.79, 0.31, 1.11, 1.69, 1.23, 2.05,
2.29, 0.17, -0.12, 2.69, 1.78, 2.26, 0.0,
1.55, 0.44, 0.89, 1.51, -0.67, 1.06, -0.05,
0.27, 0.78, 0.6, 1.06, 2.29, 1.13, 1.85,
1.62, 1.5, 0.21, 2.04, 1.26, 1.98, 1.5,
0.94, 0.17, 1.9, 1.64, 1.12, 0.89, 0.4]
def Calulate_mean():
mean = 0.0
sum_data = 0.0
data_size = len(data)
print(data_size)
i=0
while i < data_size:
sum_data += data[i]
i+=1
print(sum_data)
mean = sum_data/data_size
print("Mean is %lf"%(mean))
def Calulate_median():
n = len(data)
data.sort()
if n % 2 == 0:
median1 = data[n // 2]
median2 = data[n // 2 - 1]
median = (median1 + median2) / 2
else:
median = data[n // 2]
print("Median is: " + str(median))
def Calulate_mode():
n = len(data)
data_1 = Counter(data)
get_mode = dict(data_1)
mode = [k for k, v in get_mode.items() if v == max(list(data_1.values()))]
if len(mode) == n:
get_mode = "No mode found"
else:
get_mode = "Mode is / are: " + ', '.join(map(str, mode))
print(get_mode)
def Plot_graph():
maximum_value = max(data)
minimum_value = min(data)
length_data = len(data)
Interval_Number = math.ceil((1 + math.log2(length_data)))
intervalWidth = (maximum_value - minimum_value) / Interval_Number
print(maximum_value, ' ', minimum_value, ' ', Interval_Number)
Interval_Array = []
low_val = minimum_value
high_val = 0.0
for i in range(Interval_Number):
hi = low_val + intervalWidth
if i == (Interval_Number - 1):
high_val = maximum_value
Interval_Array.append((low_val, high_val))
low_val = high_val
print(Interval_Array)
frequency = []
for low, i in Interval_Array: # ...
frequency.append(len(list(filter(lambda x: low <= x <= i, data))))
print(frequency)
plt.hist(data, bins=10, color='#4B0082')
plt.show()
def Calculating_Skewness():
standard_deviation = statistics.stdev(data)
mean = 0.0
sum_data = 0.0
data_size = len(data)
print(data_size)
i = 0
while i < data_size:
sum_data += data[i]
i += 1
print(sum_data)
mean = sum_data / data_size
n = len(data)
data.sort()
if n % 2 == 0:
median1 = data[n // 2]
median2 = data[n // 2 - 1]
median = (median1 + median2) / 2
else:
median = data[n // 2]
skewness = 3* (mean - median)/standard_deviation
print("skewness is %lf" %(skewness))
def main():
Calulate_mean()
Calulate_median()
Calulate_mode()
Plot_graph()
Calculating_Skewness()


main()
