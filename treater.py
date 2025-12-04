import serial # For communicating with Arduino
import time # For sleep

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

        size = str(value).encode()
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=100) # Open serial connection
            time.sleep(2)
            print("serial console opened")
            ser.reset_input_buffer()
            print(size)
            print(ser.write(size)) # Send data
            ser.flush()

            time.sleep(2) # wait a bit

            if ser.in_waiting: # If we heard back...
                data = ser.read(1).decode()
                response = "Gave " + str(data) + " treat(s)" # Read response
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

        
        
                    
