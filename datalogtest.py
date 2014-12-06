from pyDatalog import pyDatalog

pyDatalog.load("ancestor(X,Y) <= parent(X,Y)")
pyDatalog.load("ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)")
pyDatalog.assert_fact('parent', 'bill', 'John Adams')
# pyDatalog.load("""
# 	ancestor(X, Y) <= parent(X, Y)
# 	ancestor(X, Y) <= parent(X, Z) & ancestor(Z, Y)
# """)
print(pyDatalog.ask('parent(bill, X)'))
