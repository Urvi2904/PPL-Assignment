(print "Enter a number to find its factorial: ")
(setq x (read))
(setq y 0)


	(do ((f 1 (* f i))
	   (i x (- i 1)))
	   ((= i 0)(- x x))
	   (setq y f)
	)

(if(= x 0)
		(print 1)

		(print y)
)
