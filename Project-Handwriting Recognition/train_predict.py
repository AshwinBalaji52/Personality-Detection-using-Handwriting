import os
import itertools
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # 34.79
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier  # 34.3858431645,9.63451306963
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
import extract
import categorize

X_baseline_angle = []
X_top_margin = []
X_letter_size = []
X_line_spacing = []
X_word_spacing = []
X_pen_pressure = []
X_slant_angle = []
y_t1 = []
y_t2 = []
y_t3 = []
y_t4 = []
y_t5 = []
page_ids = []

if os.path.isfile("label_list"):
	print ("Info: label_list found.")
	#=================================================================
	with open("label_list", "r") as labels:
		for line in labels:
			content = line.split()
			
			baseline_angle = float(content[0])
			X_baseline_angle.append(baseline_angle)
			
			top_margin = float(content[1])
			X_top_margin.append(top_margin)
			
			letter_size = float(content[2])
			X_letter_size.append(letter_size)
			
			line_spacing = float(content[3])
			X_line_spacing.append(line_spacing)
			
			word_spacing = float(content[4])
			X_word_spacing.append(word_spacing)
			
			pen_pressure = float(content[5])
			X_pen_pressure.append(pen_pressure)
			
			slant_angle = float(content[6])
			X_slant_angle.append(slant_angle)
			
			trait_1 = float(content[7])
			y_t1.append(trait_1)
			
			trait_2 = float(content[8])
			y_t2.append(trait_2)
			
			trait_3 = float(content[9])
			y_t3.append(trait_3)
			
			trait_4 = float(content[10])
			y_t4.append(trait_4)

			trait_5 = float(content[11])
			y_t5.append(trait_5)

			
			page_id = content[12]
			page_ids.append(page_id)
	#===============================================================
	
	# neuroticism
	X_t1 = []
	for a, b in itertools.izip(X_baseline_angle, X_slant_angle):
		X_t1.append([a, b])
	
	
		
	# agreeableness
	X_t2 = []
	for a, b in itertools.izip(X_letter_size, X_top_margin):
		X_t2.append([a, b])
		
	# openness
	X_t3 = []
	for a, b in itertools.izip(X_line_spacing, X_word_spacing):
		X_t3.append([a, b])
		
	# conscientiousness
	X_t4 = []
	for a, b in itertools.izip(X_slant_angle, X_top_margin):
		X_t4.append([a, b])
		
	
	# extraversion
	X_t5 = []
	for a, b in itertools.izip(X_line_spacing, X_word_spacing):
		X_t5.append([a, b])
	
	#print X_t1
	#print type(X_t1)
	#print len(X_t1)
	
	X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t1, test_size = .30, random_state=5)
	clf1 = SVC(kernel='rbf' )
	clf1.fit(X_train, y_train)
	print "Classifier 1 accuracy: ",accuracy_score(clf1.predict(X_test), y_test)
	
	X_train, X_test, y_train, y_test = train_test_split(X_t2, y_t2, test_size = .30, random_state=5)
	clf2 = SVC(kernel='rbf' )
	clf2.fit(X_train, y_train)
	print "Classifier 2 accuracy: ",accuracy_score(clf2.predict(X_test), y_test)
	
	X_train, X_test, y_train, y_test = train_test_split(X_t3, y_t3, test_size = .30, random_state=5)
	clf3 = SVC(kernel='rbf')
	clf3.fit(X_train, y_train)
	print "Classifier 3 accuracy: ",accuracy_score(clf3.predict(X_test), y_test)
	
	X_train, X_test, y_train, y_test = train_test_split(X_t4, y_t4, test_size = .30, random_state=5)
	clf4 = SVC(kernel='rbf')
	clf4.fit(X_train, y_train)
	print "Classifier 4 accuracy: ",accuracy_score(clf4.predict(X_test), y_test)
	
	X_train, X_test, y_train, y_test = train_test_split(X_t5, y_t5, test_size = .30, random_state=5)
	clf5 =  SVC(kernel='rbf')
	clf5.fit(X_train, y_train)
	print "Classifier 5 accuracy: ",accuracy_score(clf5.predict(X_test), y_test)
	# ================================================================================================

	print "Accuracy of Classifiers from KNN"

	from sklearn.model_selection import train_test_split

	X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t1, test_size=0.30)

	from sklearn.neighbors import KNeighborsClassifier

	clf6 = KNeighborsClassifier(n_neighbors=5)
	clf6.fit(X_train, y_train)
	print "Classifier 1 KNN accuracy: ", accuracy_score(clf6.predict(X_test), y_test)

	from sklearn.model_selection import train_test_split

	X_train, X_test, y_train, y_test = train_test_split(X_t2, y_t2, test_size=0.30)

	from sklearn.neighbors import KNeighborsClassifier

	clf7 = KNeighborsClassifier(n_neighbors=5)
	clf7.fit(X_train, y_train)
	print "Classifier 2 KNN accuracy: ", accuracy_score(clf7.predict(X_test), y_test)

	from sklearn.model_selection import train_test_split

	X_train, X_test, y_train, y_test = train_test_split(X_t3, y_t3, test_size=0.30)

	from sklearn.neighbors import KNeighborsClassifier

	clf8 = KNeighborsClassifier(n_neighbors=5)
	clf8.fit(X_train, y_train)
	print "Classifier 3 KNN accuracy: ", accuracy_score(clf8.predict(X_test), y_test)

	from sklearn.model_selection import train_test_split

	X_train, X_test, y_train, y_test = train_test_split(X_t4, y_t4, test_size=0.30)

	from sklearn.neighbors import KNeighborsClassifier

	clf9 = KNeighborsClassifier(n_neighbors=5)
	clf9.fit(X_train, y_train)
	print "Classifier 4 KNN accuracy: ", accuracy_score(clf9.predict(X_test), y_test)

	from sklearn.model_selection import train_test_split

	X_train, X_test, y_train, y_test = train_test_split(X_t5, y_t5, test_size=0.30)

	from sklearn.neighbors import KNeighborsClassifier

	clf10 = KNeighborsClassifier(n_neighbors=5)
	clf10.fit(X_train, y_train)
	print "Classifier 5 KNN accuracy: ", accuracy_score(clf10.predict(X_test), y_test)


	# =================================================================================================

	print "Accuracy of classifiers from Random Forest"

	X_train, X_test, y_train, y_test = train_test_split(X_t1, y_t1, test_size=0.30)
	clf11 = RandomForestClassifier(criterion="gini", n_estimators=10)
	clf11.fit(X_train, y_train)
	print "Classifier 1 RF accuracy: ", accuracy_score(clf11.predict(X_test), y_test)

	X_train, X_test, y_train, y_test = train_test_split(X_t2, y_t2, test_size=0.30)
	clf12 = RandomForestClassifier(criterion="gini", n_estimators=10)
	clf12.fit(X_train, y_train)
	print "Classifier 2 RF accuracy: ", accuracy_score(clf12.predict(X_test), y_test)

	X_train, X_test, y_train, y_test = train_test_split(X_t3, y_t3, test_size=0.30)
	clf13 = RandomForestClassifier(criterion="gini", n_estimators=10)
	clf13.fit(X_train, y_train)
	print "Classifier 3 RF accuracy: ", accuracy_score(clf13.predict(X_test), y_test)

	X_train, X_test, y_train, y_test = train_test_split(X_t4, y_t4, test_size=0.30)
	clf14 = RandomForestClassifier(criterion="gini", n_estimators=10)
	clf14.fit(X_train, y_train)
	print "Classifier 4 RF accuracy: ", accuracy_score(clf14.predict(X_test), y_test)

	X_train, X_test, y_train, y_test = train_test_split(X_t5, y_t5, test_size=0.30)
	clf15 = RandomForestClassifier(criterion="gini", n_estimators=10)
	clf15.fit(X_train, y_train)
	print "Classifier 5 RF accuracy: ", accuracy_score(clf15.predict(X_test), y_test)


	#================================================================================================
	
	while True:
		file_name = raw_input("Enter file name to predict or z to exit: ")
		if file_name == 'z':
			break
			
		raw_features = extract.start(file_name)
		
		raw_baseline_angle = raw_features[0]
		baseline_angle, comment = categorize.determine_baseline_angle(raw_baseline_angle)
		print "Baseline Angle: "+comment
		
		raw_top_margin = raw_features[1]
		top_margin, comment = categorize.determine_top_margin(raw_top_margin)
		print "Top Margin: "+comment
		
		raw_letter_size = raw_features[2]
		letter_size, comment = categorize.determine_letter_size(raw_letter_size)
		print "Letter Size: "+comment
		
		raw_line_spacing = raw_features[3]
		line_spacing, comment = categorize.determine_line_spacing(raw_line_spacing)
		print "Line Spacing: "+comment
		
		raw_word_spacing = raw_features[4]
		word_spacing, comment = categorize.determine_word_spacing(raw_word_spacing)
		print "Word Spacing: "+comment
		
		raw_pen_pressure = raw_features[5]
		pen_pressure, comment = categorize.determine_pen_pressure(raw_pen_pressure)
		print "Pen Pressure: "+comment
		
		raw_slant_angle = raw_features[6]
		slant_angle, comment = categorize.determine_slant_angle(raw_slant_angle)
		print "Slant: "+comment
		
		print
		print "Neuroticism ", clf1.predict([[baseline_angle, slant_angle]])
		print "Agreeableness: ", clf2.predict([[letter_size, top_margin]])
		print "Openness: ", clf3.predict([[line_spacing, word_spacing]])
		print "Conscientiousness: ", clf4.predict([[slant_angle, top_margin]])
		print "Extraversion: ", clf5.predict([[line_spacing, word_spacing]])
		print "---------------------------------------------------"
		print
		
	#=================================================================================================
		
else:
	print ("Error: label_list file not found.")