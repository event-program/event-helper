import sqlite3


def db_make():

    conn = sqlite3.connect('helper.db')

    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE Event (event_name text, event_start_date text, event_end_date text, event_location text, event_description text, event_id text, event_banner text, participant text)""")
    except:
        pass

    try:
        cur.execute("""
        CREATE TABLE User (user_name text, user_phone_number text, language text, user_id text, user_optional text, qr_code text)
        """)
    except:
        pass

    try:
        cur.execute("""
        CREATE TABLE Alert (type text, name text)
        """)
    except:
        pass

    conn.commit()

if __name__ == "__main__":
    db_make()