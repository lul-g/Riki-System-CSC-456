#!/Users/smcho/virtualenv/riki/bin/python
# -*- coding: utf-8 -*-
import os
from wiki import create_app

cur_directory = os.getcwd()
app = create_app(cur_directory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5005)