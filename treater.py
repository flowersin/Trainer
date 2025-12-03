import serial # For communicating with Arduino
global response
response = "Fuck my life"


class Treater:
    def __init__(self):
        pass

    def treat(self, reason):
        match reason:
            case "small":
                return self.small()
            case "medium":
                return self.medium()
            case "large":
                return self.large()
    
    def small(self):
        return self.send(1)

    def medium(self):
        return self.send(2)

    def large(self):
        return self.send(3)

    def send(self, value):
        print("attempting to send treat")

        size = int(value)
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # Open serial connection
            print("serial console opened")

            ser.write(size) # Send data

            delay(1000) # wait a bit

            waiting = ser.in_waiting # Check if we got a response
            if waiting > 0: # If we heard back...
                data = ser.read(1)
                response = "Gave " + str(data) + " treats" # Read response
            else: # If we didn't...
                response = "No Reply"
    
        except serial.SerialException as e:
            response = f"Serial port error: {e}"
        except PermissionError:
            response = "Permission denied - check user permissions"
        except FileNotFoundError:
            response = "Port not found - verify device connection"
        finally:
            if 'ser' in locals() and ser.is_open:
                ser.close()
            print(response)
            return response

        
        
                    
