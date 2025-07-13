# 🎮 This is the controller that connects to our fake factory machine
# It asks for some numbers, and then changes one

from pymodbus.client.sync import ModbusTcpClient  # The tool we use to connect
import logging  # To show messages in the terminal

# Turn on logging so we can see what's going on
logging.basicConfig()

# 🤝 Connect to the machine on the same computer (localhost) using port 5020
client = ModbusTcpClient('localhost', port=5020)
client.connect()

# 📥 Ask the machine: "What are the first 5 numbers in your memory?"
result = client.read_holding_registers(0, 5, unit=1)  # Start at address 0, read 5 registers
print("Read holding registers:", result.registers)  # Show what we got

# ✍️ Say: "Change register 1 to the number 123"
client.write_register(1, 123, unit=1)
print("Wrote 123 to register 1")

# 👋 All done, say goodbye
client.close()
