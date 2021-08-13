import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
# import fileupload
import io
import sys

def calculate_frequencies():
    # Here is a list of punctuations and uninteresting words you can use to process your text
    file_contents = input()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    frequencies = {}
    kept = []
    for mark in punctuations:
        file_contents = file_contents.replace(mark, '')
    for word in uninteresting_words:
        file_contents = file_contents.replace(' ' + word + ' ', '')
    for word in file_contents.split():
        if word.lower() not in kept:
            kept.append(word.lower())
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    #   return cloud.to_file("myfile.jpg")
    return cloud.to_array()

myimage = calculate_frequencies()
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()