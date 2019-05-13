from app.util.db import DbUtils

with DbUtils() as c:
    c.execute("UPDATE information SET enable = 1 WHERE ID = {}".format(2))
    max = c.execute("SELECT MAX(sort) FROM information WHERE time = date('now1')")
    max = max.fetchone()[0]
    print(max is None)