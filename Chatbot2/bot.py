import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def qa_pairs(x):
    cpairs = re.findall(": (.*?)(?:$|\\n)", x)
    clist.extend(list(zip(cpairs[0::2], cpairs[1::2])))

def get_response(q):
    my_question = vectorizer.transform([q])
    cs = cosine_similarity(my_question,vec)
    rs = pd.Series(cs[0]).sort_values(ascending=False)
    rsi = rs.index[0]
    return convo_frame.iloc[rsi]['a']#print the closest answer


def main():
    pd.set_option('display.max_colwidth', 200)
    global convo_frame
    global vectorizer
    global vec

    df = pd.read_csv(r'data.csv', encoding='latin-1')
    df

    convo = df.iloc[:, 1]
    #print(convo)

    global clist
    clist = []

    convo.map(qa_pairs)
    convo_frame = pd.Series(dict(clist)).to_frame().reset_index()
    convo_frame.columns = ['q', 'a']


    vectorizer = TfidfVectorizer(ngram_range=(1, 3))

    vec = vectorizer.fit_transform(convo_frame['q'])

    #print(convo_frame)

    userQuestion = ""
    print("Hello! I am a Jerard! I learn from conversations!\n")
    print("Type 'exit' to leave!\n ")
    while(userQuestion!="exit"):
        userQuestion = input(">>: ")
        print(get_response(userQuestion))
    print("goodbye")

if __name__ == "__main__": main()
