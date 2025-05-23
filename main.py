from flask import Flask
from app import views

app = Flask(__name__) # webserver gateway interphase (WSGI)

app.add_url_rule(rule='/',endpoint='home',view_func=views.index)
app.add_url_rule(rule='/app/',endpoint='app',view_func=views.app)
app.add_url_rule(rule='/app/gender/',
                 endpoint='gender',
                 view_func=views.genderapp,
                 methods=['GET','POST'])
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from Railway
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind to all interfaces

