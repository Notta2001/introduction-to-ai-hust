from load_model import getanswer
context = "The US has passed the peak on new coronavirus cases, " \
          "President Donald Trump said and predicted that some states would reopen this month. " \
          "The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world."

question = "What was President Donald Trump's prediction?"
ans = getanswer(question, context)
print(ans['answer'])