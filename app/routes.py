from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user
from app.controllers.car_controller import create_car, get_cars

bp = Blueprint('bp', __name__)


# home(/)
@bp.route('/')
def home():
    return '<h1>User API</h1>'


# (/user) C
@bp.route('/users', methods=['POST'])
def add_user():
    return create_user()

# (/user) R
@bp.route('/users', methods=['GET'])
def list_users():
    return get_users()


# (/user/id) R
@bp.route('/users/<int:user_id>', methods=['GET'])
def list_user(user_id):
    return get_user(user_id)

# (/user/id) U
@bp.route('/users/<int:user_id>', methods=['PATCH'])
def edit_user(user_id):
    return update_user(user_id)



# (/cars) C
@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()

# (/cars) R
@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

""" TD """

# (/cars/car_id) R


# (/cars/car_id) U


# (/cars/car_id) D
