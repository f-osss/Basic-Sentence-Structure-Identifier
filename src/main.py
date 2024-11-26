import ssl
import nltk
# nltk.download()

# # Disable SSL certificate verification (use with caution)
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#

# Attempt to download NLTK resources
try:
    nltk.download('punkt', download_dir='.')
    nltk.download('averaged_perceptron_tagger', download_dir='.')
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")
    print("Please try manual download or check your internet connection.")

def identify_parts_of_speech(sentence):
    try:
        words = nltk.word_tokenize(sentence)

        pos_tags = nltk.pos_tag(words)


        for word, pos in pos_tags:
            print(f"{word}: {pos}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure NLTK resources are properly downloaded.")

def main():
    sentence = input("Enter a sentence: ")

    identify_parts_of_speech(sentence)

if __name__ == "__main__":
    main()