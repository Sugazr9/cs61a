(define (deep-map fn s)
  (cond
  	((null? s) s)
  	((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
  	(else (cons (fn (car s)) (deep-map fn (cdr s))))
	)
  )
