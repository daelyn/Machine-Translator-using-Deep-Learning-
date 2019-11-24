import numpy as np
from keras.preprocessing.sequence import pad_sequences


def encode_sequences(tokenizer, length, lines):

    x = tokenizer.texts_to_sequences(lines)

    x = pad_sequences(x, maxlen=length, padding='post')

    return x


def predict_sequence(model, eng_tokenizer, hin_tokenizer, eng_max_len,
                     hin_max_len, index_to_hin_word, eng_line, hin_vocab_size):

    eng_seq = encode_sequences(eng_tokenizer, eng_max_len, [eng_line])

    hin_words = ['ssss']

    for i in range(hin_max_len - 1):

        hin_seq = encode_sequences(hin_tokenizer, hin_max_len - 1, hin_words)

        pred = model.predict([eng_seq, hin_seq])

        index = np.argmax(pred[0, i])

        hin_word = index_to_hin_word[index]

        if hin_word == 'eeee':
            break

        line = hin_words[0] + ' ' + hin_word

        hin_words[0] = line

    return ' '.join(hin_words[0].split()[1:])
