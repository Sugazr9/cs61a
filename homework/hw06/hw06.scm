(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 0) 1)
    ((even? n) (square (pow b (/ n 2))))
    (else (* b (pow b (- n 1))))
    )
)

(define (ordered? s)
  (cond
    ((null? (cdr s)) True)
    ((<= (car s) (cadr s)) (ordered? (cdr s)))
    (else False)
    )
)

(define (no-repeats s)
  (define (test-repeats l v)
    (cond 
      ((null? l) l)
      ((= (car l) v) (test-repeats (cdr l) v)) 
      (else (cons (car l) (test-repeats (cdr l) v)))
  ))
  (if (null? s) s 
  (cons (car s) (no-repeats (test-repeats (cdr s) (car s)))))
  )

(define (nodots s)
  (cond
    ((null? s) s)
    ((pair? (car s)) (cons (nodots (car (car s))) (cons (nodots (cdr(car s))) (nodots (cdr s)))))
    (else (cons (car s) (nodots (cdr s))))
    )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) False)
          ((= (car s) v) True)
          ((< v (car s)) False)
          (else (contains? (cdr s) v)) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
(define (add s v)
    (cond ((empty? s) (list v))
          ((< v (car s)) (cons v s)) ; replace this line
          ((= (car s) v) s)
          (else (cons (car s) (add (cdr s) v)))
          ))
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t)))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t)))
           ; replace this line
          )))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ; replace this line
          ))

; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ((= v (label t)) True)
          ((< v (label t)) (in? (left t) v))
          ((> v (label t)) (in? (right t) v))
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.label == v:
;         return True
;     elif s.label < v:
;         return contains(s.right, v)
;     elif s.label > v:
;         return contains(s.left, v)
(define (as-list t)
    (cond
      ((null? t) nil) 
      ((and (null? (left t)) (null? (right t))) (cons (label t) nil))
      ((null? (left t)) (cons (label t) (as-list (right t))))
      ((null? (right t)) (cons (as-list (left t)) (label t)))
      (else (cons (car (as-list (left t))) (cons (label t) (as-list (right t)))))
    ))

