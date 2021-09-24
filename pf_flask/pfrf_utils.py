import sys

from werkzeug.utils import ImportStringError


def import_from_string(import_name: str, silent: bool = False):
    import_name = import_name.replace(":", ".")
    try:
        try:
            __import__(import_name)
        except ImportError:
            if "." not in import_name:
                raise
        else:
            return sys.modules[import_name]

        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
        try:
            return getattr(module, obj_name)
        except AttributeError as e:
            raise ImportError(e)

    except ImportError as e:
        if not silent:
            raise ImportStringError(import_name, e).with_traceback(sys.exc_info()[2])

    return None


def is_url_register(flask_app, url):
    for url_rule in flask_app.url_map.iter_rules():
        if url_rule.rule == url:
            return True
    return False
