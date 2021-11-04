from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
]


def index(request):
    context = {'id': my_task_list.get('id'), 'name': my_task_list.get('name'),
               'priority': my_task_list.get('priority'), 'description': my_task_list.get('description')}
    return render(request, 'todo/home.html', context=context)

def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])
    return index_of_task

def tasks(request):
    return render(request,'todo/home.html', {'my_task_list':my_task_list})


def detail(request, pk):
    task = _get_target_task(pk)
    detail = list(filter(lambda i: i['index'] == task, my_task_list))
    return render(request, 'todo/home.html', {'my_task_list': detail})


def update(request, pk):
    task = _get_target_task(pk)
    my_task_list[task].update({'name': "updated-movie"})
    return render(request, 'todo/home.html', {'my_task_list': my_task_list})


def delete(request, pk):
    task = _get_target_task(pk)
    del my_task_list[task]
    return render(request,'todo/home.html', {'my_task_list':my_task_list})


