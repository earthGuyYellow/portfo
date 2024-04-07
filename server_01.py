from flask import Flask, render_template, url_for, request, redirect, send_from_directory
import csv 
import os 

app = Flask(__name__)
print(__name__)

#each app.route signfies a page on server
@app.route("/")
def homepage():
    return render_template('web_template_01.html') 
    #render template is in house flask, html file we are seeking to use.
    # flask automtically searches for folder called templates w/n directory
    # flask templates give us use of multiple html files.

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'myIcon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database_01.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database_csv:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
    if request.method == 'POST':
            try:
                data = request.form.to_dict()
                write_to_csv(data)
                write_to_file(data)
                #return 'Form submitted. Now quit asking. -Nick Saban'
                return redirect("/thankyou.html")
            except:
                return 'Did not save to database. Did your Mom unplug the cord again?'
    else:   
        return'There is a snake in your boot. Check your code and try again.'


