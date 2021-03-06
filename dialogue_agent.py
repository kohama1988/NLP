from os.path import join,dirname,normpath
import MeCab
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

class DialogueAgent:
    def __init__(self) -> None:
        self.tagger = MeCab.Tagger()
    
    def _tokenize(self, text):
        node = self.tagger.parseToNode(text)
        tokens = []
        while node:
            if node.surface != '':
                tokens.append(node.surface)
            node = node.next
        return tokens
    
    def train(self,texts,labels):
        vectorizer = CountVectorizer(tokenizer=self._tokenize)
        bow = vectorizer.fit_transform(texts)

        classifier = SVC()
        classifier.fit(bow,labels)
        self.vectorizer = vectorizer
        self.classifier = classifier
    
    def predict(self,texts):
        bow = self.vectorizer.transform(texts)
        return self.classifier.predict(bow)

if __name__ == '__main__':
    training_data = pd.read_csv('assets/dialogue_agent_data/training_data.csv')
    dialogue_agent = DialogueAgent()
    dialogue_agent.train(training_data['text'], training_data['label'])
    with open('assets/dialogue_agent_data/replies.csv') as f:
        replies = f.read().split('\n')
    input_text = '私の話聞いてる？'
    predictions = dialogue_agent.predict([input_text])
    predicted_class_id = predictions[0]

    print(replies[predicted_class_id])
