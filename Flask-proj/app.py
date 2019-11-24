import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from model_utils import predict_sequence
from pickle import load

app = Flask(__name__)


##################################################################################

ENG_WORD_TOKENIZER = load(open('word-pickles/engtokenizer.pkl', 'rb'))
HIN_WORD_TOKENIZER = load(open('word-pickles/hintokenizer.pkl', 'rb'))


INDEX_TO_HIN_WORD = {i: word for word, i in HIN_WORD_TOKENIZER.word_index.items()}

HIN_VOCAB_SIZE_WORD = len(HIN_WORD_TOKENIZER.word_index) + 1

########################################################################################

ENG_SENT_TOKENIZER = load(open('sentences-pickles/engsenttokenizer.pkl', 'rb'))
HIN_SENT_TOKENIZER = load(open('sentences-pickles/hinsenttokenizer.pkl', 'rb'))

INDEX_TO_HIN_WORD_SENT = {i: word for word, i in HIN_SENT_TOKENIZER.word_index.items()}

HIN_VOCAB_SIZE_SENT = len(HIN_SENT_TOKENIZER.word_index) + 1

#########################################################################################

ENG_MAX_LEN = 12

HIN_MAX_LEN = 14


def loadmodel():
    #words
    global model
    model = load_model('models/nmt9.hdf5')
    #sentences
    global model1
    model1 = load_model('models/nmt18.hdf5')

    global graph
    graph = tf.get_default_graph()

 

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        #print(request.json)

        english_sentence = request.json['data']
                
        eng_len = len(english_sentence.split())
        
        if  eng_len == 1:
            
            print("Word")
            with graph.as_default():
                hin_translation = predict_sequence(model, ENG_WORD_TOKENIZER, HIN_WORD_TOKENIZER, ENG_MAX_LEN-1, HIN_MAX_LEN-1, INDEX_TO_HIN_WORD, english_sentence, HIN_VOCAB_SIZE_WORD)
            return jsonify(translation=hin_translation)

        else:
            print("Sentence")
            with graph.as_default():
                hin_translation = predict_sequence(model1, ENG_SENT_TOKENIZER, HIN_SENT_TOKENIZER, ENG_MAX_LEN, HIN_MAX_LEN, INDEX_TO_HIN_WORD_SENT, english_sentence, HIN_VOCAB_SIZE_SENT)
            return jsonify(translation=hin_translation) 

    return render_template('nmt.html')


if __name__ == "__main__":
    loadmodel()
    app.run(debug=True)
