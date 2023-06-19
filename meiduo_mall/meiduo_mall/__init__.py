# from pymysql import install_as_MySQLdb
#
# install_as_MySQLdb()

import pymysql

pymysql.version_info = (1, 4, 0, 'final', 0)  #指定版本，这句才是关键
pymysql.install_as_MySQLdb()
