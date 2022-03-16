from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models.register import Email


@app.route('/')
def register():
    return render_template("index.html")

@app.route('/validate', methods =['POST'])
def validate_email():
    if not Email.validate_email(request.form):
        return redirect ('/')
    Email.save(request.form)
    return redirect ('/success')

@app.route('/success')
def success():
    return render_template('success.html', emails=Email.get_all_emails())

@app.route('/delete/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    Email.destroy(data)
    return redirect ('/success')