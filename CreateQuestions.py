import json
import random

def getQuestions(numberOfQuestions):
    with open('bin.json', encoding='utf8') as f:
        words = json.load(f)
    
    questions = []
    
    ordflokkar = {
    'ao': 'atviksorð',
    'fn': 'fornafn',
    'hk': 'hvorugkynsnafnorð',
    'kk': 'karlkynsnafnorð',
    'kvk': 'kvenkynsnafnorð',
    'lo': 'lýsingarorð',
    'so': 'sagnorð'
    }
    
    for i in range(numberOfQuestions):
        word = words[random.randrange(len(words))]
        
        rightAnswer = ''
        wrongAnswers = []
        
        for key in ordflokkar:
            if key == word['ordfl']:
                rightAnswer = ordflokkar[key]
            else:
                wrongAnswers.append(ordflokkar[key])
        
        question = {
            'number' : i+1,
            'question' : 'Hvaða orðflokki tilheyrir orðið ' + word['uppflord'] + '?',
            'rightAnswer' : rightAnswer,
            'wrongAnswers' : wrongAnswers
        }

        questions.append(question)
    
    return questions
