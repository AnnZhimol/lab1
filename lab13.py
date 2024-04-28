import pymorphy3
import nltk
from math import log
from nltk import ConditionalFreqDist, ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

morph = pymorphy3.MorphAnalyzer()

with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# извлечение токенов ("слов") из текста
tokens = word_tokenize(text.lower())

stop_words = stopwords.words("russian")
stop_words.extend(['т.д.', '.', ',', '"', '""', ':', ';', '(', ')', '[', ']', '{', '}', '-', 
                   '–', '|', '%', '•', '«', '»', '𝐴', '𝑆𝑖', '∈', 'ℕ', '𝑆𝑖', '𝑅𝑗', '|𝑖', '∈',
                     '𝑁𝑎𝑚𝑒', '𝑦', '𝑧', '𝛼', '=', '<', '𝛽'] + [str(i) for i in range(10)])
# удаление стоп слов
tokens = [word for word in tokens if word not in stop_words]

# кол-во существительных во множественном числе
kol = sum(1 for word in tokens if 'NOUN' in morph.parse(word)[0].tag and 'plur' in morph.parse(word)[0].tag)
print(f'кол-во существительных во множественном числе - {kol}')

# лемматизация (слова в канонической, основной форме)
lemmatize_tokens = [morph.parse(word)[0].normal_form for word in tokens]
lemmatize_tokens_str = " ".join(lemmatize_tokens)

bigrams = list(ngrams(lemmatize_tokens_str.split(), 2))
bigrams_fd = ConditionalFreqDist(bigrams)

summ_freq = sum(bigrams_fd[bigram[0]][bigram[1]] for bigram in bigrams)

res = {}
for bigram in bigrams:
    a = bigrams_fd[bigram[0]][bigram[1]]  # частотность биграмы
    b = sum(bigrams_fd[b_[0]][b_[1]] for b_ in bigrams if bigram[0] == b_[0] and bigram[1] != b_[1])
    c = sum(bigrams_fd[b_[0]][b_[1]] for b_ in bigrams if bigram[0] != b_[0] and bigram[1] == b_[1])
    d = summ_freq - a
    
    res[bigram] = (a * log(a + 1) + b * log(b + 1) + c * log(c + 1) + d * log(d + 1) - (a + b) * log(a + b + 1) -
                   (a + c) * log(a + c + 1) - (b + d) * log(b + d + 1) - (c + d) * log(c + d + 1) +
                   (a + b + c + d) * log(a + b + c + d))

# сортировка биграм по значению Log-Likelihood
sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)

print('Топ-10 наиболее статистически значимых биграмм: ')
for item in sorted_res[:10]:
    print(item)