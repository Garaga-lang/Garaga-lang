# BAHASA PEMROGRAMAN GARAGA-LANG 2020
# membuat parser
# Mengambil kelas parser di library sly
from sly import Parser

# mengimport kelas GaragaLexer
import GaragaLexer

# ---class pengidentifikasian---------------------------------------------------------
# Membuat kelas untuk parser garaga-lang
# Parser digunakan untuk mengidentifikasi token
class Program(Parser):

    # Mengambil daftar token dari kelas lexer
    tokens = GaragaLexer.Program.tokens

    # Aturan grammar dan tindakan
    # Untuk menyelesaikan ambiguitas
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    # Membuat array penempatan token
    def __init__(self):
        self.env = {}

    # Membuat dekorator untuk token kosong
    @_('')
    def statement(self, p):
        pass

    # Membuat dekorator untuk untuk - hingga
    @_('UNTUK var_assign HINGGA expr MAKA statement')
    def statement(self, p):
        return ('perulangan_untuk', ('konfigurasi_perulangan_untuk', p.var_assign, p.expr), p.statement)

    # Membuat dekorator untuk jika - maka - kaji
    @_('JIKA condition MAKA statement KAJI statement')
    def statement(self, p):
        return ('jika_stmt', p.condition, ('branch', p.statement0, p.statement1))

    # Membuat dekorator untuk fungsi nama() ->
    @_('FUNGSI NAMA "(" ")" ARROW statement')
    def statement(self, p):
        return ('pendefinisian_fungsi', p.NAMA, p.statement)

    # Membuat dekorator pemanggilan fungsi
    @_('NAMA "(" ")"')
    def statement(self, p):
        return ('pemanggilan_fungsi', p.NAMA)

    # Membuat dekorator untuk penulisan double equation (==)
    @_('expr DOBEQ expr')
    def condition(self, p):
        return ('condition_dobeq', p.expr0, p.expr1)

    # Membuat dekorator untuk penulisan tidak sama dengan (!=)
    @_('expr TIDAKSAM expr')
    def condition(self, p):
        return ('condition_tidaksam', p.expr0, p.expr1)

    # Membuat dekorator untuk penulisan kurang dari sama dengan (<=)
    @_('expr KURDARSAM expr')
    def condition(self, p):
        return ('condition_kurdarsam', p.expr0, p.expr1)

    # Membuat dekorator untuk penulisan lebih dari sama dengan (>=)
    @_('expr LEBDARSAM expr')
    def condition(self, p):
        return ('condition_lebdarsam', p.expr0, p.expr1)

    # Membuat dekorator untuk penulisan kurang dari (<)
    @_('expr "<" expr')
    def condition(self, p):
        return ('condition_kurdar', p.expr0, p.expr1)

    # Membuat dekorator untuk penulisan lebih dari (>)
    @_('expr ">" expr')
    def condition(self, p):
        return ('condition_lebdar', p.expr0, p.expr1)

    # Membuat dekorator var_assign
    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    # Membuat dekorator untuk penulisan nama = ekpresi
    @_('NAMA "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAMA, p.expr)

    # Membuat dekorator untuk penulisan nama = kata(string)
    @_('NAMA "=" KATA')
    def var_assign(self, p):
        return ('var_assign', p.NAMA, p.KATA)

    # Membuat dekorator untuk ekpresi
    @_('expr')
    def statement(self, p):
        return (p.expr)

    # Membuat dekorator untuk penjumlahan (+)
    @_('expr "+" expr')
    def expr(self, p):
        return ('tambah', p.expr0, p.expr1)

    # Membuat dekorator untuk pengurangan (-)
    @_('expr "-" expr')
    def expr(self, p):
        return ('kurang', p.expr0, p.expr1)

    # Membuat dekorator untuk perkalian (*)
    @_('expr "*" expr')
    def expr(self, p):
        return ('kali', p.expr0, p.expr1)

    # Membuat dekorator untuk pembagian (/)
    @_('expr "/" expr')
    def expr(self, p):
        return ('bagi', p.expr0, p.expr1)

    # Membuat dekorator untuk nilai minus (-ekspresi)
    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        #return p.expr
        return ('minus', p.expr)

    # Membuat dekorator untuk nama variabel
    @_('NAMA')
    def expr(self, p):
        return ('var', p.NAMA)

    # Membuat dekorator untuk angka atau integer
    @_('ANGKA')
    def expr(self, p):
        return ('angka', p.ANGKA)

    # Membuat dekorator untuk cetak ekspresi
    @_('CETAK expr')
    def expr(self, p):
        return ('cetak', p.expr)

    # Membuat dekorator untuk cetak kata(string)
    @_('CETAK KATA')
    def statement(self, p):
        return ('cetak', p.KATA)

# ---fungai main----------------------------------------------------------------------
# fungsi main program untuk melakukan pengujian pada parser
if __name__ == '__main__':
    # Memanggil kelas pemisahan pada lexer()
    lexer = GaragaLexer.Program()
    # Memanggil kelas pengidentifikasian pada parser()
    parser = Program()
    # Membuat array
    env = {}
    ujiCoba = '''
        # Komentar
        nama = "Garaga"
        tahun = 2020
        a=2
        b=3
        cetak tahun
        fungsi hitung() -> cetak a+b
        untuk a hingga 3 maka cetak nama
        jika a==2 maka cetak "true" kaji cetak "false"
        {}
        '''
    while True:
        try:
            text = input('garaga > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
