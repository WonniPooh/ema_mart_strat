start cmd /k "cd .. & python -Xutf8 strategy/main.py & timeout /t 10"

timeout /t 5

start cmd /k "cd .. & python -Xutf8 interface/main.py & timeout /t 10"
