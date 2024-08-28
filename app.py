from flask import Flask, render_template, request
import sqlite3

class FlaskManager:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/submit', 'submit', self.submit, methods=['POST'])
        self.database_path = 'instance/quiz.db'
        self.scores = set()

    def get_db_connection(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def index(self):
        conn = self.get_db_connection()
        questions = conn.execute('SELECT * FROM Question').fetchall()
        conn.close()
        return render_template('index.html', questions=questions)

    def submit(self):
        conn = self.get_db_connection()
        questions = conn.execute('SELECT * FROM Question').fetchall()
        conn.close()

        answers = request.form.to_dict()
        score = 0
        total_questions = len(questions)

        for question in questions:
            correct_option = question['correct_option']
            selected_option = answers.get(f'question_{question["id"]}')
            if selected_option == correct_option:
                score += 1

        score = (score / total_questions) * 100
        self.scores.add(score)
        return render_template('index.html', questions=questions, 
                               best_score=max(self.scores), 
                               current_score = score)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

if __name__ == '__main__':
    app = FlaskManager()
    app.run(debug=True)