(TeX-add-style-hook "_region_"
 (lambda ()
    (LaTeX-add-bibliographies
     "mybib.bib")
    (TeX-run-style-hooks
     "latex2e"
     "art12"
     "article"
     "12pt"
     "packages"
     "style")))

