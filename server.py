from flask import (Flask, render_template, send_from_directory, request,
                   redirect)
import os
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}.html')


# def write_to_file(data):
#     with open('data.txt', mode='a') as datafile:
#         email = data['email']
#         subject = data['subject']
#         body = data['body']
#         file = datafile.write(f'\n{email}, {subject}, {body}')


def write_to_csv(data):
    with open('data.csv', newline='', mode='a') as data_csv:
        email = data['email']
        subject = data['subject']
        body = data['body']
        write_to_csv = csv.writer(data_csv,
                                  delimiter=',',
                                  quotechar='\'',
                                  quoting=csv.QUOTE_MINIMAL)
        write_to_csv.writerow([email, subject, body])


@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'did not save correctly'
    else:
        return 'something went wrong!'