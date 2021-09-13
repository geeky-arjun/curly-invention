# this is a pattern matching algo
def calculate_z(self, string):
    
    N = len(string)
    Z = [0]*N
    Z.append(N)
    L = R = 0
    for i in range(1,N):
        # brute force 
        if i > R:
            L = R = i
            while R < N and string[R] == string[R-L]:
                R += 1
            Z[i] = R-L
            R -= 1
        else:
            # calculate from the interval
            j = i-L
            # not touching and exceeding the boundry
            if Z[j] < R-i+1:
                Z[i] = Z[j]
            # touching or exceeding the boundry
            else:
                L = i
                while R < N and string[R] == string[R-L]:
                    R += 1
                Z[i] = R-L
                R -= 1
    
    return Z