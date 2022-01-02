import webbrowser
import datetime
import pyjokes
from get_answer import get_answer

class bot:
    def query(self, input):
        q = input.lower()
        if ('start youtube' in q):
            webbrower.open('https://www.youtube.com')
            return f'Starting youtube'
        elif ('start browser' in q):
            webbrowser.open('https://www.google.com')
            return f"starting browser"
        elif ('what time' in q):
            return query_time()
        elif ('what day' in q):
            return query_day()
        elif ('what is' in q or 'who is in q'):
            ans = get_answer(q)
            return ans
        elif ('a joke' in q):
            return joke()

    def query_day():
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


    def query_time():
        time = datetime.datetime.now().strftime("%I:%M:%S")
        return f"{time[0:2]} o'clock and {time[3:5]} minutes"

    def watups():
        return '''Hola, I am Hannah. I am your personal assistant.
        How may i help you?
        '''
    def joke():
        joke = pyjokes.get_joke(language="en", category="neutral")
        return joke