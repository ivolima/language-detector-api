#!/Users/Ivo/.virtualenvs/time4fun/bin/python
from flask import Flask, jsonify, request
from languagedetector import LanguageDetector

app = Flask(__name__)
my_detector = LanguageDetector()

history = [
            {
                'id': 1,
                'content': u'Buy groceries',
                'language': u'english'
            },
            {
                'id': 2,
                'content': u'Need to find a good Python tutorial on the web',
                'language': u'english'
            }
          ]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/nlp/api/v1.0/lang', methods=['POST'])
def guess_language():
        if not request.json or not 'content' in request.json:
            abort(400)
        try:
            result, query_ = my_detector.guessLanguage(unicode(request.json['content']))
        except:
            result = {'error': 0}

        query = {
                'id': history[-1]['id'] + 1,
                'content': request.json['content'],
                'language': min(result, key=result.get)
                }
        history.append(query)
        return jsonify({'query': query}), 201

if __name__ == '__main__':
    app.run(debug=True)
