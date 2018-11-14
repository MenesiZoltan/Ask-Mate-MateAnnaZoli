# SQL query file

import connection


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

