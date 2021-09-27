from example.model.contact import database as contact_model
from example.controller.contact_controller import contact_controller


class ExampleRegistry:

    def register_model(self, flask_app):
        contact_model.create_all()

    def register_controller(self, flask_app):
        flask_app.register_blueprint(contact_controller)


example_registry = ExampleRegistry()
