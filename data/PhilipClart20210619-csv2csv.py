import opencc
from unicodedata import category, name, normalize
s2t = opencc.OpenCC('s2t.json')
t2s = opencc.OpenCC('t2s.json')

def rm(s):
	return ''.join(c for c in normalize('NFKD', s.replace('ø', 'o').replace('Ø', 'O').replace('⁻', '-').replace('₋', '-'))
					if category(c) != 'Mn')

# s = 'śḟēò'
# ss = rm(s)
# print(ss)

namelist = []

with open('Clart20210619.csv','r',encoding='utf8') as h:
	lines = h.readlines()
	for line in lines:
		if len(line) <= 2:
			continue
		en_comma_zh = line.strip().split(',')
		# 
		if len(en_comma_zh) == 2:
			if '(' in en_comma_zh[0]:
				# 如果在英文名里面有()
				en,env = en_comma_zh[0].split('(')
				en = en.strip()
				env = env.rstrip(')').strip()
			elif '/' in en_comma_zh[0]:
				en,env = en_comma_zh[0].split('/')
				en = en.strip()
				env = env.strip()
			else:
				en = en_comma_zh[0].strip()
				env = ''
			s_comma_n = en.split('，')
			if len(s_comma_n) < 2:
				print(s_comma_n)
				continue
			s = s_comma_n[0].strip()
			n = s_comma_n[1].strip()
			if '/' in en_comma_zh[1]:
				# 如果中文名里有（）
				zhvs = en_comma_zh[1].strip().split('/')
				# 似乎有多于两个的情况
				zh = zhvs.pop(0).strip()
				zhv = "、".join(zhvs)
			else:
				zh = en_comma_zh[1].strip()
				zhv = ''
			tr = s2t.convert(zh)
			sm = t2s.convert(zh)
			en_drmd = rm(en)
			env_drmd = rm(env)

			dict = {}
			dict['洋名'] = n + ' ' + s
			dict['洋姓'] = s
			dict['洋字'] = n
			dict['中名'] = zh
			dict['汉名'] = sm
			dict['漢名'] = tr
			dict['洋名又'] = env
			dict['中名又'] = zhv
			dict['洋名无音符'] = en_drmd
			dict['洋名又无音符'] = env_drmd
			namelist.append(dict)
		else:
			print(en_comma_zh)
			continue

with open('Clart20210619-output.txt','w',encoding='utf-8') as o:
	for names in namelist:
		o.write(names['洋名'] + ',' + names['洋姓'] + ',' + names['洋字'] + ',' + names['中名'] + ',' + names['汉名'] + ',' + names['漢名'] + ',' + names['洋名又'] + ',' + names['中名又'] + ',' + names['洋名无音符'].strip() + ',' + names['洋名又无音符'].strip() + '\n')
