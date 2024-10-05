start cmd /k "cd .. & python -Xutf8 strategy/main.pyc & timeout /t 10"

timeout /t 5

start cmd /k "cd .. & python -Xutf8 interface/main.pyc & timeout /t 10"
