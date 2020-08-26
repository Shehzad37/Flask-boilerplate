#!/usr/bin/env python3
from rvn.dbhandler.CveHandler import add_all_to_db
from rvn import app

if __name__ == '__main__':
    # add_all_to_db()
    app.run(debug=True, port=8000)