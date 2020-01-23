# Set으로 사용해서 인접리스트 만들기

a, b, c, d, e, f = range(6) # 6개 노드
N = [{b, c, d}, {a, d, f}, {a, b, d, e}, {a, e}, {a, b, c}, {b, c, d, e}]
print(b in N[a]) # Membership Test : True
print(b in N[b]) # Membership Test : False
print(len(N[f])) # Degree : 4


# List로 인접리스트 만들기
a, b, c, d, e, f = range(6) # 6개 노드
N = [[b, c, d], [a, d, f], [a, b, d, e], [a, e], [a, b, c], [b, c, d, e]]
print(b in N[a]) # Membership Test : True
print(b in N[b]) # Membership Test : False
print(len(N[f])) # Degree : 4


# Dictionary로 인접리스트 만들기1
a, b, c, d, e, f = range(6) # 6개 노드 
N = [{b:2, c:1, d:4, f:1}, {a:4, d:1, f:4}, {a:1, b:1, d:2, e:4}, {a:3, e:2}, {a:3, b:4, c:1}, {b:1, c:2, d:4, e:3}] # 각 노드를 간선 가중치 등의 값으로 연결
print(b in N[a]) # Membership Test : True
print(b in N[b]) # Membership Test : False
print(len(N[f]))


# Dictionary로 인접리스트 만들기2
a, b, c, d, e, f = range(6)
N = {'a': set('bcdf'), 'b': set('adf'), 'c': set('abde'), 'd': set('ae'), 'e': set('abc'), 'f': set('bcde')}
print('b' in N['a']) # Membership Test : True
print(len(N['f'])) # Degree :4 
