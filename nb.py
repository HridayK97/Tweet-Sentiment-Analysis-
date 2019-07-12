import numpy as np
from sklearn import metrics
file=open("myfile.csv","r")
b=[]
c=[]
i=0
for x in file:
	(a)=x.split(",")
	b.append(a)
	i+=1
	if b[i-1][-1] == "happiness\n":
		c.append(0)
		b[i-1].pop()
	elif b[i-1][-1] == "love\n":
		c.append(1)
		b[i-1].pop()
	elif b[i-1][-1] == "fun\n":
		c.append(2)
		b[i-1].pop()
	elif b[i-1][-1] == "enthusiasm\n":
		c.append(3)
		b[i-1].pop()
	elif b[i-1][-1] == "surprise\n":
		c.append(4)
		b[i-1].pop()
	elif b[i-1][-1] == "neutral\n":
		c.append(5)
		b[i-1].pop()
	elif b[i-1][-1] == "empty\n":
		c.append(6)
		b[i-1].pop()
	elif b[i-1][-1] == "worry\n":
		c.append(7)
		b[i-1].pop()
	elif b[i-1][-1] == "sadness\n":
		c.append(8)
		b[i-1].pop()
	elif b[i-1][-1] == "hate\n":
		c.append(9)
		b[i-1].pop()
	elif b[i-1][-1] == "boredom\n":
		c.append(10)
		b[i-1].pop()
	elif b[i-1][-1] == "relief\n":
		c.append(11)
		b[i-1].pop()
	elif b[i-1][-1] == "anger\n":
		c.append(12)
		b[i-1].pop()
	else: 
		c.append(13)
		print b[i-1].pop()
print len(c)


tprl=[]
fprl=[]
rc=[]
for k in range(10):
	train=[]
	for i in range(1,29999):
		if i%10 != 0:
			a=[]
			for j in range(2400):
				a.append(float(b[i][j]))
			train.append(a)

	test=[]
	for i in range(1,29999):
		if i%10 == 0:
			a=[]
			for j in range(2400):
				a.append(float(b[i][j]))
			test.append(a)

	train_class=[]
	for i in range(1,29999):
		if i%10 != 0:
			train_class.append(c[i])

	test_class=[]
	for i in range(1,29999):
		if i%10 == 0:
			test_class.append(c[i])
	print test_class
	X = np.array(train)
	y = np.array(train_class)

	from sklearn.naive_bayes import GaussianNB
	clf = GaussianNB()
	clf.fit(X, y) 
	ans=list(clf.predict(test))
	print ans
	acc=0.0
	for i in range(2999):
		if ans[i]==test_class[i]:
			acc+=1
	acc=acc*100/2999
	print "Accuracy = "+str(acc)+"%"

	cm=[[0 for j in range(13)] for i in range(13)]
	for i in range(2999):
		cm[test_class[i]][ans[i]]+=1

	tp=[0 for i in range(13)]
	for i in range(13):
		tp[i]+=cm[i][i]

	fp=[0 for i in range(13)]
	for i in range(13):
		for j in range(13):
			if i!=j:
				fp[j]+=cm[i][j]

	tn=[0 for i in range(13)]
	for i in range(13):
		for j in range(13):
			if i!=j:
				fp[i]+=cm[i][j]

	fn=[0 for i in range(13)]
	for k in range(13):
		for i in range(13):
			for j in range(13):
				if i!=k and j!=k:
					fp[k]+=cm[i][j]

	print tp,fp,tn,fn

	# def precision(y_true, y_pred):
	#     i = set(y_true).intersection(y_pred)
	#     len1 = len(y_pred)
	#     if len1 == 0:
	#         return 0
	#     else:
	#         return len(i) / len1


	# def recall(y_true, y_pred):
	#     i = set(y_true).intersection(y_pred)
	#     return len(i) / len(y_true)


	# def f1(y_true, y_pred):
	#     p = precision(y_true, y_pred)
	#     r = recall(y_true, y_pred)
	#     if p + r == 0:
	#         return 0
	#     else:
	#         return 2 * (p * r) / (p + r)

	# tpr=recall(test_class,ans)

	# fpr=precision(test_class,ans)

	tpr=0.0
	fpr=0.0

	for i in range(13):
		if fn[i]+tp[i]>0:
			tpr+=1.0*tp[i]/((fn[i]+tp[i])*13)
		if fp[i]+tn[i]>0:
			fpr+=1.0*fp[i]/((fp[i]+tn[i])*13)

	print "True positive rate : "+str(tpr)
	print "False positive rate : "+str(fpr)
	print ""

	tprl.append(tpr)
	fprl.append(fpr)

	fpr,tpr,thr=metrics.roc_curve(test_class,ans)
	pos_label=2
	x=metrics.auc(fpr,tpr)
	rc.append(x)

print tprl
print fprl
print rc

tprl.sort()
fprl.sort()


from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
# Compute fpr, tpr, thresholds and roc auc
# fpr, tpr, thresholds = roc_curve(test_class, y_score)
# roc_auc = auc(test_class, ans)

# Plot ROC curve
plt.plot(fprl, tprl, label='ROC curve (area = %0.3f)' % x)
plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate or (1 - Specifity)')
plt.ylabel('True Positive Rate or (Sensitivity)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
