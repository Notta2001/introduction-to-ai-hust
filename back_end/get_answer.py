from load_model import getanswer
from get_context import get_context

"""context = "The US has passed the peak on new coronavirus cases, " \
          "President Donald Trump said and predicted that some states would reopen this month. " \
          "The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world."

question = "Who is the president?"

question = "What is binary search tree"

question = question.lower()
if "what is" in question:
    keyword = question[8:]
    print(keyword)
context = get_context(keyword)
print(context)
ans = getanswer(question, context)
print(ans["answer"])
"""
def get_answer(question):
    question = question.lower()
    keyword = question
    if "what is" in question:
        keyword = question[8:]
    elif "who is" in question:
        keyword = question[7:]
    if "birthday" in question:
        keyword = keyword[:-9]
    #print(keyword)
    context = get_context(keyword)
    #print(context)
    return getanswer(question, context)["answer"]

#print(get_answer("What is Leonardo DiCaprio birthday"))