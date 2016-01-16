import sqlite3
import time
import json

def get_temp_json():
    conn = sqlite3.connect('data-dev.sqlite3')
    return_array = []

    #time_range = int(time.time()) - (60*60*24.0) #grab the last 24 hours
    cur = conn.cursor()
    cur.execute("SELECT * FROM tempdata")

    rows = cur.fetchall()

    for row in rows:
        timestamp = row[2]
        temp = row[1]
        return_array.append({'date': timestamp, 'temperature': temp})

    #response = Response(json.dumps(return_array))
    return json.dumps(return_array)

if __name__ == "__main__":
    print(get_temp_json())
