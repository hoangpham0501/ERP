import numpy as np
import math
def pearson(R, P, Q):
	for i in range(len(R[0])):
		for j in range(i+1,len(R[0])):
			result = s1 = s2 = 0
			for k in range(len(R)):
				if R[k][i]*R[k][j] == 0:
					continue
				result = result + (R[k][i]-Q[i])*(R[k][j]- Q[j])
				s1 = s1 + pow(R[k][i]-Q[i], 2)
				s2 = s2 + pow(R[k][j]- Q[j], 2)
			P[i][j] = result/(np.sqrt(s1*s2))
			P[j][i] = P[i][j]

	for i in range(len(P)):
		for j in range(len(P[0])):
			if math.isnan(P[i][j]):
				P[i][j] = 0

	return P

def average(R,Q): 
	for i in range(len(R[0])):
		s = count = 0 
		for j in range(len(R)): 
			if R[j][i] != 0:
				s = s + R[j][i]
				count = count + 1
		Q[i] = s/count
	return Q

def recommendation(R,P,Q,T): 
	for i in range(len(R)):
		for j in range(len(R[0])):
			if R[i][j] == 0:
				sim = sim_abs = 0
				for k in range(len(P)):
					if k != j:
						if T[i][k] != 0:
							sim = sim + P[j][k]*(T[i][k] - Q[k])
							sim_abs = sim_abs + abs(P[j][k])
					if sim_abs == 0:
						continue
					R[i][j] = Q[j] + sim/sim_abs
	return R


if __name__ == '__main__':
	R = [
		 [1.0,4.0,5.0,0.0,3.0],
		 [5.0,1.0,0.0,5.0,2.0],
		 [4.0,1.0,2.0,5.0,0.0],
		 [0.0,3.0,4.0,0.0,4.0],
		]

	R = np.array(R)
	T = np.array(R)		#copy matrix R
	N = len(R[0])

	# init sim matrix P
	P = np.zeros((N,N))	 
	for i in range(len(P)):
		for j in range(len(P)):
			if i == j:
				P[i][j] = 1.0

	# init average matrix
	Q = np.zeros((N))	
	Q = average(R, Q)

	# Pearson matrix
	P = pearson(R,P,Q)		
	print(P)

	# Result
	R = recommendation(R,P,Q,T)
	print(R)