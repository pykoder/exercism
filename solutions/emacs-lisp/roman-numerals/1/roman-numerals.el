;;; roman-numerals.el --- roman-numerals Exercise (exercism)  -*- lexical-binding: t; -*-

;;; Commentary:

(defun to-roman (value)
  (cond 
   ((< value 1) "")
   ((<= value 3) (concat "I" (to-roman (- value 1))))
   ((<= value 4) (concat "IV" (to-roman (- value 4))))
   ((< value 9) (concat "V" (to-roman (- value 5))))
   ((< value 10) (concat "IX" (to-roman (- value 9))))
   ((< value 40) (concat "X" (to-roman (- value 10))))
   ((< value 50) (concat "XL" (to-roman (- value 40))))
   ((< value 90) (concat "L" (to-roman (- value 50))))
   ((< value 100) (concat "XC" (to-roman (- value 90))))
   ((< value 390) (concat "C" (to-roman (- value 100))))
   ((< value 500) (concat "CD" (to-roman (- value 400))))
   ((< value 900) (concat "D" (to-roman (- value 500))))
   ((< value 1000) (concat "CM" (to-roman (- value 900))))
   ((< value 4000) (concat "M" (to-roman (- value 1000))))
   (t "ttt"))
)

(provide 'roman-numerals)
;;; roman-numerals.el ends here
