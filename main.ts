radio.onReceivedNumber(function (receivedNumber) {
    s = Math.map(radio.receivedPacket(RadioPacketProperty.SignalStrength), -95, -42, 0, 255)
    seznam[0] = seznam[1]
    seznam[1] = seznam[2]
    seznam[2] = seznam[3]
    seznam[3] = seznam[4]
    seznam[4] = s
    basic.pause(250)
    graf(seznam)
})
function graf (c: any[]) {
    basic.clearScreen()
    col(0, seznam[0], 1)
    col(1, seznam[1], 2)
    col(2, seznam[2], 3)
    col(3, seznam[3], 4)
    col(4, seznam[4], 5)
}
function col (x: number, val: number, br: number) {
    if (val <= 50) {
        led.plotBrightness(x, 4, br * 15)
    } else {
        if (val <= 100) {
            led.plotBrightness(x, 4, br * 50)
            led.plotBrightness(x, 3, br * 15)
        } else {
            if (val <= 150) {
                led.plotBrightness(x, 4, br * 50)
                led.plotBrightness(x, 3, br * 30)
                led.plotBrightness(x, 2, br * 15)
            } else {
                if (val <= 200) {
                    led.plotBrightness(x, 4, br * 50)
                    led.plotBrightness(x, 3, br * 40)
                    led.plotBrightness(x, 2, br * 30)
                    led.plotBrightness(x, 1, br * 15)
                } else {
                    led.plotBrightness(x, 4, br * 50)
                    led.plotBrightness(x, 3, br * 45)
                    led.plotBrightness(x, 2, br * 40)
                    led.plotBrightness(x, 1, br * 30)
                    led.plotBrightness(x, 0, br * 15)
                }
            }
        }
    }
}
let s = 0
let seznam: number[] = []
radio.setGroup(1)
seznam = [
50,
150,
250,
150,
50
]
graf(seznam)
