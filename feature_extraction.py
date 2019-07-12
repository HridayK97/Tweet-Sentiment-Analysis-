#lists=[0,0,3,0]


def num_of_positives(lists):
	p_count=0
	for i in lists:
		if i>0:
			p_count=p_count+1
	
	return p_count

def num_of_negatives(lists):
	n_count=0
	for i in lists:
		if i<0:
			n_count=n_count+1
	
	return n_count

def pratio(lists):
	n_count=0.0
	p_count=0.0		
	for i in lists:
		if i<0.0:
			n_count=n_count+1
	
	for i in lists:
		if i>0.0:
			p_count=p_count+1

	if n_count!=0:
		pton=(p_count/n_count)
		#print pton
		return pton
	else:
		return -999

def nratio(lists):
	n_count=0.0
	p_count=0.0		
	for i in lists:
		if i<0.0:
			n_count=n_count+1
		elif i>0.0:
			p_count=p_count+1
	if p_count!=0:
		ntop=(n_count/p_count)
		#print nton
		return ntop
	else:
		return -999

def sentiment_score(lists):	
	total=sum(lists)
	count=len(lists)
	if count==0:
		value=0
	else:
		value=(total/float(count))
	return value
