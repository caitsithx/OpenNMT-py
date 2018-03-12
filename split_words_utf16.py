s = """Chinese (汉语/漢語 Hànyǔ or 中文 Zhōngwén) is a group of related
        language varieties, several of which are not mutually intelligible,"""
us = u"""Chinese (汉语/漢語 Hànyǔ or 中文 Zhōngwén) is a group of related
        language varieties, several of which are not mutually intelligible,"""
import codecs

SOURCE_FILE = 'gy2/test.zh'
TGT_FILE = SOURCE_FILE + '.split'

#print(''.join(c for c in s.decode('utf-8') if u'\u4e00' <= c <= u'\u9fff'))

print(''.join(c for c in s if u'\u4e00' <= c <= u'\u9fff'))

with codecs.open(SOURCE_FILE, 'r', 'utf-16-le') as f:
    text = f.readlines()
    text = [line.strip() for line in text]
print(text[:10])

split_text = []
for line in text:
    newline = ''
    for i, c in enumerate(line):
        if u'\u2000' <= c <= u'\u9fff':
            if i > 0 and not (u'\u2000' <= line[i-1] <= u'\u9fff'):
                newline += ' ' + c + ' '
            else:
                newline += c + ' '
        else:
            newline += c
    split_text.append(newline)

with open(TGT_FILE, 'w') as f:
    for line in split_text:
        f.write(line.strip() + '\n')
