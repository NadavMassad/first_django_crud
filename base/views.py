from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student, Phones


def index(r):
    return JsonResponse("Hello", safe=False)

# Crud for the Students model(table)
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def students(request, id=-1):
    if request.method == 'GET':
        students = []
        if int(id) > -1:
            stu = Student.objects.get(id=(int(id)))
            students.append({"id": stu.id, "sName": stu.sName, "age": stu.age})
        else:
            for stu in Student.objects.all():
                students.append(
                    {"id": stu.id, "sName": stu.sName, "age": stu.age})
        return JsonResponse(students, safe=False)
    if request.method == 'POST':
        Student.objects.create(
            sName=request.data['sName'], age=request.data['age'])
        return JsonResponse('Student Added Successfully', safe=False)
    if request.method == 'DELETE':
        if int(id) > -1:
            del_student = Student.objects.get(id=int(id))
            del_student.delete()
            return JsonResponse(f'Student With ID: {id} Was Deleted', safe=False)
    if request.method == 'PUT':
        if int(id) > -1:
            upd_student = Student.objects.get(id=int(id))
            upd_student.sName = request.data['sName']
            upd_student.age = request.data['age']
            upd_student.save()
            return JsonResponse(f'Student With ID: {id} Was Updated', safe=False)


# Crud for the Phones model(table)
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def phones(request, id=-1):
    if request.method == 'GET':
        phones = []
        if int(id) > -1:
            phone = Phones.objects.get(id=int(id))
            phones.append({"id": phone.id, "sName": phone.name,
                          "color": phone.color, "price": phone.price})
        else:
            for phone in Phones.objects.all():
                phones.append({"id": phone.id, "sName": phone.name,
                              "color": phone.color, "price": phone.price})
        return JsonResponse(phones, safe=False)
    if request.method == 'POST':
        Phones.objects.create(
            name=request.data['name'], color=request.data['color'], price=request.data['price'])
        return JsonResponse("Phone Added Successfuly", safe=False)
    if request.method == 'DELETE':
        del_phone = Phones.objects.get(id=int(id))
        del_phone.delete()
        return JsonResponse(f"Phone With ID: {id} Was Deleted", safe=False)
    if request.method == 'PUT':
        upd_phone = Phones.objects.get(id=int(id))
        upd_phone.name = request.data['name']
        upd_phone.color = request.data['color']
        upd_phone.price = request.data['price']
        upd_phone.save()
        return JsonResponse(f"Phone With ID: {id} Was Updated", safe=False)
