from __future__ import print_function

from tornado import ioloop, gen
import tornado_mysql

@gen.coroutine
def main():
    conn = yield tornado_mysql.connect(host='192.168.1.155', port=3306,charset='utf8', user='root', passwd='1qazxsw2!@', db='wpnbmdb')
    cur = conn.cursor()
    yield cur.execute("SELECT * from zs_yjsf")
    print(cur.description)
    for row in cur:
        print(row)
    cur.close()
    conn.close()

ioloop.IOLoop.current().run_sync(main)