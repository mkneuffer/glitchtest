from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aslkjhgftgb'  # Replace with your own secret key

class LinkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    num_links = IntegerField('Number of Links', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        # Process form data (e.g., store in a database)
        name = form.name.data
        num_links = form.num_links.data
        # You can add your custom logic here
        return f"Hello, {name}! You entered {num_links} links."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
