# 🏭 This is our fake industrial machine (like a PLC).
# It just sits and waits for someone to connect and ask for data.

from pymodbus.server.sync import StartTcpServer  # Starts the Modbus server
from pymodbus.device import ModbusDeviceIdentification  # Lets us describe the server
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext  # Creates memory storage
from pymodbus.datastore import ModbusSequentialDataBlock  # Lets us store numbers in order
import logging  # Shows messages in the terminal so we know what’s happening

# Turn on logging so we can see messages like "server started"
logging.basicConfig()

# 🧠 Create some memory for our fake machine to use
# These are like drawers where we store numbers. All are set to 0 to start.
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0]*100),  # Coils
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0]*100)   # Input Registers
)

# We tell the server: "This is your storage to use"
context = ModbusServerContext(slaves=store, single=True)

# 📛 Give our server a fake ID like it's a real device
identity = ModbusDeviceIdentification()
identity.VendorName = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'Modbus Server'
identity.MajorMinorRevision = '1.0'

# 🚪 Start the server on your computer, listening at port 5020
# It's like opening the door and waiting for a client to knock.
StartTcpServer(context, identity=identity, address=("localhost", 5020))
