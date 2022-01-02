import wikipedia

def get_context(input):
    searched = wikipedia.search(input, results = 2, suggestion = False)
    #print(searched)
    context = wikipedia.summary(searched[0], auto_suggest = False)
    return context

#print(get_context("Taylor Swift"))
#print(wikipedia.page(wikipedia.search("tom holland")[0]))
#print(wikipedia.suggest("Tom Holland"))