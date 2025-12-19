#keyword to search
keyword= input(" Enter the Keyword Or Phrase To Search ").lower().strip(",!") 

with open("text.txt") as file :
    data= file.read().lower().strip(",!")

    # break the Data of file into sentences 
    list_of_sentences=data.split(".")
    relevanceScoreDict={}
    keyword_count=0
    # search the keyword in different sentences ---

    for sentence in list_of_sentences:
        if keyword in sentence:
            sentence=sentence.strip(" ,!\n")#cleaning sentencing (removing punctuations)
            # Calculate relvance Score
            keyword_count+= sentence.count(keyword)
            curr_keyword_count=sentence.count(keyword)
            total_words= len(sentence.split())
            relevanceScore=curr_keyword_count/total_words

            # stroing relevance score in dictionary
            relevanceScoreDict[sentence]=relevanceScore
    
    # Rank the sentences based on relevance score
    sorted_relevanceScoreDict=sorted(relevanceScoreDict.items(), key= lambda item: item[1], reverse=True)

    if keyword_count!=0:
        print(f"{keyword} found : YES ")
        print(f" Occurrences : {keyword_count}")
        print(f" Sentences in which it was Found with their relevence score ")
        for sentence,score in sorted_relevanceScoreDict:
            print(f"{sentence} :: SCORE :{score} ")
    
    else:
        print(f"{keyword} does not found")
