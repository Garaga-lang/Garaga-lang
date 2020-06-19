# Garaga-Lang 2020
Garaga-lang adalah sebuah bahasa pemrograman baru yang dikembangkan menggunakan bahasa python sebagai dasar pemrograman-seperti pembuatan token, pemisahan token, pengidentifikasian dan pengujian prorgram. 

## Anggota:
- Elfanty Dhea
- David Leandro Wibisono
- Nugraha Dwi Putra

---

# Dokumentasi

## Penting!

- [x] Bahasa ini dikembangkan dengan [PYTHON version 3.*](https://www.python.org/ "Python")
- [x] Bahasa ini memiliki ekstensi .garaga

## Command di Garaga-Lang

| GARAGA-LANG |  MEAN  |
| --------- |  ----  |
| jika      |  IF    |
| cetka     |  PRINT |
| maka      |  THEN  |
| kaji      |  ELSE  |
| untuk     |  FOR   |
| fungsi    |  FUN   |
| hingga    |  TO    |
| ->        |  ARROW |


## Cara Penggunaan 

**Ikuti langkah-langkah ini**
1. Buka cmd atau terminal pada direktori ini `cd .../Garaga-Lang/`
2. Dan kemudian jalankan file run.py atau open.py, run.py berguna untuk penulisan kode secara langsung
    . Sedangkan open.py digunakan untuk menjalankan file.garaga

Sebagai contoh penggunaan open.py : 
jalankan perintah berikut pada cmd/terminal
```
python open.py helloworld.py
```

**_Sekarang coba untuk file-file yang lain_**

> file .garaga dapat kalian edit sesuai keinginan

## Contoh Garaga-Lang

### PRINT Hello World!!

**contoh:**
```
cetak "Hello World" 
```

**hasil:**
```
Hello World
```

**atau:**
```
a= "Hello World"
cetak a 
```

**hasil**
```
"Hello World"
```

### Aritmatika

**contoh:**
```
1+2
2-3
4*5
6/3
```

**result**
```
3
-1
20
2
```

**atau**
```
a=10
b=2
cetak a+b
cetak a-b
cetak a*b
cetak a/b
```

**hasil**
```
12
8
20
5
```

### IF ELSE 

> JIKA _expr_ MAKA _stmt1_ KAJI _stmt2_

**contoh:**
```
a=2
y="true"
n="false"
jika a==3 maka cetak y kaji cetak n
```

**hasil**
```
"false"
```

### FOR

> UNTUK _expr_ HINGGA _stmt1_ MAKA _stmt2_

**contoh:**
```
untuk a=0 hingga 5 maka cetak a
```

**hasil:**
```
0
1
2
3
4
```

### Function

> fungsi namaFungsi() -> penulisan kode..

**contoh:**
```
fungsi sapa() -> TNIRP "haii.."

sapa()
```

**hasil:**
```
haii..
```

### Penggunaan komentar

> Anda dapat menggunakan simbol`'#'` untuk membuat komentar pada penulisan kode garaga-lang

**contoh:**
```
# ini adalah komentar
cetak "ini bukan komentar"
# ini adalah komentar
```

**hasil:**
```
ini bukan komentar
```

Selesai, Terima Kasih!!
