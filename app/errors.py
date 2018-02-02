from flask import render_template
from app import app_instance, db_instance

@app_instance.errorhandler(404)
def page_note_found_error(err):
    return render_template("err_404.html"), 404

@app_instance.errorhandler(500)
def internal_server_error(err):
    db_instance.session.rollback()
    return render_template("err_500.html"), 500
