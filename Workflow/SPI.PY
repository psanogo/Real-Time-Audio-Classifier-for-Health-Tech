import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Function to read from a specific ADC channel
def read_channel(channel):
    # MCP3008 command: [start, single-ended, channel, 0, 0]
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        # Read from channel 0
        value = read_channel(0)
        print(f"Raw ADC Value: {value}")
        time.sleep(0.5)
except KeyboardInterrupt:
    spi.close()
    print("SPI connection closed.")
