'''
K cores: A vertex with degree >= K 
we need to find vertices withd degree K
after we have removed vertices with 
degree <= K.

s1. we find vertices of degree < K
s2. delete vertices with degree < K
s3. s2 creates mroe vertices with 
degree < K 
s4. delete vertices with degree < K

possible that at end no vertices are left
'''
