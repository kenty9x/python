def solution(S):
    if S.count('a') <3 or S.count('b') < 3:
        return -1
    
    for a, b in ['ab', 'ba']:
        if S.find(a*3) != -1: # In case of that we have 'aaa' or 'bbb'
            pos = [i for i in range(len(S)) if S[i] == b] # List all position of 'a' or 'b'
            ans = len(S)
            for i in range(len(pos)-2):
                ans = min(ans, pos[i+2] - pos[i] - 2) # Find min of distance between 2 same chars
            return ans
    
    d = dict()
    q = []
    for i in range(len(S)):
        w = S[i:i+8] # Get 9-char substring and add to queue, index with dict
        if w not in d:
            d[w] = 0
            q.append(w)

    while q:
        w = q[0]
        q = q[1:]

        # Return value when we have substring 'aaa' and 'bbb' in queue items
        if w.find('aaa') != -1 and w.find('bbb') != -1: 
            return d[w]
        
        for i in range(len(w)-1):
            w2 = w[:i] + w[i+1] + w[i] + w[i+2:]
            if w2 not in d:
                d[w2] = d[w] +1
                q.append(w2)
