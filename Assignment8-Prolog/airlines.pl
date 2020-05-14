flight(london, air_canada, toronto, 500, 360).
flight(london, united, toronto, 650, 420).
flight(london, iberia, barcelona, 220, 240).
flight(barcelona, air_canada, madrid, 100, 60).
flight(barcelona, iberia, madrid, 120, 65).
flight(barcelona, iberia, valencia, 110, 75).
flight(valencia, iberia, madrid, 40, 50).
flight(madrid, air_canada, toronto, 900, 480).
flight(madrid, united, toronto, 950, 540).
flight(madrid, iberia, toronto, 800, 480).
flight(madrid, iberia, malaga, 50, 60).
flight(valencia, iberia, malaga, 50, 30).
flight(paris, united, toulouse, 35, 120). 

airport(london, 75, 80).
airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).


/*1.) To check if flight exists from city X to city Y*/

isflight(X, Y) :- (flight(X, A, Y, B, C) ; flight(Y, A, X, B, C)) -> write('There is a flight') ; write('There is no flight').


/*2.) If journey from A to B with flight C is below 400$, it is cheap*/

ischeap(A, B, C) :- airport(A, X, S) , airport(B, V, T), (flight(A, C, B, L, M) ; flight(B, C, A, L, M)), X + L + V < 400 -> write('Flight is cheap. ') ; write('Flight is not cheap. ').


/*3.) If you can go from A to B in two flights*/

istwopossible(A, B) :- ((flight(A, V, W, X, Y) ; flight(W, V, A, X, Y)), (flight(W, L, B, M, N)) ; flight(B, L, W, M, N)) -> write('Two flights are possible') ;  write('Two flights are not possible').


/*4.) Checks if flight from A to B is cheap or C is air_canada*/

ispreferable(A, B, C) :- ((airport(A, X, S) , airport(B, V, T), (flight(A, C, B, L, M) ; flight(B, C, A, L, M)), X + L + V < 400) ; C == air_canada) -> write('The flight is preferred') ; write('Flight is not preferred').


/*5.) Checks if there is United from A to B then there is Air Canada from B to A*/

ifunithencan(A, B) :- (flight(A, united, B, C, D) ; flight(B, united, A, C, D)) , (flight(A, air_canada, B, E, F) ; flight(B, air_canada, A, E, F)) -> write('True') ; write('false').
