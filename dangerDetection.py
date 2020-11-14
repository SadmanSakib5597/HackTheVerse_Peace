from math import sqrt
from math import exp
from math import pi
from csv import reader
 
def load_csv_file(filename):
	dataset = list()
	with open(filename, 'r') as file:
		C_reader = reader(file)
		for row in C_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
 

def separatedata_by_classvalue(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated
 

def calculate_mean_stdev(dataset):
	summaries=[]
	for val in zip(*dataset):
		mean=sum(val)/float(len(val))
		avg = mean
		variance = sum([(x-avg)**2 for x in val]) / float(len(val)-1)
		stdv= sqrt(variance)
		lngth=len(val)
		summaries.append([mean,stdv,lngth])
	
	print(summaries)
	del(summaries[-1])
	return summaries
 

def summarize_by_classvalue(dataset):
	separatedClass = separatedata_by_classvalue(dataset)
	summaries = dict()
	for class_value, rows in separatedClass.items():
		summaries[class_value] = calculate_mean_stdev(rows)
	return summaries
 

def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent
 

def calculate_class_probability(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			print("rara ", row[i])
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities
 

def prediction(summaries, row):
	probabilities = calculate_class_probability(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label
 

filename = 'filenew1.csv'
dataset = load_csv_file(filename)
print("len ", len(dataset[0])-1)
for i in range(len(dataset[0])-1):
	for row in dataset:
		row[i] = float(row[i].strip())

class_values = [row[len(dataset[0])-1] for row in dataset]
unique = set(class_values)
lookup = dict()
for i, value in enumerate(unique):
	lookup[value] = i
	print('[%s] => %d' % (value, i))
for row in dataset:
	row[len(dataset[0])-1] = lookup[row[len(dataset[0])-1]]

model = summarize_by_classvalue(dataset)

row=[100.9,116,96,96,145]

# row=[99.6,76,75,54,139]

# row=[100.7,77,63,105,177]


# row=[11,103.7,75,64,93]
label = prediction(model, row)
print('Data=%s, Predicted: %s' % (row, label))
