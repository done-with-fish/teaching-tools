## -*- encoding: utf-8 -*-
## This file (1.4.sagetex.sage) was *autogenerated* from 1.4.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('1.4', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = 16
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='[', right=']')
except:
 _st_.goboom(18)
_st_.blockend()
_st_.current_tex_line = 24
_st_.blockbegin()
try:
   A = matrix.diagonal([3,-1,1/2,0])
   B = matrix.diagonal([3,1])
except:
 _st_.goboom(27)
_st_.blockend()
try:
 _st_.current_tex_line = 33
 _st_.inline(0, latex(A))
except:
 _st_.goboom(33)
try:
 _st_.current_tex_line = 33
 _st_.inline(1, latex(B))
except:
 _st_.goboom(33)
try:
 _st_.current_tex_line = 33
 _st_.inline(0, latex(A))
except:
 _st_.goboom(33)
try:
 _st_.current_tex_line = 33
 _st_.inline(1, latex(B))
except:
 _st_.goboom(33)
_st_.current_tex_line = 70
_st_.blockbegin()
try:
   A = matrix([[1,4,2],[0,0,4],[0,0,1]])
   B = matrix([[0,0,0],[2,8,0],[4,9,7]])
except:
 _st_.goboom(73)
_st_.blockend()
try:
 _st_.current_tex_line = 79
 _st_.inline(2, latex(A))
except:
 _st_.goboom(79)
try:
 _st_.current_tex_line = 79
 _st_.inline(3, latex(B))
except:
 _st_.goboom(79)
try:
 _st_.current_tex_line = 79
 _st_.inline(2, latex(A))
except:
 _st_.goboom(79)
try:
 _st_.current_tex_line = 79
 _st_.inline(3, latex(B))
except:
 _st_.goboom(79)
_st_.current_tex_line = 98
_st_.blockbegin()
try:
   A = matrix([[1,2,3],[4,5,6]])
except:
 _st_.goboom(100)
_st_.blockend()
try:
 _st_.current_tex_line = 102
 _st_.inline(4, latex(A))
except:
 _st_.goboom(102)
try:
 _st_.current_tex_line = 102
 _st_.inline(5, latex(A.transpose()))
except:
 _st_.goboom(102)
_st_.current_tex_line = 141
_st_.blockbegin()
try:
   A = matrix([[1,2,3],[2,4,5],[3,5,6]])
   B = matrix([[1,2,3],[4,5,6],[7,8,9]])
except:
 _st_.goboom(144)
_st_.blockend()
try:
 _st_.current_tex_line = 150
 _st_.inline(6, latex(A))
except:
 _st_.goboom(150)
try:
 _st_.current_tex_line = 150
 _st_.inline(7, latex(B))
except:
 _st_.goboom(150)
try:
 _st_.current_tex_line = 150
 _st_.inline(6, latex(A))
except:
 _st_.goboom(150)
try:
 _st_.current_tex_line = 150
 _st_.inline(7, latex(B))
except:
 _st_.goboom(150)
_st_.endofdoc()
