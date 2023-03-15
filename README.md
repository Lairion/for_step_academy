# For Step Academy

# How to start Python solution

## Install Python
Download and install latest Python version on https://www.python.org/

## Install package virtualenv

```
pip install virtualenv
```

## Install packeges for project

Create environment for python packeges
```
cd <root_project>/pysolution/
virtualenv env

```
Activate environment
### For Windows
```
env\Scripts\activate

```
### For unix
```
source env\scripts\activate

```
### Install packages
```
pip install -r req.txt

```

## Raw data for python solution

Folder structure

```
.
└── data/
    ├── satelit/
    │   ├── <class_name>/
    │   │   └── <your_png>.png
    │   └── ...
    └── ...
```
## Setup Tuya API

Go to H:\My_project\python\Geo_II\py_solution\cred and add parameter to tuya_cred.ini

Use that instruction for getting parameters
https://developer.tuya.com/en/docs/iot/Configuration_Guide_custom?id=Kamcfx6g5uyot

## Usage
Run next python script and choose option for run
```
python <root_project>/pysolution/__main__.py
or
python <root_project>/pysolution

```
