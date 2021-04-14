# Aid-to-the-Names-and-Surnames-of-Western-Literati
西儒名姓资<br>

按：名称戏仿《西儒耳目资》，参见[Nicolas Trigault - Wikipedia](https://en.wikipedia.org/wiki/Nicolas_Trigault#Publications)

详情可参：[附录（二）：汉学家汉名表](https://mp.weixin.qq.com/s/K9qDpcOuWXKXCNDebQQP_Q)。



## 数据来源（预处理）

### Chinese Names of Western Scholars
A directory compiled and maintained by Philip Clart 柯若樸 (University of Leipzig)
~~[链接在这里](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.htm)~~
按：这个链接一段时间内是2017年更新的，国内网络上流传的链接似乎是这个。<br>
然而，柯若朴教授所保持更新的链接则是html结尾的：[链接](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.html)
所以，我的一些结果需要重做。（2021-3-10）<br>
有空了我会慢慢考订的。

2021-04-14 更新爲“7 April 2021”版本。

data文件夹中，名为`PhilipClart.csv`的文件是复制自该网页然后用Excel转存的。

使用`PhilipClart-csv2csv.py`将csv文件输出到`PhilipClart-output.txt`。具体可以自己看代码。

很多不统一的地方是我人肉一个一个调的，尤其是全角半角字符的问题。

其中，有的学者没有“姓氏”（系佛家子弟），为了保证体例统一，在其洋文姓一栏录为“Shi”，中文名录为“释·某某”，以区别于原来就有的“释”姓。

> 当然，“印顺”大师带有“释”字的名字也较为通用。

### English/Chinese Comparison Table for Names of Chinese Studies Scholars
### 北美中国研究学者英中姓名对照
> Zhang, Haihui and Xue, Zhaohui and Jiang, Shuyong and Lugar, Gary Lance (2013) English/Chinese Comparison Table for Names of Chinese Studies Scholars [ 北美中国研究学者英中姓名对照 ]. In: A Scholarly Review of Chinese Studies in North America = 北美中国研究综述. Association for Asian Studies (AAS). ISBN 978-0-924304-72-9
Last updated: 16 November 2017

这里使用的是[该页面](http://d-scholarship.pitt.edu/17682/PDF)“As of October 12, 2020”的一版pdf。

~~我已经把pdf文件偷过来放在了data文件夹下。然后使用福昕PDF编辑器转成docx，然后复制粘贴到txt。后缀为plain的删掉了开头的介绍。~~

~~其中`List*`几个文件就是辗转转换的原文件。然后主要的调整都是在`HaihuiZhang.txt`中做的。包括但不限于：~~

1. 将“又作”、“又译作”、“又名”、“亦名”、“号某某”、“也作”等等统一（因此不细分）。
2. 删除von、van导致的两见，只保留von在姓中的一种情况。
3. 把部分空格改成tab
4. 调整全角半角

然后通过`HaihuiZhang-txt2csv.py`输出成后缀为txt但实为csv的output。

## 工作流（去重工作）

1. 在上述准备之后，合并三个不同来源的文件内容
2. 将洋名和汉名组成字符串，如果仍然被判定为重复行，则认为重复无疑
3. 去掉其中多余的行，然后在“加权计数”一列记录一个数值（`重复行数 * 10 + OMG1中的所见次数`），这样个位数保留原来我的计数，十位数表示数据来源数量）
4. 输出在如是去重之后基于简体字汉名仍可判定为重复的各行（第一步完）
5. 人肉阅读这些行，根据异文进行校对（发现了一些错误，也发现了一些疑似重名的学者）
6. 遵循~~宁可信其有~~说有易，说无难的原则，将疑似重名的学者分别命名为某某A、某某B。
7. (第二步开始)基于修改之后的OMG6,重复第一步的操作,最后基于简体字的汉名去重,分别保留第一次出现和最后一次出现的"名字",然后将后者附于前者"异文"列,然后与完全不包含重复行的数据合并.
8. 生成OMG7.

### 还需要润色

- [ ] **把原數據換成2021年更新的，而不是2017年更新的**
- [x] 删除部分文件，出于尊重版权的考虑（2021-03-31）
- [x] 进一步删除某些来源的资料，但给出：1. 校勘记 2. 批处理脚本
- [x] 然後重新做一遍（因爲一些疏失沒有用最新的Philip Clart先生的資料）
- [ ] ~~去掉缺值补〇~~
- [ ] 调整文件字体
- [ ] 重排顺序
- [x] 去掉此前忘记strip而留下的空格
- [x] 修改Readme的病句和不小心使用的英文标点

## 依赖

如果有哪位闲的无聊，想看看代码的话，那我只能说依赖Python的OpenCC，记得装。
``` pip install opencc```

其中用到了pandas和numpy，都是临时抱佛脚百度搜代码，好剿袭不求甚解，为此感谢互联网的共享精神。

# 真-依赖

**在此需要郑重地感谢柯若樸先生在网站上公开的电子表格**<br>

我今天（2021-03-09）给Philip Clart先生写了邮件，先生表示并不主张版权（爱了爱了爱了❤），并表示会在下次更新时更正几个typos。<br>
大佬人真好；这里是大佬个人主页，有空多去踩踩：[Philip Clart](https://home.uni-leipzig.de/clartp/)

（2021-04-14）Clart先生前不久修正了幾個typos，今天有空重新理了一邊。所做的工作包括：
- 從網站複製，粘貼到Excel
- 從Excel另存爲csv
- 在佛家子弟名字前妄加“釋”字（並加間隔號“·”以示區別）
- 在兩個沒有逗號的地方添加了逗號隔開姓氏與名字
- 簡單修改此前的py文件，重新輸出output
- 此外，僅保留Haihui Zhang先生異於柯若樸先生的部分，其他部分已盡量刪除，容后細勘

## Chinese Names of Western Scholars & Western Names of Chinese Scholars

Just too lazy to write an En version.

> This listing aims to facilitate communication between Western and Asian China-scholars. As anyone who has attended a bi- or multilingual conference can attest, some amount of confusion is occasioned by the fact that Western sinologists are usually known in Chinese-speaking academia primarily by their Chinese names. As the latter, however, are not in common use in Western academic circles, it often takes a while to figure out that, for example, the professor Du Zanqi 杜贊奇, whom a Chinese conference participant keeps citing, is in fact better known in the English-speaking world as Prasenjit Duara.<br>
> [柯若樸](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.htm)

目标一致，只不过想：
1. 著录更加详细
2. 注重可迁移性
3. ~~冷嘲国家队~~
