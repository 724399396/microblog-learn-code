from flask import render_template
from app import app, db

@app.errorhandler(Exception)
def not_found_error(error):
    return render_template('404.html'), 404

app.register_error_handler(404, not_found_error)

@app.errorhandler(Exception)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


app.register_error_handler(500, internal_error)