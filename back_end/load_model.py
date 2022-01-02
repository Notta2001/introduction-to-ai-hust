from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForQuestionAnswering


#model = AutoModelForQuestionAnswering.from_pretrained("./distillbert/")
model = AutoModelForQuestionAnswering.from_pretrained("./roberta_ver2/")
tokenizer = AutoTokenizer.from_pretrained("./roberta_ver2")
#tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def getanswer(input, context):
    QA_input = {
        'question': input,
        'context': context
    }
    res = nlp(QA_input)
    return res



