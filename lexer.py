#BAHASA PEMROGRAMAN GARAGA-LANG 2020
#membuat lexer
#mengambil kelas Lexer di dalam Library sly
from sly import Lexer

#membuat kelas untuk lexer garaga-lang
#lexer digunakan untuk memisahkan text ke dalam token
class pemisahanLexer(Lexer):
    #membuat nama-nama token (sangat diperlukan)
    tokens   = {NAMA, ANGKA, KATA, CETAK, JIKA, KAJI, KETIKA, MAKA, UNTUK, HINGGA, FUNGSI, DOBEQ}
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '{', '}', '<', '>'}
    
    #membuat karakter yang akan ditolak token
    ignore = ' \t'              #mengabaikan spaso
    ignore_comment = r'\#.*'    #mengabaikan komentar
    ignore_newline = r'\n+'     #mengabaikan perintah \n

    #membuat token harus mengenali reguler expression seperti apa
    NAMA    = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ANGKA   = r'\d+'
    KATA    = r'\".*?\"'
    DOBEQ   = r'=='

    #token remapping kasus khusus
    NAMA['cetak']   = CETAK
    NAMA['jika']    = JIKA
    NAMA['kaji']    = KAJI
    NAMA['ketika']  = KETIKA 
    NAMA['maka']    = MAKA
    NAMA['untuk']   = UNTUK
    NAMA['hingga']  = HINGGA
    NAMA['fungsi']  = FUNGSI

    #menambahkan aski
    def ANGKA(self, t):            #merubah angka ke integer
        t.value = int(t.value)
        return t
    
    def ignore_newline(self, t):    #mendefiniskan menolak baris baru
        self.lineno += len(t.value)
    
    def find_column(text, token):   #mencari kolom
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column