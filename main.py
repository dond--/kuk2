def on_received_number(receivedNumber):
    basic.show_string("" + str((receivedNumber)))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("Polickaaa rulezz!")
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.clear_screen()
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    basic.show_string(name)
    basic.show_string("" + str((value)))
radio.on_received_value(on_received_value)

radio.set_group(255)
basic.show_number(3)
basic.show_number(2)
basic.show_number(1)

def on_forever():
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.pause(500)
basic.forever(on_forever)
