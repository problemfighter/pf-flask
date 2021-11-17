from example.model.contact import database as contact_model
from example.controller.contact_controller import contact_controller
from pf_flask.pff_interfaces import PFFAppRegistry


class ExampleRegistry(PFFAppRegistry):

    def run_on_start(self, flask_app):
        pass

    def register_model(self):
        contact_model.create_all()

    def register_controller(self, flask_app):
        flask_app.register_blueprint(contact_controller)


example_registry = ExampleRegistry()
