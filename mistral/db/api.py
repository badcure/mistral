# -*- coding: utf-8 -*-
#
# Copyright 2013 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# TODO: replace this module later with a real implementation
from mistral.openstack.common.db import api as db_api
from mistral.openstack.common import log as logging

# Workbooks

_BACKEND_MAPPING = {
    'sqlalchemy': 'mistral.db.sqlalchemy.api',
}

IMPL = db_api.DBAPI(backend_mapping=_BACKEND_MAPPING)
LOG = logging.getLogger(__name__)


def setup_db():
    IMPL.setup_db()


def drop_db():
    IMPL.drop_db()


# Workbook

def workbook_get(name):
    return IMPL.workbook_get(name)


def workbook_create(values):
    return IMPL.workbook_create(values)


def workbook_update(name, values):
    return IMPL.workbook_update(name, values)


def workbook_delete(name):
    IMPL.workbook_delete(name)


def workbooks_get():
    return IMPL.workbooks_get_all()


def workbook_definition_get(workbook_name):
    return IMPL.workbook_get(workbook_name)['doc']


def workbook_definition_put(workbook_name, text):
    workbook = IMPL.workbook_update(workbook_name, {'doc': text})
    IMPL.create_associated_events(workbook)
    return workbook


# Executions


def execution_get(workbook_name, id):
    return IMPL.execution_get(workbook_name, id)


def execution_create(workbook_name, values):
    return IMPL.execution_create(workbook_name, values)


def execution_update(workbook_name, id, values):
    return IMPL.execution_update(workbook_name, id, values)


def execution_delete(workbook_name, id):
    return IMPL.execution_delete(workbook_name, id)


def executions_get(workbook_name):
    return IMPL.executions_get_all(workbook_name=workbook_name)


# Tasks

def task_get(workbook_name, execution_id, id):
    return IMPL.task_get(workbook_name, execution_id, id)


def task_create(workbook_name, execution_id, values):
    return IMPL.task_create(workbook_name, execution_id, values)


def task_update(workbook_name, execution_id, id, values):
    return IMPL.task_update(workbook_name, execution_id, id, values)


def task_delete(workbook_name, execution_id, id):
    return IMPL.task_delete(workbook_name, execution_id, id)


def tasks_get(workbook_name, execution_id):
    return IMPL.tasks_get_all(workbook_name=workbook_name,
                              execution_id=execution_id)


# Listeners


def listener_get(workbook_name, id):
    return {}


def listener_create(workbook_name, values):
    values['id'] = 1

    return values


def listener_update(workbook_name, id, values):
    return values


def listener_delete(workbook_name, id):
    pass


def listeners_get(workbook_name):
    return [{}]


# Events

def event_create(values):
    return IMPL.event_create(values)


def event_update(event_id, values):
    return IMPL.event_update(event_id, values)


def get_next_events(time):
    return IMPL.get_next_events(time)