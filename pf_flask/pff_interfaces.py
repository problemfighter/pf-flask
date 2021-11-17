from abc import abstractmethod, ABC


class PFFRegisterModule(ABC):

    @abstractmethod
    def register_model_controller(self, flask_app):
        pass

    @abstractmethod
    def run_on_start(self, flask_app):
        pass


class PFFAppRegistry(ABC):

    @abstractmethod
    def register_model(self):
        pass

    @abstractmethod
    def register_controller(self, flask_app):
        pass

    @abstractmethod
    def run_on_start(self, flask_app):
        pass
