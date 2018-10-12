from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

basic_form = """
<form action="/" method ='POST'>
        <input type="submit" value="Submit"/>
</form>
"""

@app.route("/")
def index():
    return basic_form

@app.route("/")
def index():
    return 'post'
    
    <h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header + edit_header + add_form + page_footer

    return content


app.run()
