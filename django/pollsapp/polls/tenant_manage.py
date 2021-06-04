#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import random


def create_schema():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budgeting.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    from django.db import connection

    with connection.cursor() as cursor:
        schema  = "tenant" + str(random.randrange(100))
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS contacts(contact_id INTEGER PRIMARY KEY,first_name TEXT NOT NULL)")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
        cursor.execute(f"SET search_path to {schema}")
        execute_from_command_line(["manage.py", "migrate", "polls"])
        print("migrated")
        return schema


def connect_to_schema(schema):
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute("select schema_name from information_schema.schemata")
        rows = cursor.fetchall()
        available_schemas = [row[0] for row in rows]
        if(schema is not None and schema in available_schemas):
            print("connecting to schema:" + schema)
            cursor.execute(f"SET search_path to {schema}")
            print("connected to schema:" + schema)
        else:
            raise Exception("Invalid Schema")
