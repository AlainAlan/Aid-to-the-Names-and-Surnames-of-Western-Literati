# Aid-to-the-Names-and-Surnames-of-Western-Literati
西儒名姓资<br>
按：名称戏仿《西儒耳目资》，参见[Nicolas Trigault - Wikipedia](https://en.wikipedia.org/wiki/Nicolas_Trigault#Publications)

csv文件用UTF-8编码，使用Excel打开需要采取`数据-获取和转换数据-从文本/CSV`并选择Unicode（UTF-8），方能安全打开避免乱码。

文件仍在建设中。<br>

详情可参：[附录（二）：汉学家汉名表](https://mp.weixin.qq.com/s/K9qDpcOuWXKXCNDebQQP_Q)。

## 数据来源

### Chinese Names of Western Scholars
A directory compiled and maintained by Philip Clart 柯若樸 (University of Leipzig)
[链接在这里](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.htm)

data文件夹中，名为`PhilipClart.csv`的文件是复制自该网页然后用Excel转存的。
使用`PhilipClart-csv2csv.py`将csv文件输出到`PhilipClart-output.txt`。具体可以自己看代码。
很多不统一的地方是我人肉一个一个调的，尤其是全角半角字符的问题。

其中，有的学者没有“姓氏”（系佛家子弟），为了保证体例统一，在其洋文姓一栏录为“Shi”，中文名录为“释·某某”，以区别于原来就有的“释”姓。
当然，“印顺”大师带有“释”字的名字也较为通用。

### English/Chinese Comparison Table for Names of Chinese Studies Scholars
### 北美中国研究学者英中姓名对照
> Zhang, Haihui and Xue, Zhaohui and Jiang, Shuyong and Lugar, Gary Lance (2013) English/Chinese Comparison Table for Names of Chinese Studies Scholars [ 北美中国研究学者英中姓名对照 ]. In: A Scholarly Review of Chinese Studies in North America = 北美中国研究综述. Association for Asian Studies (AAS). ISBN 978-0-924304-72-9
Last updated: 16 November 2017

这里使用的是[该页面](http://d-scholarship.pitt.edu/17682/PDF)“As of October 12, 2020”的一版pdf。我已经把pdf文件偷过来放在了data文件夹下。然后使用福昕PDF编辑器转成docx，然后复制粘贴到txt。后缀为plain的删掉了开头的介绍。

其中`List*`几个文件就是辗转转换的原文件。然后主要的调整都是在`HaihuiZhang.txt`中做的。包括但不限于：
1. 将“又作”、“又译作”、“又名”、“亦名”、“号某某”、“也作”等等统一（因此不细分）。
2. 删除von、van导致的两见，只保留von在姓中的一种情况。
3. 把部分空格改成tab
4. 调整全角半角

然后通过`HaihuiZhang-txt2csv.py`输出成后缀为txt但实为csv的output。

## 基本格式

1. 洋名：名前姓后的全名（带diacritics）
2. 洋姓：洋姓（带von、van者亦在其内）
3. 洋字：除了姓之外的剩余部分
4. 中文名：保留原文件中的字符
5. 汉名：中文名机器转换为简体字
6. 漢名：中文名机器转换为繁体字
7. 洋名又名：其他写法（例如名字部分简写为首字母与否，或者是否冠夫姓，或者译音或另起洋名等造成的洋名又名）
8. 中文名又名：其他中文名，保留原字符，不转换繁简
9. 洋名去调符：由于我个人不懂Unicode也不懂normalize，盗用[OpenTaal/diacritic-removal: Remove diacritics from characters](https://github.com/OpenTaal/diacritic-removal)的一段代码。其[LICENSE](https://github.com/OpenTaal/diacritic-removal/blob/master/LICENSE)。
10. 
11. 洋名又名去调符：如果洋名又名本身无diacritic，此项手动删掉。
12. 所见次数：此即我个人在手动编制过程中在不同地方看到该洋汉对应关系的次数，年久日深将可以作为该学者在笔者领域影响力的altmetrics(bushi
13. 族裔：尚未标准化，也仅著录少数学者，有待将来再搞
14. 备注：人物关系、著作、领域、传教士。尚未标准化，以后再说。

## 依赖

如果有哪位闲的无聊，想看看代码的话，那我只能说依赖Python的OpenCC，记得装。
``` pip install opencc```

## Chinese Names of Western Scholars & Western Names of Chinese Scholars

Just too lazy to write an En version.

> This listing aims to facilitate communication between Western and Asian China-scholars. As anyone who has attended a bi- or multilingual conference can attest, some amount of confusion is occasioned by the fact that Western sinologists are usually known in Chinese-speaking academia primarily by their Chinese names. As the latter, however, are not in common use in Western academic circles, it often takes a while to figure out that, for example, the professor Du Zanqi 杜贊奇, whom a Chinese conference participant keeps citing, is in fact better known in the English-speaking world as Prasenjit Duara.<br>
> [柯若樸](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.htm)

目标一致，只不过想：
1. 著录更加详细
2. 注重可迁移性
3. 冷嘲国家队
