from abc import ABC, abstractmethod

# Abstract Class
class SmartDevice(ABC):

    @abstractmethod
    def command(self):
        pass


# Subclass 1
class SmartLight(SmartDevice):

    def command(self):
        return "💡 Smart Light: Turning on the lights."


# Subclass 2
class SmartFan(SmartDevice):

    def command(self):
        return "🌀 Smart Fan: Setting fan speed to medium."


# Subclass 3
class SmartSpeaker(SmartDevice):

    def command(self):
        return "🔊 Smart Speaker: Playing your favorite music."


# Function demonstrating polymorphism
def control_device(device):
    print(device.command())


# Create objects
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()

# Store objects in a list
devices = [light, fan, speaker]

print("=== Smart Device Command Center ===\n")

# Call the same method on different objects
for device in devices:
    control_device(device)