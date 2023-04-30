import psycopg2

user_name = input()
with psycopg2.connect(dbname="postgres", user="postgres", password=" ", host="127.0.0.1") as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users_test (
        user_id SERIAL PRIMARY KEY,
        name TEXT
        )""")
    cur.execute(""" CREATE TABLE IF NOT EXISTS levels_test (
           level_id SERIAL PRIMARY KEY REFERENCES users_test(user_id),
           level int
           )""")

    cur.execute(f"SELECT name FROM users_test WHERE name = '{user_name}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users_test(name) VALUES ('{user_name}')")
        cur.execute(f"INSERT INTO levels_test(level) VALUES (0)")
        level = 0
    else:
        cur.execute(
            f"SELECT levels_test.level, levels_test.level_id, users_test.name, users_test.user_id FROM levels_test join users_test on levels_test.level_id = users_test.user_id  WHERE name = '{user_name}'")
        level = cur.fetchone()
        level = level[0]
    cur.execute(
        f"SELECT users_test.user_id, users_test.name, levels_test.level FROM levels_test join users_test on levels_test.level_id = users_test.user_id  WHERE name = '{user_name}'")
    data = cur.fetchall()
    for i in data:
        print(i)


def update(nm, nlv):
    with psycopg2.connect(dbname="postgres", user="postgres", password=" ", host="127.0.0.1") as con:
        cur = con.cursor()
        cur.execute(f"""UPDATE levels_test SET level = {nlv}
                        WHERE level_id = (
                            SELECT users_test.user_id
                            FROM users_test
                            WHERE name = '{nm}'
                        )""")
