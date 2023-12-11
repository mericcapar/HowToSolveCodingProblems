# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

def ilk_akla_gelen_cozum(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

"""

Ilk cozum ilk akla gelen cozum olmakla birlikte array'lerin cok buyuk oldugunu dusunecek olursak bize time complexity
bakimindan cok buyuk sorun cikartir. Burada ic ice dongu kullandigimiz icin bunun time complexity'sine
O(m x n) diyebiliriz. m x n dememizin sebebi de her iki array'in buyukluklerinin farkli olmasi.
Eger ki array'ler ayni boyutta olsaydi O(n^2) diyebilirdik. 

Dedigim gibi bu cozum ilk akla gelen cozum olsa da verimsiz oldugunu soyleyebiliriz.
Bunun yerine daha verimli bir cozum bulmamiz gerekli.

Onun yerine bir dictionary olusturup birinci arrayin elemanlarini bu dictionary'e kaydedebiliriz.
Bundan sonra da ikinci array uzerinde kontrol edebiliriz.
Burada ilk array'in elemanlarini loop ile dictionary'e kaydetmemiz gerektigi icin buradan bir dongu olusturmamiz gerekli.
Kontrol icin de ayri bir loop olusturmamiz gerekli bu da ikinci bir dongu yaratmamizi sagliyor. 
Fakat ustteki cozumden farkli olarak iki ayri dongu olusturdugumuz icin time complexity'e O(m+n) diyebiliriz.
Burada m = Dictionary'ye kaydetmek icin olusturdugumuz dongu. n = array2'yi kontrol ederken olusturdugumuz dongu.

"""

def mantikli_cozum(array1, array2):
    dictionary = dict()
    for i in range(len(array1)):
        dictionary[array1[i]] = True


    for i in range(len(array2)):
        if array2[i] in dictionary:
            return True

    return False

print(mantikli_cozum(array1, array2))

