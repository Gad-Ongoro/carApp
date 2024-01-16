from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user
from app.controllers.car_controller import create_car, get_cars, get_car, update_car, delete_car

from app.controllers.sales_controller import create_sale, get_sales, get_sale, update_sale, delete_sale

bp = Blueprint('bp', __name__)


# home(/)
@bp.route('/')
def home():
    return '<h1>User API</h1>'

""" USERS """
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

""" CARS """
# (/cars) C
@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()

# (/cars) R
@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

# (/cars/car_id) R
@bp.route('/cars/<int:car_id>', methods = ['GET'])
def read_car(car_id):
    return(get_car(car_id))


# (/cars/car_id) U
@bp.route('/cars/<int:car_id>', methods = ["PATCH"])
def patch_car(car_id):
    return(update_car(car_id))

# (/cars/car_id) D
@bp.route('/cars/<int:car_id>', methods = ['DELETE'])
def remove_car(car_id):
    return(delete_car(car_id))


""" SALES """
# (/sales) C
@bp.route('/sales', methods=['POST'])
def add_sale():
    return create_sale()

# (/cars) R
@bp.route('/sales', methods=['GET'])
def list_sales():
    return(get_sales())

# (/sales/sale_id) R
@bp.route('/sales/<int:sale_id>', methods = ['GET'])
def read_sale(sale_id):
    return(get_sale(sale_id))

# (/sales/sales_id) U
@bp.route('/sales/<int:sale_id>', methods = ["PATCH"])
def patch_sale(sale_id):
    return(update_sale(sale_id))

# (/cars/car_id) D
@bp.route('/sales/<int:sale_id>', methods = ['DELETE'])
def remove_sale(sale_id):
    return(delete_sale(sale_id))