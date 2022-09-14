from pickle import TRUE


class DefaultDBRouter:

    route_app_labels = { 'admin', 'auth', 'contenttypes',  'messages', 'staticfiles', 'testdb', 'sessions' }
    testdefaultdb={'Teacher','Student'}

    def db_for_read(self, model, **hints):
        """
        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if (model._meta.app_label in self.route_app_labels and model.__name__ in self.testdefaultdb):
            return 'default'
        elif model._meta.app_label in self.route_app_labels and model._meta.app_label!='testdb':
            return 'default'
        return False

    def db_for_write(self, model, **hints):
        """
        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if (model._meta.app_label in self.route_app_labels and model.__name__ in self.testdefaultdb):
            return 'default'
        elif (model._meta.app_label in self.route_app_labels and model._meta.app_label!='testdb'):
            return 'default'
        return False

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app1 or app2 apps is
        involved.
        """
        if (
            (obj1._meta.app_label in self.route_app_labels and obj1.__class__.__name__ in self.testdefaultdb) or
            (obj2._meta.app_label in self.route_app_labels and obj2.__class__.__name__ in self.testdefaultdb)
        ):
            return True
        elif (
            (obj1._meta.app_label in self.route_app_labels and obj1._meta.app_label!='testdb') or
            (obj2._meta.app_label in self.route_app_labels and obj2._meta.app_label!='testdb')
        ):    
            return True
        else:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app1 and app2 apps only appear in the
        app1 or app2 database.
        """
        if app_label in self.route_app_labels and (model_name=="teacher" or model_name=="student"):
            return db == 'default'
        elif app_label in self.route_app_labels and app_label!='testdb':
            return db == 'default'
        return None

class ProdDBRouter:

    route_app_labels = {'testdb'}
    proddb={'Teacherprod','Studentprod'}

    def db_for_read(self, model, **hints):
        """
        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if model._meta.app_label in self.route_app_labels and model.__name__ in self.proddb:
            return 'proddb'
        return False

    def db_for_write(self, model, **hints):
        """

        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if model._meta.app_label in self.route_app_labels and model.__name__ in self.proddb:
            return 'proddb'
        return False

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app1 or app2 apps is
        involved.
        """
        if (
                (obj1._meta.app_label in self.route_app_labels and obj1.__class__.__name__ in self.proddb) or
                (obj2._meta.app_label in self.route_app_labels and obj2.__class__.__name__ in self.proddb) 
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app1 and app2 apps only appear in the
        app1 or app2 database.
        """
        if (model_name=="teacherprod" or model_name=="studentprod"):
            if app_label in self.route_app_labels:
                return db == 'proddb'
        return None
    
class TestDBRouter:

    route_app_labels = {'testdb'}
    testdab={'Teachertest','Studenttest'}

    def db_for_read(self, model, **hints):
        """
        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if model._meta.app_label in self.route_app_labels and model.__name__ in self.testdab:
            return 'testdbse'
        return False

    def db_for_write(self, model, **hints):
        """
        If the model is from app1, it suggests querying the app1 database. If the model is from app2, then app2
        """
        if model._meta.app_label in self.route_app_labels and model.__name__ in self.testdab:
            return 'testdbse'
        return False

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app1 or app2 apps is
        involved.
        """
        if (
                (obj1._meta.app_label in self.route_app_labels and obj1.__class__.__name__ in self.testdab) or
                (obj2._meta.app_label in self.route_app_labels and obj2.__class__.__name__ in self.testdab) 
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app1 and app2 apps only appear in the
        app1 or app2 database.
        """
        if (model_name=="teachertest" or model_name=="studenttest"):
            if app_label in self.route_app_labels:
                return db == 'testdbse'
        return None