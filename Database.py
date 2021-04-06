import sqlite3


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query, user_victories, user_fails, user_win_friendly, name, age):
    cursor = connection.cursor()
    try:

        cursor.execute(query, (user_victories, user_fails, user_win_friendly, name, age))
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error in execute_query '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error in execute_read_query '{e}' occurred")

def read_user_stat(conn, name, age):
    query = f"""
    SELECT
     victories, fails, win_friendly
    FROM Users
    WHERE 
        name LIKE "{name}" AND age = {age}
    """
    user_stats = execute_read_query(conn, query)
    return user_stats[0]

    #return user_stats(0)
    #return [0, 0, 0]

def write_round_stat(connection, usernames, ages, results):
    user1, user2 = usernames
    age1, age2 = ages
    user1_result, user2_result = results
    user1_victories, user1_fails, user1_win_friendly = read_user_stat(connection, user1, age1)
    user2_victories, user2_fails, user2_win_friendly = read_user_stat(connection, user2, age2)
    if user1_result == 100:
        user1_win_friendly += 1
        user2_win_friendly += 1
    if user1_result == 0:
        user1_fails += 1
        user2_victories += 1
    if user1_result == 1:
        user1_victories += 1
        user2_fails += 1
    query = f"""
            UPDATE
                users
            SET victories=?, fails=?, win_friendly=?
            WHERE name=? AND age=?;
            """
    execute_query(connection, query, user1_victories, user1_fails, user1_win_friendly, user1, age1)
    execute_query(connection, query, user2_victories, user2_fails, user2_win_friendly, user2, age2)
    test1=1