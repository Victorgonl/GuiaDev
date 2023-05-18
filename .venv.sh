#!/bin/sh

if [ -f ".venv/bin/django-admin" ]; then
    cd src; exec bash
else
    exec bash
fi
