import pytest
import requests
from methods.user.registration_user_methods import RegistrationUserMethods
from methods.user.delete_user_methods import DeleteUserMethods
from methods.user.login_user_methods import LoginUserMethods
from methods.user.change_user_methods import ChangeUserMethods
from methods.order.create_order_methods import CreateOrderMethods
from methods.order.get_order_methods import GetOrderMethods


@pytest.fixture(scope='function')
def registration_user_methods():
    response = requests
    registration_user_methods = RegistrationUserMethods(response)
    yield registration_user_methods
    delete_user_methods = DeleteUserMethods(response)
    if registration_user_methods.get_auth_token():
        delete_user_methods.delete_user({'Authrization': registration_user_methods.get_auth_token()})

@pytest.fixture()
def login_user_methods():
    response = requests
    login_user_methods = LoginUserMethods(response)
    return login_user_methods

@pytest.fixture()
def change_user_methods():
    response = requests
    change_user_methods = ChangeUserMethods(response)
    return change_user_methods

@pytest.fixture()
def create_order_methods():
    response = requests
    create_order_methods = CreateOrderMethods(response)
    return create_order_methods

@pytest.fixture()
def get_order_methods():
    response = requests
    get_order_methods = GetOrderMethods(response)
    return get_order_methods
