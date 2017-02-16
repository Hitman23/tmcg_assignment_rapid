from __future__ import absolute_import

from api_test.celery import app
from .models import GetData, Groups
from temba_client.v2 import TembaClient


@app.task
def callData():
    k = GetData.objects.first()

    url = k.url
    token = k.token
    group_size = k.number_of_groups

    client = TembaClient(url, token)
    new_group_data = client.get_groups().all()
    g_number = len(new_group_data)
    existing_groups = Groups.objects.all()
    existing_grouplst = []
    for g in existing_groups:
        existing_grouplst.append(g.name)

    for groupz in new_group_data:
        if groupz.name in existing_grouplst:
            return
        else:
            Groups.objects.create(name=groupz.name, number_of_contacts=groupz.count)

        k.number_of_groups = g_number
        k.save()

    return
