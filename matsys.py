from sage.all import latex


class Term(object):

    def __init__(self, c, i, varname=None):
        self.c = c
        self.i = i
        if varname is None:
            self.varname = 'x'
        else:
            self.varname = varname

    def str_variable(self):
        if self.c == 0:
            return ' '
        return '{}_{{{}}}'.format(self.varname, self.i + 1)

    def str_coeff(self):
        if self.c == 0 or self.c.abs() == 1:
            return ''
        if self.i == 0:
            return '{}\\,'.format(latex(self.c))
        return '{}\\,'.format(latex(self.c.abs()))

    def pm(self):
        if self.i == 0:
            return ''
        if self.c.sign() == 1:
            return '+'
        elif self.c.sign() == -1:
            return '-'
        return ' '

    def amper(self):
        if self.i == 0:
            return ''
        return '&'

    def str(self):
        return '{} {} {}{} & '.format(self.pm(), self.amper(), self.str_coeff(), self.str_variable())

    def __repr__(self):
        return '\'' + self.str() + '\''


class Line(object):

    def __init__(self, v, lastline=None, varname=None):
        self.v = v
        self.lastline = lastline
        self.varname = varname

    def terms_iter(self):
        return (Term(c, i) for i, c in enumerate(self.v[:-1]))

    def pre(self):
        return ' '.join(t.str() for t in self.terms_iter())

    def post(self):
        if self.lastline is None:
            return '= & {} \\\\\n'.format(self.v[-1])
        return '= & {}'.format(self.v[-1])

    def str(self):
        return self.pre() + self.post()

    def __repr__(self):
        return '\'' + self.str().rstrip('\n\r') + '\''


def var_from_num(c, i, varname=None):
    if varname is None:
        varname = 'x'
    return '{}\\,{}_{{{}}}'.format(latex(c), varname, i)


def mat2sys(A):
    return None
