#find the majority element in a list
#uses python3
def majority_element(a):
	maj_el, count = None, 0
	for i in a:
		if count == 0:
			maj_el, count = i, 1
		elif a[i] == maj_el:
			count += 1
		else:
			count -= 1
	return maj_el, count