from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField, SelectMultipleField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
# from wsgiref.validate import validator

class EmailForm(Form):
    user_email = StringField('user_email', [DataRequired(),Email()])
    user_name = StringField('user_name', [DataRequired()])
    user_districts = SelectMultipleField('user_districts', choices=[('1', 'District 1'),('2', 'District 2'),('3', 'District 3'),('4', 'District 4'),('5', 'District 5'),('6', 'District 6'),('7', 'District 7')])
    user_message = TextAreaField('user_message')