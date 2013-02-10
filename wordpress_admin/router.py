#:coding=utf-8:

class WordPressRouter(object):
    """A router to control all database operations on models in
    the wordpress application"""

    def db_for_read(self, model, **hints):
        "Point all operations on wordpress models to 'wordpress'"
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on wordpress models to 'wordpress'"
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in wordpress is involved"
        if obj1._meta.app_label == 'wordpress' or obj2._meta.app_label == 'wordpress':
            return True
        return None

    def allow_syncdb(self, db, model):
        "We don't create the wordpress tables via Django."
        return model._meta.app_label != 'wordpress'
