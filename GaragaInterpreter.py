# BAHASA PEMROGRAMAN GARAGA-LANG 2020
# membuat interpreter

# mengimport kelas GaragaLexer
import GaragaLexer
# mengimport kelas GaragaParser
import GaragaParser

# ---class eksekusi---------------------------------------------------------
# Membuat kelas untuk interpreter garaga-lang
# Interpreter digunakan untuk mengeksekusi ekspresi yang telah diidentifikasi parser
class Program:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):

        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'angka':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'cetak':
            if node[1][0] == '"':
                print(node[1][1:len(node[1])-1])
            else:
                return self.walkTree(node[1])

        if node[0] == 'jika_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        if node[0] == 'condition_dobeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

        if node[0] == 'condition_tidaksam':
            return self.walkTree(node[1]) != self.walkTree(node[2])

        if node[0] == 'condition_lebdarsam':
            return self.walkTree(node[1]) >= self.walkTree(node[2])

        if node[0] == 'condition_kurdarsam':
            return self.walkTree(node[1]) <= self.walkTree(node[2])

        if node[0] == 'condition_lebdar':
            return self.walkTree(node[1]) > self.walkTree(node[2])

        if node[0] == 'condition_kurdar':
            return self.walkTree(node[1]) < self.walkTree(node[2])

        if node[0] == 'pendefinisian_fungsi':
            self.env[node[1]] = node[2]

        if node[0] == 'pemanggilan_fungsi':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Fungsi tidak terdefinisi '%s'" % node[1])
                return 0

        if node[0] == 'tambah':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'kurang':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'kali':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'bagi':
            return int(self.walkTree(node[1]) / self.walkTree(node[2]))
        elif node[0] == 'minus':
            return int(self.walkTree(node[1]) * (-1))

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Variabel tidak terdefinisi ditemukan: '"+node[1]+"'")
                return 0

        if node[0] == 'perulangan_untuk':
            if node[1][0] == 'konfigurasi_perulangan_untuk':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count+1, loop_limit+1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        print(res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == 'konfigurasi_perulangan_untuk':
            return (self.walkTree(node[1]), self.walkTree(node[2]))


if __name__ == '__main__':
    lexer = GaragaLexer.Program()
    parser = GaragaParser.Program()
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
            Program(tree, env)
