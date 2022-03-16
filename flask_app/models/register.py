from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM email_address WHERE email = %(email)s"
        results = connectToMySQL('email_validation').query_db(query,email)
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_emails(cls):
        query ="SELECT * FROM email_address;";
        results = MySQLConnection('email_validation').query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails
    
    @classmethod
    def save(cls,data):
        query = "INSERT into email_address (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW())"
        return MySQLConnection('email_validation').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE from email_address WHERE id = %(id)s"
        return MySQLConnection('email_validation').query_db(query,data)
