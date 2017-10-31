#--------------------------------------------------------------------------------------------------
# Name:		wordcount
# Purpose:
# 
# Author: 	Saurabh Kumar
# 
# Created:	10/30/2017
# License: 	<your license>
#--------------------------------------------------------------------------------------------------

#import required libraries
import sys
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#function to calculate the wordcount
def wordcount(ip_file,ex_file):

    #Get the words from input file
    with open(ip_file) as f:
        words = f.read().lower().split()

    #Get the words from exclude input file
    with open(ex_file) as e:
        ex_words = e.read().lower().split()

    #Update the words which are not in exclude file
    words =[x for x in words if x not in ex_words]    

    #Get the wordcount dictionary 
    count_dict = Counter(words)
    count_dict_percent ={}
    count_sum = sum(count_dict.values())

    #print the wordcounts
    print 'word', '\t', 'count'
    
    for k,v in count_dict.items():
        print k,'\t',v


    #wordcloud function to display and save the wordcloud
    wordcloud = WordCloud(width=1000, height=500, max_words=2000, relative_scaling=1, normalize_plurals=False).generate_from_frequencies(frequencies= count_dict)
    wordcloud.to_file("wordcloud.png")
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    wordcount(sys.argv[1],sys.argv[2])
