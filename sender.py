import can
import cantools
import random
import time

# Load DBC file
db = cantools.database.load_file("vehicle.dbc")

# Connect to virtual CAN interface
bus = can.interface.Bus(
    channel="vcan0",
    interface="socketcan"
)

print("Sensor Node Started...")

while True:

    # Generate sensor values
    speed = random.randint(20, 120)
    temp = random.randint(25, 50)

    # Encode signals using DBC
    data = db.encode_message(
        "VehicleData",
        {
            "Speed": speed,
            "Temp": temp
        }
    )

    # Create CAN message
    msg = can.Message(
        arbitration_id=100,
        data=data,
        is_extended_id=False
    )

    # Send message
    bus.send(msg)

    print(f"Sent -> Speed: {speed} km/h, Temp: {temp} °C")

    time.sleep(1)
