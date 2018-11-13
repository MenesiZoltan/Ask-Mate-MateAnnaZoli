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
                    SELECT vote_number, message FROM answer
                    WHERE question_id = %(id)s;
                    ''',
                   {'id': id})
    details = cursor.fetchall()
    return details
