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