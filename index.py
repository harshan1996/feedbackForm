from flask import Flask, render_template, request
import pymysql
from send_mail import send_mail
from config import host,user,database,password
import os

app = Flask(__name__)

mydb = pymysql.connect(host=host,user=user,database=database,password=password)

my_cursor = mydb.cursor()

create_table="CREATE TABLE feedback (id INT AUTO_INCREMENT PRIMARY KEY, customer VARCHAR(255), dealer VARCHAR(255),rating INT, comments VARCHAR(400))"
# Run the below command once and then comment it to avoid re-creating the table which leads to error.
# my_cursor.execute(create_table)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return render_template('index.html', message='please enter all details')
        check_customer_in_query = "SELECT * FROM feedback WHERE customer =%s"
        my_cursor.execute(check_customer_in_query,(customer,))
        result=my_cursor.fetchall()
        if len(result)==0:
            insert_data = "INSERT INTO feedback (customer,dealer,rating,comments) VALUES (%s,%s,%s,%s)"
            values = (customer,dealer,str(rating),comments)
            my_cursor.execute(insert_data, values)
            my_cursor.close()
            mydb.commit()
            send_mail(customer,dealer,rating,comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted the feedback')


if __name__ == '__main__':
    app.run(host= "0.0.0.0",port=int(os.environ.get("PORT", 5000)))
