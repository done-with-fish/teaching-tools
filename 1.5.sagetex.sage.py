## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file 1.5.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_188 = Integer(188); _sage_const_162 = Integer(162); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_163 = Integer(163); _sage_const_34 = Integer(34); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_161 = Integer(161); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_183 = Integer(183); _sage_const_18 = Integer(18); _sage_const_49 = Integer(49); _sage_const_86 = Integer(86); _sage_const_116 = Integer(116); _sage_const_69 = Integer(69); _sage_const_171 = Integer(171); _sage_const_170 = Integer(170); _sage_const_155 = Integer(155); _sage_const_172 = Integer(172); _sage_const_153 = Integer(153); _sage_const_177 = Integer(177); _sage_const_149 = Integer(149); _sage_const_33 = Integer(33); _sage_const_21 = Integer(21); _sage_const_192 = Integer(192); _sage_const_196 = Integer(196); _sage_const_32 = Integer(32); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_54 = Integer(54); _sage_const_35 = Integer(35); _sage_const_52 = Integer(52); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_108 = Integer(108); _sage_const_74 = Integer(74); _sage_const_76 = Integer(76); _sage_const_181 = Integer(181); _sage_const_168 = Integer(168); _sage_const_72 = Integer(72); _sage_const_101 = Integer(101); _sage_const_164 = Integer(164); _sage_const_169 = Integer(169); _sage_const_79 = Integer(79); _sage_const_105 = Integer(105); _sage_const_160 = Integer(160); _sage_const_107 = Integer(107); _sage_const_111 = Integer(111)## This file (1.5.sagetex.sage) was *autogenerated* from 1.5.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('1.5', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_16 
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='[', right=']')
except:
 _st_.goboom(_sage_const_18 )
_st_.blockend()
_st_.current_tex_line = _sage_const_26 
_st_.blockbegin()
try:
   A = matrix([[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ],[_sage_const_7 ,_sage_const_0 ,_sage_const_10 ],[_sage_const_0 ,-_sage_const_1 ,_sage_const_6 ]])
   A21 = matrix([[_sage_const_2 ,_sage_const_3 ],[-_sage_const_1 ,_sage_const_6 ]])
except:
 _st_.goboom(_sage_const_29 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_31 
 _st_.inline(_sage_const_0 , latex(A))
except:
 _st_.goboom(_sage_const_31 )
try:
 _st_.current_tex_line = _sage_const_31 
 _st_.inline(_sage_const_1 , latex(A21))
except:
 _st_.goboom(_sage_const_31 )
_st_.current_tex_line = _sage_const_49 
_st_.blockbegin()
try:
   var('a b c d')
   A = matrix([[a,b],[c,d]])
except:
 _st_.goboom(_sage_const_52 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_54 
 _st_.inline(_sage_const_2 , latex(A))
except:
 _st_.goboom(_sage_const_54 )
_st_.current_tex_line = _sage_const_69 
_st_.blockbegin()
try:
   var('a11 a12 a13 a21 a22 a23 a31 a32 a33')
   A = matrix([[a11, a12, a13],[a21, a22, a23],[a31, a32, a33]])
except:
 _st_.goboom(_sage_const_72 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_74 
 _st_.inline(_sage_const_3 , latex(A))
except:
 _st_.goboom(_sage_const_74 )
_st_.current_tex_line = _sage_const_76 
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='|', right='|')
   M = lambda i,j: A.delete_rows([i-_sage_const_1 ]).delete_columns([j-_sage_const_1 ])
except:
 _st_.goboom(_sage_const_79 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_4 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_5 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_6 , latex(M(_sage_const_1 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_4 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_5 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_6 , latex(M(_sage_const_1 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_86 )
_st_.current_tex_line = _sage_const_101 
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='[', right=']')
   var('a11 a12 a13 a21 a22 a23 a31 a32 a33')
   A = matrix([[a11, a12, a13],[a21, a22, a23],[a31, a32, a33]])
except:
 _st_.goboom(_sage_const_105 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_107 
 _st_.inline(_sage_const_7 , latex(A))
except:
 _st_.goboom(_sage_const_107 )
_st_.current_tex_line = _sage_const_108 
_st_.blockbegin()
try:
     latex.matrix_delimiters(left='|', right='|')
     M = lambda i,j: A.delete_rows([i-_sage_const_1 ]).delete_columns([j-_sage_const_1 ])
   
except:
 _st_.goboom(_sage_const_111 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_8 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_9 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_10 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_11 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_12 , latex(M(_sage_const_3 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_13 , latex(M(_sage_const_3 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_8 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_9 , latex(M(_sage_const_1 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_10 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_11 , latex(M(_sage_const_1 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_12 , latex(M(_sage_const_3 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_13 , latex(M(_sage_const_3 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_116 )
_st_.current_tex_line = _sage_const_149 
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='|', right='|')
   A = matrix([[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ],[_sage_const_4 ,_sage_const_5 ,_sage_const_6 ],[_sage_const_7 ,_sage_const_8 ,_sage_const_9 ]])
   M = lambda i,j: A.delete_rows([i-_sage_const_1 ]).delete_columns([j-_sage_const_1 ])
except:
 _st_.goboom(_sage_const_153 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_14 , latex(A))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.inline(_sage_const_15 , latex(A))
except:
 _st_.goboom(_sage_const_160 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_16 , latex((-_sage_const_1 )**(_sage_const_2 +_sage_const_1 )*A[_sage_const_1 ,_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_17 , latex(M(_sage_const_2 ,_sage_const_1 )))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_18 , latex((-_sage_const_1 )**(_sage_const_2 +_sage_const_2 )*A[_sage_const_1 ,_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_19 , latex(M(_sage_const_2 ,_sage_const_2 )))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_20 , latex((-_sage_const_1 )**(_sage_const_2 +_sage_const_3 )*A[_sage_const_1 ,_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_21 , latex(M(_sage_const_2 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_164 
 _st_.inline(_sage_const_22 , latex(A.det()))
except:
 _st_.goboom(_sage_const_164 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_23 , latex(A))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_169 
 _st_.inline(_sage_const_24 , latex((-_sage_const_1 )**(_sage_const_1 +_sage_const_3 )*A[_sage_const_0 ,_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_169 )
try:
 _st_.current_tex_line = _sage_const_169 
 _st_.inline(_sage_const_25 , latex(M(_sage_const_1 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_169 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_26 , latex((-_sage_const_1 )**(_sage_const_2 +_sage_const_3 )*A[_sage_const_1 ,_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_27 , latex(M(_sage_const_2 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_28 , latex((-_sage_const_1 )**(_sage_const_3 +_sage_const_3 )*A[_sage_const_2 ,_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_29 , latex(M(_sage_const_3 ,_sage_const_3 )))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_30 , latex(A.det()))
except:
 _st_.goboom(_sage_const_172 )
_st_.current_tex_line = _sage_const_177 
_st_.blockbegin()
try:
   latex.matrix_delimiters(left='|', right='|')
   A = matrix([[_sage_const_7 ,-_sage_const_3 ,_sage_const_0 ,_sage_const_4 ],[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_3 ],[_sage_const_2 ,_sage_const_1 ,-_sage_const_2 ,-_sage_const_5 ],[_sage_const_0 ,_sage_const_4 ,_sage_const_0 ,_sage_const_6 ]])
   M = lambda X, i,j: X.delete_rows([i-_sage_const_1 ]).delete_columns([j-_sage_const_1 ])
except:
 _st_.goboom(_sage_const_181 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_183 
 _st_.inline(_sage_const_31 , latex(A))
except:
 _st_.goboom(_sage_const_183 )
try:
 _st_.current_tex_line = _sage_const_188 
 _st_.inline(_sage_const_32 , latex(A))
except:
 _st_.goboom(_sage_const_188 )
try:
 _st_.current_tex_line = _sage_const_188 
 _st_.inline(_sage_const_33 , latex(M(A, _sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_188 )
try:
 _st_.current_tex_line = _sage_const_192 
 _st_.inline(_sage_const_34 , latex(M(A, _sage_const_3 , _sage_const_3 )))
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.current_tex_line = _sage_const_192 
 _st_.inline(_sage_const_35 , latex(M(M(A, _sage_const_3 , _sage_const_3 ), _sage_const_1 , _sage_const_1 )))
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_36 , latex(A))
except:
 _st_.goboom(_sage_const_196 )
try:
 _st_.current_tex_line = _sage_const_196 
 _st_.inline(_sage_const_37 , latex(A.det()))
except:
 _st_.goboom(_sage_const_196 )
_st_.endofdoc()

