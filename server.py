from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__, template_folder='templates')
print(__name__)

@app.route('/')
def mp():
    return render_template('index.html')

@app.route('/<string:page_name>')
def dp(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        full_name =  data["fullname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{full_name} , {email} , {subject} , {message}')
    
def write_to_csv(data):
    with open('database.csv', mode='a' , newline='') as database2:
        full_name = data["fullname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2 , delimiter=',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([full_name,email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    return 'somthing went wrong'
