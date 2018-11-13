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
                    SELECT vote_number, title, message FROM question
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