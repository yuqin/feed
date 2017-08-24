# coding: utf-8
# __author__: u"Yuqin"
"""
这里存放数据预处理的内容, 也就是ETL部分
数据清洗根据不同的数据源有多种pipeline (class为单位), 每个pipeline都有好几步 (function为单位),
"""
from abc import abstractmethod
from helpers import *
#import jieba
#import jieba.analyse
from optparse import OptionParser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

class BaseETL(object):
    """
    抽象类
    每个继承BaseETL的类都需要Override [extract, transform, load] 这三个方法
    :return:
    """
    def __init__(self,file_name,data,cleaned):
        self.file_name = ""
        self.data = None
        self.cleaned = False
        self.list=[]

    @abstractmethod
    def extract(self):
        """
        数据抽取层, 文件读操作
        :return:
        """
        pass

    @abstractmethod
    def transform(self):
        """
        数据转换层、筛选、插值、标准化等操作
        :return:
        """
        pass

    @abstractmethod
    def load(self):
        """
        数据输出层, 文件写操作
        :return:
        """
        pass

    def etl(self, file_name):
        self.file_name = file_name
        self.extract()
        self.transform()
        self.load()
        return

class DocContentETL(BaseETL):
    """
    清洗data.csv文件，将文档内容向量化，创建标签
    """
    def __init__(self,file_name,data,cleaned):
        BaseETL.__init__(self,file_name,data,cleaned)

    def extract(self):
        self.data=read_data_set(self.file_name,self.cleaned)
        return
    def transform(self):
        """
        1.nlp相关，将文章内容转化成向量
        :return:
        """
        tags = jieba.analyse.extract_tags(doc_content_1, topK=5, withWeight=1)
        for tag in tags:
           print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
        return
    def load(self):
        save_data_set(self.data, self.file_name)
        return

class User_clickETL(BaseETL):
    """
    提取测试集中y的数据
    """
    def __init__(self,file_name,data,cleaned):
        BaseETL.__init__(self,file_name,data,cleaned)

    def extract(self):
        """
        打开train.csv数据集
        :return:
        """
        with open("train.csv", "rb") as csvfile:
            for row in csvfile:
                user_id = re.split(r'\t', row)[0].decode('gb18030')
                doc_id = re.split(r'\t', row)[1].decode('gb18030')
                user_click1 = re.split(r'\t', row)[2].decode('gb18030')
                m=re.match(r"(\d+)", user_click1)
                user_click=m.group(1)
                self.list.append({"user_id": user_id, "doc_id": doc_id, "user_click": user_click})
            return self.list
    def transform(self):
        """
        :return:
        """
        return
    def load(self):
        save_data_set(self.data, self.file_name)
        return


#df=User_clickETL("train.csv",None,False)
#df1=df.extract()
#df1=pd.DataFrame(df1)
#print df1["user_click"]
df=read_data_set(get_file_path("data.csv",cleaned=False))
df1=pd.DataFrame(df)
corpus=df1["doc_content"][1:4].tolist()
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
m=pd.DataFrame(X.toarray())
print m