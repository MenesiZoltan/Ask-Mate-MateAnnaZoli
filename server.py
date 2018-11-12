from flask import Flask, render_template, request
import data_manager
import data_manager
import connection
import time

app = Flask(__name__)

@app.route("/")
def route_list():
    questions = data_manager.show_questions_by_order(request.args.get('select_order'))
    return render_template('list.html', questions=questions)

@app.route("/ask-question", methods=["GET", "POST"])
def route_ask_question():
    if request.method == "GET":
        return "Niceű job"
    else:
        return "matéka meleg"

@app.route("/question/<id>")
def route_question(id):
    pass

@app.route('/question/<id>', methods=['POST'])
def route_question_add_answer(id):
    pass


@app.route("/answer/<answer_id>/delete/<id_>")
def route_delete_answer(answer_id, id_):
    pass


@app.route("/question/<id>/<vote>")
def route_question_voting(id, vote):
    pass


@app.route("/question/<id>/<vote>/<submission_time>")
def route_answer_voting(id, vote, submission_time):
    pass


@app.route("/question/<id>/edit", methods=["GET", "POST"])
def route_edit_question(id):
    pass


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
