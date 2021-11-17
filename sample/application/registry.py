from pf_flask.pff_interfaces import PFFRegisterModule
from example.example_registry import example_registry


class Register(PFFRegisterModule):

    def register_model_controller(self, flask_app):
        print("Register Model Controller")
        example_registry.register_model()
        example_registry.register_controller(flask_app)

    def run_on_start(self, flask_app):
        print("Run On Start")
