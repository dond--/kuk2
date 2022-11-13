def on_received_number(receivedNumber):
    global s
    s = Math.map(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
        -95,
        -42,
        0,
        255)
    seznam[0] = seznam[1]
    seznam[1] = seznam[2]
    seznam[2] = seznam[3]
    seznam[3] = seznam[4]
    seznam[4] = s
    basic.pause(250)
    graf(seznam)
radio.on_received_number(on_received_number)

def graf(c: List[any]):
    basic.clear_screen()
    col(0, seznam[0], 1)
    col(1, seznam[1], 2)
    col(2, seznam[2], 3)
    col(3, seznam[3], 4)
    col(4, seznam[4], 5)
def col(x: number, val: number, br: number):
    if val <= 50:
        led.plot_brightness(x, 4, br * 15)
    else:
        if val <= 100:
            led.plot_brightness(x, 4, br * 50)
            led.plot_brightness(x, 3, br * 15)
        else:
            if val <= 150:
                led.plot_brightness(x, 4, br * 50)
                led.plot_brightness(x, 3, br * 30)
                led.plot_brightness(x, 2, br * 15)
            else:
                if val <= 200:
                    led.plot_brightness(x, 4, br * 50)
                    led.plot_brightness(x, 3, br * 40)
                    led.plot_brightness(x, 2, br * 30)
                    led.plot_brightness(x, 1, br * 15)
                else:
                    led.plot_brightness(x, 4, br * 50)
                    led.plot_brightness(x, 3, br * 45)
                    led.plot_brightness(x, 2, br * 40)
                    led.plot_brightness(x, 1, br * 30)
                    led.plot_brightness(x, 0, br * 15)
s = 0
seznam: List[number] = []
radio.set_group(1)
seznam = [50, 150, 250, 150, 50]
graf(seznam)