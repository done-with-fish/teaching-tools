from collections import namedtuple
from sage.all import elementary_matrix, latex


def swaptex(i, j):
    return 'R_{{{}}}\\leftrightarrow R_{{{}}}'.format(i + 1, j + 1)


def scaletex(s, i):
    return '{}\\cdot R_{{{}}}\\to R_{{{}}}'.format(latex(s), i + 1, i + 1)


def addtex(i, j, s):
    if s.sign() == -1:
        pm = '-'
    elif s.sign() == 1:
        pm = '+'
    else:
        raise TypeError('scalar must be nonzero!')
    if s.abs() == 1:
        i += 1
        j += 1
        return 'R_{{{}}} {} R_{{{}}}\\to R_{{{}}}'.format(i, pm, j, i)
    t = latex(s.abs())
    i += 1
    j += 1
    return 'R_{{{}}} {} {}\\cdot R_{{{}}}\\to R_{{{}}}'.format(i, pm, t, j, i)


def pivotgetter(A, rownum, colnum):
    'raises ValueError if pivot is impossible'
    n = A.nrows()
    if A[rownum, colnum]:
        s = A[rownum, colnum]
        E = elementary_matrix(n, row1=rownum, scale=s)
        l = scaletex(1 / s, rownum)
        return E.inverse(), l
    col = A.columns()[colnum]
    swap_pos = min([_ for _ in col.nonzero_positions() if rownum <= _])
    E = elementary_matrix(n, row1=rownum, row2=swap_pos)
    l = swaptex(rownum, swap_pos)
    return E, l


def clearcolumn(A, pivotrow, pivotcol):
    elems = []
    tex = []
    n = A.nrows()
    if A[pivotrow, pivotcol] != 1:
        raise TypeError(
            'No pivot in position ({}, {})'.format(pivotrow, pivotcol))
    for rownum in xrange(n):
        if rownum == pivotrow:
            continue
        row = A.rows()[rownum]
        s = row[pivotcol]
        if s:
            E = elementary_matrix(n, row1=rownum, row2=pivotrow, scale=-s)
            l = addtex(rownum, pivotrow, -s)
            elems.append(E)
            tex.append(l)
            A = E * A
    return A, elems, tex


def reduction_info(A):
    elems = []
    tex = []
    lastpivotrow = -1
    for colnum in xrange(A.ncols()):
        for rownum in xrange(lastpivotrow + 1, A.nrows()):
            if A[rownum, colnum] == 1:
                lastpivotrow = rownum
                A, new_elems, new_tex = clearcolumn(A, rownum, colnum)
                elems += new_elems
                tex += new_tex
            while A[rownum, colnum] != 1:
                try:
                    E, l = pivotgetter(A, rownum, colnum)
                    elems.append(E)
                    tex.append(l)
                    A = E * A
                except ValueError:
                    break
            else:
                lastpivotrow = rownum
                A, new_elems, new_tex = clearcolumn(A, rownum, colnum)
                elems += new_elems
                tex += new_tex
    RowInfo = namedtuple('RowInfo', 'rref, elems, latex')
    return RowInfo(A, elems, tex)


def latex_reduction(A, M=None):
    if M is None:
        M = A
    info = reduction_info(A)
    s = '\\begin{align*}\n'
    s += latex(M)
    s += '\n'
    for l, E in zip(info.latex, info.elems):
        M = E * M
        s += '&\\xrightarrow{{{}}}\n{} \\\\ \n'.format(l, latex(M))
    s += '\\end{align*}'
    return s
