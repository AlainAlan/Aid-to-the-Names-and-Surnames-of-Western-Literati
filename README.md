# Aid-to-the-Names-and-Surnames-of-Western-Literati
西儒名姓资<br>

按：名称戏仿《西儒耳目资》，参见[Nicolas Trigault - Wikipedia](https://en.wikipedia.org/wiki/Nicolas_Trigault#Publications)

一个可供浏览器检索的版本（科学上网required）：
[西儒名姓资](https://alainalan.github.io/Aid-to-the-Names-and-Surnames-of-Western-Literati/)

关于该网页的按语：
1. 懒得学html和css，胡乱弄出一个页面，供且仅供在线查找（也便于更新维护），较于csv、xlsx有一定优势；
2. 在主流桌面浏览器中，搜索`Goran`可匹配到`Göran`，而在excel中则未必然，这也是在线的优势之一，省去了我去掉diacritical的工作，也简化了页面；
3. 以后再说。

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
- [x] 静态网页
- [ ] 把网页整好看点，现在丑死了
- [ ] css适配水果（参考[iOS Fonts](http://www.iosfonts.com/)）
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

## 又臭又长的更新日志

### 2021-07-01

数据来源已更新：
- 柯若朴：2021-06-19更新
- 张海惠：2021-05-05更新（已备份到data文件夹，可参）

柯若朴20210619与上一版diff结果：
```
Choi, Chi Cheung	蔡志祥
Cohen, Jerome Alan	孔傑榮 / 柯恩	删了一个空格
Collie, David	柯大衛 / 高大衛 / 顧利
Guan, Zengjian	關增建
Hall, David L.	郝大為 / 郝大維	（增加第二个译名）
Herrmann, Konrad	赫爾曼
Hillier, Charles Batten	禧利 / 奚禮爾
Hughes, E.R.	修中誠
Ing, Michael David Kaulana	吳榮桂
King, Chien-kün	經乾堃
Ku, Hung Ming	辜鴻銘
Lyall, Leonard A.	賴發洛
Marshman, Joshua	馬士曼 / 馬殊曼
Moran, Patrick Edwin	莫然
Morrison, Robert	馬禮遜
Schachter, Bony B.	羅逸	（删除）
Seaman, Gary	沈雅禮 / 蓋西曼
Shepherd, Eric	謝博德
```

由于从网页复制表格存在一些问题（也为了省事，不想重新按自己的需要校订一遍），我没有整体重做数据，而是直接把上面的diff粘贴在末尾（omg我发现我忘了修改和删除了，只是粘贴在最后，那么下次再改正吧）

使用Word比较了张女士的修订前后的表格，发现除了一些细小的勘误之外，尚有：

- Sena, David	孙大卫	改为	孙大维


根据两位（在邮件中所表示）的意思，我们可以近似地认为这些资料采用CC 4.0许可，虽然张女士对credit的主张更明确一些。因此我也求了“差”，以示区别。

对于学者而言，“经营”这种表格一般都不会是为了谋利，读过任何一本科学社会学导论类书籍都会知道默顿是怎么说的——虽然我不曾读过[默顿](https://book.douban.com/subject/1028800/)。所以如果有人翻到了我整理的这些数据，请在另行发布时注明数据来源：

- 柯若朴：https://home.uni-leipzig.de/clartp/ChineseNamesWesternScholars.html
- 张海惠：http://d-scholarship.pitt.edu/17682/

至于我本人，就没脸皮掠美了。

本次具体的工作流程可见代码如屎一般优雅的`OMG8toOMG9.ipynb`。

1. 将Clart新版diff之后，把新加入的部分放到原来的txt最后。
2. 转换HaihuiZhang新版pdf，统一“又作”，更正一些tab，使用全角括号，半角逗号。
3. 使用对应的py输出output。
4. 使用Excel把output合并为一个excel
5. 读取excel到ipynb，输出所有“汉名”重复的行，人工挑选出一些比较蹊跷的重复行（予以保留，等待考证），作为weird_dup
6. 去重后输出OMG9.xlsx
