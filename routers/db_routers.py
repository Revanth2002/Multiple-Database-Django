from myapp.models import Todo

#Method-1
class AuthRouter:
    route_app_labels = {'auth','contenttypes','admin','sessions'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self,obj1,obj2,**hints):
        if(obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None

class BlueRouter:
    #blue is app name
    route_app_labels = {'blue'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue'
        return None

    # def allow_relation(self,obj1,obj2,**hints):
    #     if(obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
    #         return True
    #     return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'blue'
        return None

class TodoRouter:
    #blue is app name
    route_app_labels = {'myapp'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'todo'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'todo'
        return None

    # def allow_relation(self,obj1,obj2,**hints):
    #     if(obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
    #         return True
    #     return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'todo'
        return None


#Method-2
from myapp.models import Blog
class BlogRouter:
    #blue is app name
    route_app_labels = {'myapp'}

    def db_for_read(self, model, **hints):
        if (model == Blog):
           # your model name as in settings.py/DATABASES
           return 'todo'
        return None
       
    def db_for_write(self, model, **hints):
        if (model == Blog):
           # your model name as in settings.py/DATABASES
           return 'todo'
        return None
    # d ef allow_relation(self,obj1,obj2,**hints):
    #     if(obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
    #         return True
    #     return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'todo'
        return None


#Difference Between Method-1 and Method-2
#Method-1 => Running migrations cmd database might add other models too if its in makemigrations
#            using('accounts') method is required sometimes to query from a specific db
#Method-2 => Specifying model name and database table. Wont mix with other database when makemigrations and migrate is performed
#            and only migrates to the specific database. using('accounts') method is not required here



        
