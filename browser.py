from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_csv(data):
    with open(r'C:\Users\prem\vs-code\database.csv', mode='a') as databaser:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(databaser, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        return csv_writer.writerow([email,subject,message])

@app.route('/submitform', methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'try again!'
