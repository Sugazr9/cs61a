; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (rle s)
  (define (helper stream h n)
  	(if (= (car stream) h) (helper (cdr-stream stream) h (+ n 1)) (lst n stream)) 
  	)
  (cond
  	((if null? s) s) (
  		(define x (helper s (car s) 1))
  		(cons-stream (lst (car s) (car x) (rle (cdr x))))
  	))
)
