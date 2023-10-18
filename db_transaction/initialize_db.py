# from db_transaction.models.admin_model import db
from db_transaction import createApp


def createDB():
    app = createApp()
    with app.app_context():
        db.create_all()
        app.run(debug=True)

