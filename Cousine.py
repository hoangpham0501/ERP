import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosine(R, P):
	for i in range(len(R[0])):
		for j in range(i+1,len(R[0])):
			result = s1 = s2 = 0
			for k in range(len(R)):
				result = result + R[k][i]*R[k][j]
				s1 = s1 + pow(R[k][i], 2)
				s2 = s2 + pow(R[k][j], 2)
			P[i][j] = result/(np.sqrt(s1)*np.sqrt(s2))
			P[j][i] = P[i][j]

	return P

def CosineSimilarityMatrix(user_item_matrix):
	similarity_matrix = cosine_similarity(user_item_matrix.T)
	return similarity_matrix

def recommendation(R,P,Q): 
	for i in range(len(R)):
		for j in range(len(R[0])):
			if R[i][j] == 0:
				sim = sim_abs = 0
				for k in range(len(P)):
					if k != j:
						if Q[i][k] != 0:
							sim = sim + P[j][k]*Q[i][k]
							sim_abs = sim_abs + abs(P[j][k])
				R[i][j] = sim/sim_abs
	return R

					 

if __name__ == '__main__':
	R = [
		 [1.0,4.0,5.0,0.0,3.0],
		 [5.0,1.0,0.0,5.0,2.0],
		 [4.0,1.0,2.0,5.0,0.0],
		 [0.0,3.0,4.0,0.0,4.0],
		]

	R = np.array(R)
	Q = np.array(R)
	N = len(R[0])
	P = np.zeros((N,N))
	for i in range(len(P)):
		for j in range(len(P[0])):
			if i == j:
				P[i][j] = 1.0
	P = CosineSimilarityMatrix(R)
	# P = cosine(R,P)
	print(P)
	R = recommendation(R,P,Q)	
	print(R)