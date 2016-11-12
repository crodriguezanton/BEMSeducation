#!/bin/sh
cd ../
cd BEMS-auth
python setup.py sdist
cd ../BEMS-instances
python setup.py sdist
cd ../../
pip install BEMSxyz/BEMS-auth --upgrade
pip install BEMSxyz/BEMS-instances --upgrade
cd BEMSxyz/BEMSeducation
python manage.py runserver
