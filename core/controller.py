from django.db import models


class EmptyModel(models.Model):
    pass


class APIController(object):
    def __init__(self, request, ctx, action=None, idx=None):
        self.request = request
        self.ctx = ctx
        self.action = action
        self.id = idx
        self.model = EmptyModel()
        self.open_model()

    def open_model(self):
        if self.id:
            models_import = self.get_models()
            name = self.__class__.__name__
            if hasattr(models_import, name):
                getattr(models_import, name)(pk=self.id)

    def get_models(self):
        return __import__(self.get_models_path).models

    def get_models_path(self):
        raise NotImplementedError("'get_models_path' not implemented for this context: (%s)" % self.__class__.__name__)

    def run_root(self):
        pass

    def run_id(self):
        pass

    def run_action_with_id(self):
        pass

    def run_action(self):
        pass

    def run(self):
        if self.action is None and self.id is None:
            self.run_root()
        elif self.id is not None and self.action is None:
            self.run_id()
        elif self.id is not None and self.action is not None:
            self.run_action_with_id()
        elif self.id is None and self.action is not None:
            self.run_action()
        else:
            raise AttributeError("Could not find appropriate API call to run.")

