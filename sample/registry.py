from pf_flask.pff_interfaces import PFFRegisterModule


class Register(PFFRegisterModule):

    def register_model_controller(self, flask_app):
        print("Register Model Controller")

    def run_on_start(self, flask_app):
        print("Run On Start")
