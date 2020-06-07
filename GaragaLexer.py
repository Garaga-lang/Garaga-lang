# BAHASA PEMROGRAMAN GARAGA-LANG 2020
# membuat lexer
# mengambil kelas Lexer di dalam Library sly
from sly import Lexer


# ---class pemisahan---------------------------------------------------------
# membuat kelas untuk lexer garaga-lang
# lexer digunakan untuk memisahkan text ke dalam token
class Program(Lexer):
    # membuat nama-nama token (sangat diperlukan)
    tokens = {NAMA, ANGKA, KATA, CETAK, JIKA, KAJI, MAKA, UNTUK, HINGGA, FUNGSI,
              ARROW, KETIKA, DOBEQ, KURDARSAM, LEBDARSAM, TIDAKSAM}
    # literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '{', '}', '<', '>'}
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';', '<', '>'}

    # membuat karakter yang akan ditolak token
    ignore = ' \t'  # mengabaikan spaso
    ignore_comment = r'\#.*'  # mengabaikan komentar
    ignore_newline = r'\n+'  # mengabaikan perintah \n

    # membuat token harus mengenali reguler expression seperti apa
    NAMA = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ANGKA = r'\d+'
    KATA = r'\".*?\"'
    DOBEQ = r'=='
    ARROW = r'->'
    KURDARSAM = r'<='
    LEBDARSAM = r'>='
    TIDAKSAM = r'!='

    # token remapping kasus khusus
    NAMA['cetak'] = CETAK
    NAMA['jika'] = JIKA
    NAMA['kaji'] = KAJI
    NAMA['maka'] = MAKA
    NAMA['untuk'] = UNTUK
    NAMA['hingga'] = HINGGA
    NAMA['fungsi'] = FUNGSI
    NAMA['ketika'] = KETIKA

    # menambahkan aski
    def ANGKA(self, t):  # merubah angka ke integer
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):  # mendefiniskan menolak baris baru
        self.lineno += len(t.value)

    def find_column(text, token):  # mencari kolom
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    # penanganan kesalahan
    def error(self, t):
        print('Baris %d: TERDAPAT KESALAHAN KARAKTER %r' % (self.lineno, t.value[0]))
        self.index += 1


# ---fungai main----------------------------------------------------------------------
# fungsi main program untuk melakukan pengujian pada lexer
if __name__ == '__main__':
    # data uji coba
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
    ketika b!=3 maka cetak "false"
    {}
    '''
    # memanggil kelas pemisahan()
    lexer = Program()
    # menampilkan token yang berhasil dikenali
    for tok in lexer.tokenize(ujiCoba):
        # print('tipe =%r --> nilai=%r'%(tok.type, tok.value))
        print(tok)
