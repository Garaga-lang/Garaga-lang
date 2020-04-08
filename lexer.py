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