# SQL query file

import connection
from datetime import datetime


@connection.connection_handler
def show_questions(cursor):
    cursor.execute('''
                    SELECT id, vote_number, title, submission_time FROM question;
                    ''')
    details = cursor.fetchall()
    return details


@connection.connection_handler
def show_questions_by_order(cursor, direction):
    if direction == "desc":
        cursor.execute('''
                        SELECT id, vote_number, title, submission_time FROM question
                        ORDER BY submission_time DESC;
                        ''')
        details = cursor.fetchall()
        return details
    elif direction == "asc" or direction == None:
        cursor.execute('''
                        SELECT id, vote_number, title, submission_time FROM question
                        ORDER BY submission_time;
                        ''')
        details = cursor.fetchall()
        return details

@connection.connection_handler
def get_question_details(cursor, id):
    cursor.execute('''
                    SELECT vote_number, title, message, id FROM question
                    WHERE id = %(id)s;
                    ''',
                   {'id': id})
    details = cursor.fetchone()
    return details


@connection.connection_handler
def get_answer_details(cursor, id):
    cursor.execute('''
                    SELECT vote_number, message FROM answer
                    WHERE question_id = %(id)s;
                    ''',
                   {'id': id})
    details = cursor.fetchall()
    return details


# @connection.connection_handler
# def add_comment():
#     cursor.execute('''
#                    INSERT INTO
#                    ''')

@connection.connection_handler
def add_new_question(cursor, new_question):
    submission_time = datetime.now()
    view_number = 0
    vote_number = 0
    title = new_question["question_subject"]
    message = new_question["question_text"]
    image = new_question["url"]
    cursor.execute('''
                    INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                    VALUES ( %(submission)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s);
                    ''',
                   {"submission": submission_time,
                    "view_number": view_number,
                    "vote_number": vote_number,
                    "title": title,
                    "message": message,
                    "image": image})


@connection.connection_handler
def add_answer(cursor, new_answer):
    submission_time = datetime.now()
    question_id = new_answer["question_id"]
    vote_number = 0
    message = new_answer["answer_text"]
    cursor.execute('''
                   INSERT INTO answer(submission_time, vote_number, question_id, message)
                   VALUES(%(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s)
                   ''',
                   {"submission_time": submission_time,
                    "vote_number": vote_number,
                    "question_id": question_id,
                    "message": message})


@connection.connection_handler
def search_question(cursor, search_parameter):
    cursor.execute('''
                    SELECT id, vote_number, title, submission_time FROM question
                    WHERE title iLIKE %(search_parameter)s;
                    ''',
                   {"search_parameter": '%'+search_parameter +'%'})
    search_result = cursor.fetchall()
    return search_result


