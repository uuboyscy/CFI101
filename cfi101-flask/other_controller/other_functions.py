from flask import Blueprint

otherController = Blueprint('otherController', __name__)

@otherController.route('/other_controller')
def other_controller():
    return 'other_controller123123123'