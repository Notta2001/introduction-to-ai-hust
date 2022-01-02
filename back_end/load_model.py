from transformers import RobertaTokenizerFast
from transformers import pipeline
from transformers import AutoModelForQuestionAnswering

model = AutoModelForQuestionAnswering.from_pretrained('./roberta_finetuned')
tokenizer = RobertaTokenizerFast.from_pretrained("roberta-base")
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def getanswer(input, context):
    QA_input = {
        'question': input,
        'context': context
    }
    res = nlp(QA_input)
    return res



