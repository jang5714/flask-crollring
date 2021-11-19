import csv
import re
import time
import kss
from icecream import ic
from selenium import webdriver
from bs4 import BeautifulSoup
from nltk import word_tokenize, FreqDist
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from konlpy.tag import Okt
from konlpy.tag import Komoran
import numpy as np
from collections import Counter
import pandas as pd
from apyori import apriori





path = 'C:\\Users\\bitcamp\\____\\jarvis\\crolling\\data'
chromdriver = 'C:\\Users\\bitcamp\\____\\jarvis\\crolling\\data\\chromedriver.exe'


class MySelenium(object):
    def __init__(self):
        self.driver = webdriver.Chrome(chromdriver)

    def velog(self):
        komoran = Komoran()
        driver = self.driver
        contents = []
        driver.get('https://velog.io/@turtle_dev/%EC%9D%BC%EA%B8%B0-9')
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        blog = soup.find_all('p')
        [[contents.append(p.string) for p in i] for i in blog]
        print(contents)
        dict = {'sentents': contents }
        df = pd.DataFrame(dict)
        df.to_csv('sentence2.csv', index=False)
        # with open(f'{path}blog2.csv', 'w', newline='', encoding='UTF-8') as f:
        #     wr = csv.writer(f)
        #     wr.writerow(contents)
        # driver.close()

    def blog_wordcloud(self):
        with open('datablog2.csv', 'r', encoding='UTF-8') as f:
            full_texts = f.read()
        clean_words = []
        line_remove = full_texts.replace('\n','')
        okt = Okt()
        tokenizer = re.compile(r'[^ ㄱ-힣,a-zA-Z]')
        tokenizer_text = tokenizer.sub('', line_remove)
        sentence = kss.split_sentences(tokenizer_text)
        ic(sentence[0])
        for i, document in enumerate(sentence):
            clean_words =[]
            for word in okt.pos(document, stem=True):
                if word[1] in ['Noun', 'Verb']:
                    clean_words.append(word[0])
        # print(clean_words)
        document = ' '.join(clean_words)
        # print(document)
        count = Counter(clean_words)
        toptxt = count.most_common(10)
        available = Counter({x: count[x] for x in count if x != '하다'})
        ava = Counter({x: available[x] for x in available if len(x) > 1})
        # ic(ava)
        ac = available.most_common(10)
        # t_data = np.array([tokenizer])
        # for word in okt.pos(tokenizer_text, stem=True):
        #     if word[1] in ['Noun','Verb']:
        #         clean_words.append(word[0])
        # x_data = np.array([clean_words])
        # document = ' '.join(clean_words)

        # Punctuation, Adjective, Josa, KoreanParticle

    def text_cleaning(self, text):
        hangul = re.compile(r'[^ ㄱ-힣]')
        result = hangul.sub('', text)
        return result
    def get_nouns(self, text):
        nouns_tagget = Okt()
        nouns = nouns_tagget.nouns(text)
        # 한글자 제거
        nouns = [noun for noun in nouns if len(noun) > 1]
        return nouns

    def apriori_execute(self):
        df = pd.read_csv("sentence2.csv")
        df = df.dropna(axis=0)
        df2 = df.copy()
        df2['sentents'] = df2['sentents'].apply(lambda x : self.text_cleaning(x))
        df2.head()
        # ic(df2)

        df2['sentents'] = df2['sentents'].apply(lambda x: self.get_nouns(x))
        # ic(df2)
        transactions = df2['sentents'].tolist()
        transactions = [transaction for transaction in transactions if transaction]  # 공백 문자열을 방지합니다.
        print(transactions)
        results = list(apriori(transactions,
                               min_support=0.06,
                               min_confidence=0.05,
                               min_lift=1.0,
                               max_length=2))
        ic(results)
        columns = ['source', 'target', 'support']
        network_df = pd.DataFrame(columns=columns)
        for result in results:
            if len(result.items) == 2:
                items = [x for x in result.items]
                row = [items[0], items[1], result.support]
                series = pd.Series(row, index=network_df.columns)
                network_df = network_df.append(series, ignore_index=True)

        corpus = "".join(df2['sentents'].tolist())
        print(corpus)


if __name__ == '__main__':
    sel = MySelenium()
    sel.apriori_execute()
    # sel.velog()

