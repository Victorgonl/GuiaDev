#!/bin/sh

if [ -f ".venv/bin/django-admin" ]; then
    cd src; exec bash
else
    echo "Comandos para criação do ambiente:\npython3 -m venv .venv\nsource .venv/bin/activate\npip install -r requirements.txt\ncd src"; exec bash
fi
