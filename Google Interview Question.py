#Bu soru Google Interview Question sorusunun aynisi
#We are given an array of integers and a particular sum.
#We have to check if there are any two elements in the array that add up to the given sum.
#For example, array = [1,2,4,5] ,sum = 6
#This should return True as 2+4 = 6


#Akla ilk gelen cozum basit olsa da time complexity bakimindan mantikli olmayabilir.
#Akla ilk gelen cozumu asagiya yaptim.

array = [1,2,4,5]
sum = 3
def akla_ilk_gelen_cozum(array, sum):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == sum:
                return "Yes"
    return "No"

print(akla_ilk_gelen_cozum(array, sum))

#Gordugunuz uzere cozum bu sekilde yapilabiliyor olsa da Big O notation O(n^2) oluyor. Bu da buyuk sirketlerin isteyecegi bir sey olmayabilir.



#O(n^2) notation dan kurtulmak icin baska bir cozum bulmamiz gerekiyor.
##Dizide bir kez döngü yapip karşılaştığımız her öğe için onun tümleyenini hesaplayalim.
#Elimizdeki elemani sum'a esitleyelim.
#Daha sonra dizinin geri kalan kısmında bu tumleyen için binary search ile cozumu bulmaya calisabiliriz..
#Binary search O(log n) notationa denk gelir. Biz de binary search kullandigimiz icin karmasikligimiz O(log n) olur. Ki bu da hatirlarsiniz ki O(n^2) den iyidir.

def binary_search(array,left,right, ele):
    if right >= left:
        mid = (left+right)//2
        if (array[mid]) == ele:
            return True
        elif array[mid] > ele:
            return binary_search(array, left, mid - 1, ele)
        else:
            return binary_search(array, mid + 1, right, ele)
    else:
        return False

def daha_iyi_cozum(array, sum):
    for i in range(len(array)):
        comp = sum - array[i]
        if binary_search(array,i+1,len(array)-1,comp):
            return "Yes"
    return "No"

print(daha_iyi_cozum(array,sum))

#O(log n) cozumunu bulmus olsak da kodun hala gelistirilebilir oldugunu fark ediyoruz.
#O(n) yapmaya calisalim.

#Cozum:
#Binary search'in her iki ucundan eleman alip toplamlarini bizden istenen sum a esitse cevap dogrudur.
#Eger degilse, ve eger toplam elde ettigimizden buyukse,toplamının daha yüksek olmasını istediğimiz anlamına gelir
#Bunu yapmak için sol dizinden birer birer saga dogru hareket etmemiz gerekir ve karşılık gelen sayiyi sağ dizindeki sayiya ekleriz.
#Ve eğer verilen toplam elde ettiğimizden azsa bu, iki sayinin daha küçük olmasını istediğimiz anlamına gelir,
#Bu sefer de sağ dizini bir adım sola kaydırıyoruz ve karşılık gelen sayiyi sol dizindeki sayiya ekliyoruz.
#Verilen toplamın toplamına eşit olan bir çift bulana kadar veya sol ve sağ endeksler kesişene kadar bu şekilde ilerlemeye devam ediyoruz
#Bu dizide yalnızca bir kez geçiş yapılmasını gerektndiginden, karmaşıklık O(n) olur.

def smart_pair_sum(array, sum):
    left = 0
    right = len(array)-1
    while right > left:
        if array[left] + array[right] == sum:
            return "Yes"
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return "No"

print(smart_pair_sum(array,sum))



