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
def show_questions_by_order(cursor, direction, order_type):
    if order_type == "time":
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

    elif order_type == "vote_numbers":
        if direction == "desc":
            cursor.execute('''
                            SELECT id, vote_number, title, submission_time FROM question
                            ORDER BY vote_number DESC;
                            ''')
            details = cursor.fetchall()
            return details
        elif direction == "asc":
            cursor.execute('''
                            SELECT id, vote_number, title, submission_time FROM question
                            ORDER BY vote_number DESC;
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
                    SELECT vote_number, message, id FROM answer
                    WHERE question_id = %(id)s;
                    ''',
                   {'id': id})
    details = cursor.fetchall()
    return details


@connection.connection_handler
def get_the_answer(cursor, id):
    cursor.execute('''
                    SELECT message, id, question_id FROM answer
                    WHERE id = %(id)s
                    ''',
                   {'id': id})
    details = cursor.fetchone()
    return details


@connection.connection_handler
def change_vote_number(cursor, vote, id):
    if vote == "Vote up":
        vote_num = 1
    if vote == "Vote down":
        vote_num = -1
    cursor.execute('''
                    UPDATE question
                    SET vote_number = vote_number + %(vote_num)s
                    WHERE id = %(id)s;
                    ''',
                   {'id': id, 'vote_num': vote_num})


@connection.connection_handler
def get_current_answer_details(cursor, id, new_message):
    cursor.execute('''
                    UPDATE answer
                    SET message = %(new_message)s
                    WHERE id = %(id)s;
                    ''',
                   {'id': id, 'new_message': new_message})


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


@connection.connection_handler
def get_comments(cursor, question_id):
    cursor.execute('''
                   SELECT message,submission_time FROM comment
                   WHERE question_id = %(question_id)s;
                   ''',
                   {"question_id": question_id})
    comments = cursor.fetchall()
    return comments


@connection.connection_handler
def add_comment(cursor, question_id, message):
    submission_time = datetime.now()
    edited_count = 0
    cursor.execute('''
                   INSERT INTO comment(question_id, message, submission_time, edited_count)
                   VALUES(%(question_id)s, %(message)s, %(submission_time)s, %(edited_count)s);
                   ''',
                   {"question_id": question_id,
                    "message": message,
                    "submission_time": submission_time,
                    "edited_count": edited_count})


@connection.connection_handler
def get_comment(cursor, question_id):
    cursor.execute('''
                   SELECT message, id FROM comment
                   WHERE question_id=%(question_id)s;
                   ''',
                   {"question_id":question_id})
    message = cursor.fetchone()
    return message


@connection.connection_handler
def edit_comment(cursor, message, question_id):
    cursor.execute('''
                   UPDATE comment
                   SET message=%(message)s
                   WHERE question_id=%(question_id)s;
                   ''',
                   {"message": message, "question_id": question_id})


@connection.connection_handler
def delete_comment(cursor, question_id):
    cursor.execute('''
                   DELETE FROM comment WHERE question_id=%(question_id)s;
                   ''',
                   {"question_id": question_id})


@connection.connection_handler
def get_comment_id(cursor, question_id,message):
    cursor.execute('''
                   SELECT id FROM comment
                   WHERE question_id=%(question_id)s AND message=%(message)s;
                   ''',
                   {"question_id": question_id, "message": message})
    comment_id = cursor.fetchone()
    return comment_id
