import can
import cantools

# Load DBC file
db = cantools.database.load_file("vehicle.dbc")

# Connect to virtual CAN interface
bus = can.interface.Bus(
    channel="vcan0",
    interface="socketcan"
)

print("ECU Node Listening...")

while True:

    msg = bus.recv()

    if msg.arbitration_id == 100:

        # Decode CAN message
        decoded = db.decode_message(
            100,
            msg.data
        )

        speed = decoded["Speed"]
        temp = decoded["Temp"]

        print("\nReceived Vehicle Data")
        print(f"Speed : {speed} km/h")
        print(f"Temp  : {temp} °C")

        # ECU decision logic
        if speed > 80:
            print("⚠ WARNING: Overspeed Detected!")

        if temp > 40:
            print("⚠ WARNING: High Temperature!")

        print("-" * 30)
