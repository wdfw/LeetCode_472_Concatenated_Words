# 題目
![image](https://user-images.githubusercontent.com/111077328/215144168-c243b5a9-95ec-4827-a7e4-fff38050e037.png)
# 例子
![image](https://user-images.githubusercontent.com/111077328/215144330-da5cba43-f6d4-4d60-96e1-b585808001d6.png)
# 思路
題目要找concatenated word，所以想要組成word，要從小的先開始組成，所以先將words依字長度排序，由短的開始尋找，
且因為最短的word，是不可能被組成的(All the strings of words are unique.)，所以可以直接放入字典，成為可能組成的元素，
然後透過下圖這種方式找word是否可以被組成。而每個word的位置只要走一次就可以知道是否是concatenated word，所以透過passed紀錄走訪過的位置

![image](https://user-images.githubusercontent.com/111077328/215147528-236df958-ef43-43ea-a9ec-6fdf49890cf3.png)
