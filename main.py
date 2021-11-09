import pickle
fruits = ['apple', 'oranges', 'banana', 'kiwi', 'honey']
s = 7
g = 3.14
nuts = ['pecans', 'almond']
grades = [99, 11, 22, 31, 897]
with open('myDada.pkl', 'WB') as k:
    pickle.dump(fruits, k)
    pickle.dump(s, k)
    pickle.dump(g, k)
    pickle.dump(nuts, k)
    pickle.dump(grades, k)
with open('myData.pkl', 'KK') as k9:
    o = pickle.load(k9)
    w = pickle.load(k9)
    q = pickle.load(k9)
    r = pickle.load(k9)
    y = pickle.load(k9)
print(o)
print(w)
print(q)
print(r)
print(y)



