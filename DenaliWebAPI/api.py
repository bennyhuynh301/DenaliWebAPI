from tastypie.resources import ModelResource
from django.db import IntegrityError
from django.http import HttpResponseBadRequest
from ChopChore.models import Parent, Kid, Chore


class MultiPartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.Meta.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)
            return data

        return super(MultiPartResource, self).deserialize(request, data, format)


class ParentResource(ModelResource):
    class Meta:
        queryset = Parent.objects.all()
        resource_name = 'parents'

    def obj_create(self, bundle, **kwargs):
        device_id, name, email, password, role = bundle.data['device_id'], bundle.data['name'], \
                                                 bundle.data['email'], bundle.data['password'], bundle.data['role']
        try:
            bundle.obj = Parent(device_id=device_id,
                                name=name,
                                email=email,
                                password=password,
                                role=role)
            bundle.obj.save()
        except IntegrityError:
            raise HttpResponseBadRequest()
        return bundle


class KidResource(ModelResource):
    class Meta:
        queryset = Kid.objects.all()
        resource_name = 'kids'

    def obj_create(self, bundle, **kwargs):
        device_id, name, age, password, gender = bundle.data['device_id'], bundle.data['name'], \
                                                 bundle.data['age'], bundle.data['password'], bundle.data['gender']
        try:
            bundle.obj = Kid(device_id=device_id,
                             name=name,
                             age=age,
                             password=password,
                             gender=gender)
            bundle.obj.save()
        except IntegrityError:
            raise HttpResponseBadRequest()
        return bundle


class ChoreResource(ModelResource):
    class Meta:
        queryset = Chore.objects.all()
        resource_name = 'chores'

    def obj_create(self, bundle, **kwargs):
        device_id, name, description, custom = bundle.data['device_id'], bundle.data['name'], \
                                               bundle.data['description'], bundle.data['custom']
        try:
            bundle.obj = Chore(device_id=device_id,
                               name=name,
                               description=description,
                               custom=custom)
            bundle.obj.save()
        except IntegrityError:
            raise HttpResponseBadRequest()
        return bundle






