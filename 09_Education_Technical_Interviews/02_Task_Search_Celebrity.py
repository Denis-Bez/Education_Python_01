
# Task analysis: https://www.youtube.com/watch?v=xGvQN_g-JCI

# We have 'k' people. We can ask every human, "would do you know that human?" and had get answer - 'not' or 'yes'.
# Need to find a celebrity, which doesn't know enyone, but enyone knows him

"""
l                   k-1  (people index)
\O/  \O/    \O/     \O/
 |    |      |       |
/ \  / \    / \     / \ 
1----------->------->
<-----2----->
             3 is celebrity
             <-------4

"""

def search_celebrity(person):
    k = len(person)
    # person1.knows(person2) - method return True if 'person1' knows 'person2' and False if 'person1' doesn't know 'person2'

    l = 0
    r = k-1

    while not l==r:
        if people(l).knows(people(r)):
            l+= 1
        else:
            r-= 1

    for i in range(0, k-1):
        if (not i==l) and ( (people(l).knows(people(i))) or (not people(i).knows(people(l)) ) ):
            return False
        else:
            return person[l]

    # O = k + 2k = O(k)
