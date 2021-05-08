# Aid-to-the-Names-and-Surnames-of-Western-Literati
西儒名姓资<br>

按：名称戏仿《西儒耳目资》，参见[Nicolas Trigault - Wikipedia](https://en.wikipedia.org/wiki/Nicolas_Trigault#Publications)


## 数据来源（预处理）

### Chinese Names of Western Scholars
A directory compiled and maintained by Philip Clart 柯若樸 (University of Leipzig)
[链接在这里](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.html)

#### 流

- data文件夹中，名为`PhilipClart.csv`的文件是复制自该网页然后用Excel转存的
- 使用`PhilipClart-csv2csv.py`将csv文件输出到`PhilipClart-output.txt`。具体可以自己看代码。

#### 细节调整

- 很多不统一的地方是我人肉一个一个调的，尤其是全角半角字符的问题
- 以及最近html中的表格对齐上有问题，调整起来颇为麻烦
- 其中，有的学者没有“姓氏”（系佛家子弟），为了保证体例统一，在其洋文姓一栏录为“Shi”，中文名录为“释·某某”，以区别于原来就有的“释”姓。（当然，“印顺”大师带有“释”字的名字也较为通用）

### English/Chinese Comparison Table for Names of Chinese Studies Scholars
### 北美中国研究学者英中姓名对照
> Zhang, Haihui and Xue, Zhaohui and Jiang, Shuyong and Lugar, Gary Lance (2013) English/Chinese Comparison Table for Names of Chinese Studies Scholars [ 北美中国研究学者英中姓名对照 ]. In: A Scholarly Review of Chinese Studies in North America = 北美中国研究综述. Association for Asian Studies (AAS). ISBN 978-0-924304-72-9
Last updated: 16 November 2017

这里使用的是[该页面](http://d-scholarship.pitt.edu/17682/PDF)“As of October 12, 2020”的一版pdf。

#### 流

- 我已经重新把pdf文件偷过来放在了data文件夹下。
- 然后使用福昕PDF编辑器转成docx
- 然后复制粘贴到txt。
- 后缀为plain的删掉了开头的介绍（开头的介绍是重要的）

#### 细节
其中`List*`几个文件就是辗转转换的原文件。然后主要的调整都是在`HaihuiZhang.txt`中做的。包括但不限于：

1. 将“又作”、“又译作”、“又名”、“亦名”、“号某某”、“也作”等等统一（因此不细分）。
2. 删除von、van导致的两见，只保留von在姓中的一种情况。
3. 把部分空格改成tab
4. 调整全角半角

然后通过`HaihuiZhang-txt2csv.py`输出成后缀为txt但实为csv的output。

### 还需要润色

- [ ] 保持更新，跟踪大佬更新进度
- [ ] 留存备份，方便将来git对比
- [ ] 静态网页
- [ ] gitee拷贝

## 依赖

如果有哪位闲的无聊，想看看代码的话，那我只能说依赖Python的OpenCC，记得装。
``` pip install opencc```

其中用到了pandas和numpy，都是临时抱佛脚百度搜代码，好剿袭不求甚解，为此感谢互联网的共享精神。

# 真-依赖

需要感谢数据来源：
> Zhang, Haihui and Xue, Zhaohui and Jiang, Shuyong and Lugar, Gary Lance (2013) English/Chinese Comparison Table for Names of Chinese Studies Scholars [ 北美中国研究学者英中姓名对照 ]. In: A Scholarly Review of Chinese Studies in North America = 北美中国研究综述. Association for Asian Studies (AAS). ISBN 978-0-924304-72-9

[链接](http://d-scholarship.pitt.edu/17682/)

> Chinese Names of Western Scholars
A directory compiled and maintained by
Philip Clart 柯若樸
University of Leipzig


[链接](https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.html)

这里是大佬个人主页，有空多去踩踩：[Philip Clart](https://home.uni-leipzig.de/clartp/)
