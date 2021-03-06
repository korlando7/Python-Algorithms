# Uses python3

def max_pairwise_fast():
	n = int(input())
	a = [int(x) for x in input().split()]
	assert(len(a) == n)

	max_index1 = -1
	for i in range(0, n):
		if max_index1 == -1 or a[i] > a[max_index1]:
			max_index1 = i;

	max_index2 = -1
	for j in range(0, n):
		if j != max_index1 and (max_index2 == -1 or a[j] > a[max_index2]):
			max_index2 = j;

	return a[max_index1] * a[max_index2]
	

print(max_pairwise_fast())


	



