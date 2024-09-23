from flask import Flask, render_template
import csv
import os

app = Flask(__name__)
@app.route('/data')
def data():
    return "This is the data page."

@app.route('/')
def index():
    # Read data from the files
    data1 = read_file('/data/data.txt')
    data2 = read_data2('/data/data2.csv')
    data3 = read_data2('/data/data3.csv')
    data4 = read_data2('/data/data4.csv')

    
    return render_template('index.html', data1=data1, data2=data2,data3=data3,data4=data4)

def read_data2(filepath):
    """Read a CSV file and return its content as a list of rows."""
    if os.path.exists(filepath):
        with open(filepath, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data2 = [row for row in reader]
            print("demo")
        return data2
    return []


def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read()
    return "No data available."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)