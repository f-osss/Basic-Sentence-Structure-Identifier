import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def identify_parts_of_speech(sentence):
    words = nltk.word_tokenize(sentence)

    pos_tags = nltk.pos_tag(words)

    for word, pos in pos_tags:
        print(f"{word}: {pos}")



def main():
    sentence = input("Enter a sentence: ")

    identify_parts_of_speech(sentence)


if __name__ == "__main__":
    main()