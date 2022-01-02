import webbrowser
import datetime
import pyjokes
import wikipedia

from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForQuestionAnswering



class bot:
    def __init__(self):
        self.model = AutoModelForQuestionAnswering.from_pretrained("./roberta_ver2/")
        self.tokenizer = AutoTokenizer.from_pretrained("./roberta_ver2")
        self.nlp = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def query(self, input):
        q = input.lower()
        if ('start youtube' in q):
            webbrowser.open('https://www.youtube.com')
            return f'Starting youtube'
        elif ('start browser' in q):
            webbrowser.open('https://www.google.com')
            return f"starting browser"
        elif ('what time' in q):
            return self.query_time()
        elif ('what day' in q):
            return self.query_day()
        elif ('what is' in q or 'who is in q'):
            ans = self.get_answer(q)
            return ans
        elif ('hello' in q):
            return self.whatups()
        elif ('a joke' in q):
            return self.joke()

    def query_day(self):
        day = datetime.date.today()
        print(day)
        weekday = day.weekday()
        print(weekday)
        map = {
            0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday'
            }
        try:
            return  f'Today is {map[weekday]}'
        except:
            pass


    def query_time(self):
        time = datetime.datetime.now().strftime("%I:%M:%S")
        return f"{time[0:2]} o'clock and {time[3:5]} minutes"

    def whatups(self):
        return '''Hola, I am Hannah. I am your personal assistant.
        How may i help you?
        '''
    def joke(self):
        joke = pyjokes.get_joke(language="en", category="neutral")
        return joke

    def get_answer(self, question):
        question = question.lower()
        if "what is" in question:
            keyword = question[8:]
        elif "who is" in question:
            keyword = question[7:]
        if "birthday" in keyword:
            keyword = keyword[:-9]
        # print(keyword)
        context = self.get_context(keyword)
        # print(context)
        return self.getanswer(question, context)["answer"]

    def getanswer(self, input, context):
        QA_input = {
            'question': input,
            'context': context
        }
        res = self.nlp(QA_input)
        return res

    def get_context(self, input):
        searched = wikipedia.search(input, results=2, suggestion=False)
        # print(searched)
        context = wikipedia.summary(searched[0], auto_suggest=False)
        return context