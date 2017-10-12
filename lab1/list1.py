# -*- coding: utf-8 -*- 
# 1. 
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):
  count = 0
  for word in words:
  	if len(word) > 2 and word[0] == word[len(word) - 1]:
  		count += 1;
  		pass
  	pass
  return count


# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
	xlist = list(filter(lambda word: word[0] == 'x', words))
	xlist.sort()
	words.sort()
	xlist = xlist + list(filter(lambda word: word[0] != 'x', words))

  	return xlist


# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


# test()


if __name__ == '__main__':
  # main()
	print(me(['abbbba', 'abbbba', 'abbbba', 'abbbbb', 'aaa', 'aa', '333', 'yuiiy']))
	print(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']))
	print()