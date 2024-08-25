import time
from machine import Pin

def main():
    led = Pin(16,Pin.OUT)
    print('Blink modo RUN')

    try:
        while True:
            led(led() ^ 1)
            time.sleep_ms(1000)

    finally:
        print('Blink finalizado') 

import nop
main()

