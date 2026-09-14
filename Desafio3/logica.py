import janus_swi as janus
janus.consult('lógica proposicional', '''
conbi(and).
conbi(or).
conbi(then).
clog(v).
clog(f).
vlog(p).
vlog(q).
vlog(r).
vlog(s).
expr(X) :- clog(X).
expr(X) :- vlog(X).
expr([neg, A]) :- expr(A).
expr([A, Con, B]) :- expr(A), conbi(Con), expr(B).
''')

# p & (q -> ¬r)
salida = list(janus.query('expr( [p, and, [q, then, [neg, r]]]).'))
print(salida)

#fibonacci(N, X)
janus.consult('fibonacci', '''
f(0,0).
f(1,1).
f(N,X) :- N > 1, N1 is N-1, f(N1,X1), N2 is N-2, f(N2,X2), X is X1 + X2.
''')
salida = list(janus.query('f(10, X).'))
print(salida)

#Torres de Hanoi
janus.consult('torres_hanoi', '''
    hanoi(1, A, _, C) :- write("Mueve del "), write(A), write(" al "), write(C), nl.
    hanoi(N, A, B, C) :- N > 1, M is N-1, hanoi(M, A, C, B), hanoi(1, A, B, C), hanoi(M, B, A, C).
''')
salida = list(janus.query('hanoi(3, a, b, c).'))          

 #a,c,b 1 a _ b | c, a, b | 
 #a al c
 #a al b
 #c al b
 