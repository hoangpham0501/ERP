import numpy as np
###############################################################################
"""
@INPUT:
    R     : a matrix to be factorized, dimension N x M
    P     : an initial matrix of dimension N x K
    Q     : an initial matrix of dimension M x K
    K     : the number of latent features
    steps : the maximum number of steps to perform the optimisation
    alpha : the learning rate
    beta  : the regularization parameter
@OUTPUT:
    the final matrices P, Q and R
"""
def matrix_factorization(R, P, Q, K,muy, b_u, b_i, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - prediction(R, P, Q, i, j, muy, b_u, b_i)
                    for k in range(K):
                        #update biases
                        b_u[i] = alpha * (eij - beta*b_u[i])
                        b_i[j] = alpha * (eij - beta*b_i[j])
                         #Update user and item latent feature matrices
                        P[i][k] = P[i][k] + alpha * (2*eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2*eij * P[i][k] - beta * Q[k][j])
        eR = np.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - (np.dot(P[i,:],Q[:,j] + muy + b_u[i] + b_i[j])), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if e < 0.001:
            break
    return P, Q.T, muy, b_u, b_i

def averageMatrix(R):
    return np.mean(R[np.where(R != 0)])

def prediction(R, P, Q, i, j, muy, b_u, b_i):
    return muy + b_u[i] + b_i[j] + np.dot(P[i, :], Q[:,j])


###############################################################################

if __name__ == "__main__":
    R = [
         [5,3,0,1],
         [4,0,0,1],
         [1,1,0,5],
         [1,0,0,4],
         [0,1,5,4],
        ]

    R = np.array(R)

    N, M = R.shape 
    K = 2

    muy = averageMatrix(R)
    b_u = np.zeros(N)
    b_i = np.zeros(M)

    P = np.random.rand(N,K)
    Q = np.random.rand(M,K)

    nP, nQ, muy, b_u, b_i = matrix_factorization(R, P, Q, K, muy,b_u,b_i)
    nR = np.dot(nP, nQ.T) + muy + b_u[:,np.newaxis] + b_i[np.newaxis,:]
    print(nR)


