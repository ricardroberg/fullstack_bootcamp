import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not not the other!'

# for pattern in patterns:
#     print(f"I'm searching for {pattern}")
#
#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

match = re.search('term1', text)

print(type(match))  # <class 're.Match'>
print(match.start())  # 22 - indice onde inicia o termo
print(match.end())  # 27 - indice onde termina o termo


split_term = '@'
email = 'user@email.com'

print(re.split(split_term, email))  # ['user', 'email.com']

print(re.findall('match', 'test phrase match in match middle'))  # ['match', 'match']

####

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd*']  # 0 ou mais
test_patterns2 = ['sd+']  # 1 ou mais
test_patterns3 = ['sd?']  # 0 ou 1
test_patterns4 = ['sd{3}']  # seguido de 3
test_patterns5 = ['sd{2,3}']  # seguido de 2 a 3
test_patterns6 = ['s[sd]+']  # busca 1 ou mais S ou D

multi_re_find(test_patterns, test_phrase)  # ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd']
multi_re_find(test_patterns2, test_phrase)  # ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']
multi_re_find(test_patterns3, test_phrase)  # ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']
multi_re_find(test_patterns4, test_phrase)  # ['sddd', 'sddd', 'sddd', 'sddd']
multi_re_find(test_patterns5, test_phrase)  # ['sddd', 'sddd', 'sddd', 'sddd']
multi_re_find(test_patterns6, test_phrase)  # ['sdsd', 'sssddd', 'sdddsddd', 'sds', 'ssssss', 'sddddd']

test_phrase2 = 'This is a string! But is has punctuation. How can we remove it?'
test_patterns7 = ['[^!;?]+']
test_patterns8 = ['[a-z]+']
test_patterns9 = ['[A-Z]+']

multi_re_find(test_patterns7, test_phrase2)  # ['This is a string', ' But is has punctuation. How can we remove it']
multi_re_find(test_patterns8, test_phrase2)  # ['his', 'is', 'a', 'string', 'ut', 'is', 'has', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']
multi_re_find(test_patterns9, test_phrase2)  # ['T', 'B', 'H']

###

test_phrase3 = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns10 = [r'\d+']  # only numbers
test_patterns11 = [r'\D+']  # only strings
test_patterns12 = [r'\s+']  # spaces
test_patterns13 = [r'\S+']  # non spaces
test_patterns14 = [r'\w+']  # alphanumerics
test_patterns15 = [r'\W+']  # non alphanumerics

multi_re_find(test_patterns10, test_phrase3)  # ['12312']
multi_re_find(test_patterns11, test_phrase3)  # ['This is a string with numbers ', ' and a symbol #hashtag']
multi_re_find(test_patterns12, test_phrase3)  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
multi_re_find(test_patterns13, test_phrase3)  # ['This', 'is', 'a', 'string', 'with', 'numbers', '12312', 'and', 'a', 'symbol', '#hashtag']
multi_re_find(test_patterns14, test_phrase3)  # ['This', 'is', 'a', 'string', 'with', 'numbers', '12312', 'and', 'a', 'symbol', 'hashtag']
multi_re_find(test_patterns15, test_phrase3)  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']
