error in Arduino IDE trying to use it with ESP32

exec: "python": executable file not found in $PATH Compilation error: exec: "python": executable file not found in $PATH

jagadeesh97@jagadeesh97-HP-Pavilion-Laptop-15-eg2xxx:~$ sed -i -e 's/=python /=python3 /g' ~/.arduino15/packages/esp32/hardware/esp32/*/platform.txt

execute above cmd in terminal 

install pyserial using pip if on running above cmd results in this error [ModuleNotFoundError: No module named 'serial']

PS : Try using ESP32 Wrover Module as board in Arduino IDE
