from flask import Flask, render_template, request, redirect
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
        return render_template('ask-question.html')
    else:
        return "matéka meleg"


@app.route("/question/<id>", methods=["GET", "POST"])
def route_question(id):
    if request.method == "GET":
        questions = data_manager.get_question_details(id)
        answers = data_manager.get_answer_details(id)
        return render_template("question.html", question=questions, answers=answers)
    return "this will be the add answer stuff"


@app.route("/answer/<answer_id>/delete/<id_>")
def route_delete_answer(answer_id, id_):
    pass


@app.route("/question/vote_up/<id>", methods=["POST"])
def route_question_voting_up(id):
    vote = "Vote up"
    data_manager.change_vote_number(vote, id)
    return redirect("/")


@app.route("/question/vote_down/<id>", methods=["POST"])
def route_question_voting_down(id):
    vote = "Vote down"
    data_manager.change_vote_number(vote, id)
    return redirect("/")


@app.route("/question/<id>/<vote>/<submission_time>")
def route_answer_voting(id, vote, submission_time):
    pass


@app.route("/question/<id>/edit", methods=["GET", "POST"])
def route_edit_question(id):
    pass


@app.route("/answer/<answer_id>/edit", methods=["GET", "POST"])
def route_edit_answer(answer_id):
    answer_detail = data_manager.get_the_answer(answer_id)
    if request.method == "GET":
        return render_template('answer.html', answer_detail=answer_detail)
    else:
        new_message = request.form["edit_answer_text"]
        data_manager.get_current_answer_details(answer_id, new_message)
        print(answer_detail)
        return redirect("/question/" + str(answer_detail['question_id']))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
