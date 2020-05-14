(princ "Enter a number to find its factorial: ")
(setq x (read))

(defun factorial(x)
	(if(= x 0)
		 1
		 (* x (factorial(- x 1)))
	 )
)

(setq y (factorial x))
(print y)
