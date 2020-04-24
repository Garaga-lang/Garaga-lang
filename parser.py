# Mengambil kelas parser di library sly
from sly import Parser
# Mengambil kelas pemisahan di file lexer
import lexer

# ---class pengidentifikasian---------------------------------------------------------
# Membuat kelas untuk parser garaga-lang
# Parser digunakan untuk mengidentifikasi token
class pengidentifikasian(Parser):
    # Mengambil daftar token dari kelas lexer
    tokens = lexer.pemisahan.tokens
    
    # Aturan grammar dan tindakan
    # Untuk menyelesaikan ambiguitas
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),    # Unary minus operator
        )

    # Membuat array penempatan token
    def __init__(self):
        self.env = { }

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
        return ('cetak', p.KATA)
    # Membuat dekorator untuk nama fungsi
    @_('NAMA "(" ")"')
    def statement(self, p):
        return ('fungsi_call', p.NAMA)
    # Membuat dekorator untuk untuk - hingga
    @_('UNTUK var_assign HINGGA expr MAKA statement')
    def statement(self, p):
        return ('untuk_loop', ('untuk_loop_setup', p.var_assign, p.expr), p.statement)
    # Membuat dekorator untuk jika - maka - kaji
    @_('JIKA condition MAKA statement KAJI statement')
    def statement(self, p):
        return ('jika_stmt', p.condition, ('cabang', p.statement0, p.statement1))
    # Membuat dekorator untuk fungsi nama() ->
    @_('FUNGSI NAMA "(" ")" ARROW statement')
    def statement(self, p):
        return ('fungsi_def', p.NAMA, p.statement)
