from sly import Parser
# Mengambil kelas parser di library sly
import GaragaLexer

# ---class pengidentifikasian---------------------------------------------------------
# Membuat kelas untuk lexer garaga-lang
# Parser digunakan untuk mengidentifikasi token
class Program(Parser):
    # Mengambil daftar token dari kelas lexer
    tokens = GaragaLexer.Program.tokens

    # Aturan grammar dan tindakan
    # Untuk menyelesaikan ambiguitas
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),  # Unary minus operator
    )

    # Membuat array penempatan token
    def __init__(self):
        self.env = {}
        self.fun = {}

    # ---statement------------------------------------------------------------------------
    # Membuat dekorator untuk token kosong
    @_('')
    def statement(self, p):
        pass

    # Membuat dekorator untuk ekpresi
    @_('expr')
    def statement(self, p):
        return (p.expr)

    # Membuat dekorator var_assign
    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    # Membuat dekorator untuk cetak kata(string)
    @_('CETAK KATA')
    def statement(self, p):
        return p.KATA

    # Membuat dekorator untuk nama fungsi
    @_('NAMA "(" ")"')
    def statement(self, p):
       return self.fun[p.NAMA]

    # Membuat dekorator untuk untuk - hingga
    @_('UNTUK expr HINGGA expr MAKA statement')
    def statement(self, p):
        for i in range(p.expr0, p.expr1):
            hasil = self.statement
            print(hasil)

    # Membuat dekorator untuk jika - maka - kaji
    @_('JIKA condition MAKA statement KAJI statement')
    def statement(self, p):
        #return ('jika_stmt', p.condition, ('cabang', p.statement0, p.statement1))
        if p.condition:
            return p.statement0
        else: return p.statement1

    # Membuat dekorator untuk fungsi nama() ->
    @_('FUNGSI NAMA "(" ")" ARROW statement')
    def statement(self, p):
        self.fun[p.NAMA] = p.statement

    # Membuat dekorator untuk ketika - maka
    @_('KETIKA condition MAKA statement')
    def statement(self, p):
        while p.condition:
            p.statement

    # ---var_assign-----------------------------------------------------------------------
    # Membuat dekorator untuk penulisan nama = ekpresi
    @_('NAMA "=" expr')
    def var_assign(self, p):
        self.env[p.NAMA] = p.expr

    # Membuat dekorator untuk penulisan nama = kata(string)
    @_('NAMA "=" KATA')
    def var_assign(self, p):
        self.env[p.NAMA] = p.KATA

    # ---condition------------------------------------------------------------------------
    # Membuat dekorator untuk penulisan double equation (==)
    @_('expr DOBEQ expr')
    def condition(self, p):
        return p.expr0 == p.expr1

    # Membuat dekorator untuk penulisan tidak sama dengan (!=)
    @_('expr TIDAKSAM expr')
    def condition(self, p):
        return p.expr0 != p.expr1

    # Membuat dekorator untuk penulisan kurang dari sama dengan (<=)
    @_('expr KURDARSAM expr')
    def condition(self, p):
        return p.expr0 <= p.expr1

    # Membuat dekorator untuk penulisan lebih dari sama dengan (>=)
    @_('expr LEBDARSAM expr')
    def condition(self, p):
        return p.expr0 >= p.expr1

    # Membuat dekorator untuk penulisan kurang dari (<)
    @_('expr "<" expr')
    def condition(self, p):
        return p.expr0 < p.expr1

    # Membuat dekorator untuk penulisan lebih dari (>)
    @_('expr ">" expr')
    def condition(self, p):
        return p.expr0 > p.expr1

    # ---expression-----------------------------------------------------------------------
    # Membuat dekorator untuk penjumlahan (+)
    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    # Membuat dekorator untuk pengurangan (-)
    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    # Membuat dekorator untuk perkalian (*)
    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    # Membuat dekorator untuk pembagian (/)
    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    # Membuat dekorator untuk nilai minus (-ekspresi)
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    # Membuat dekorator untuk nama variabel
    @_('NAMA')
    def expr(self, p):
        try:
            return self.env[p.NAMA]
        except LookupError:
            print("Undefined name '%s'" % p.NAMA)
            return 0

    # Membuat dekorator untuk angka atau integer
    @_('ANGKA')
    def expr(self, p):
        return p.ANGKA

    # Membuat dekorator untuk cetak ekspresi
    @_('CETAK expr')
    def expr(self, p):
        return p.expr


# ---fungai main----------------------------------------------------------------------
# fungsi main program untuk melakukan pengujian pada parser
if __name__ == '__main__':
    # Memanggil kelas pemisahan pada lexer()
    lexer = GaragaLexer.Program()
    # Memanggil kelas pengidentifikasian pada parser()
    parser = Program()
    # Membuat array
    env = {}
    while True:
        try:
            text = input('garaga > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
