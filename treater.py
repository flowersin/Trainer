import serial # For communicating with Arduino

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
        except serial.SerialException as e:
            response = f"Serial port error: {e}"
        except PermissionError:
            response = "Permission denied - check user permissions"
        except FileNotFoundError:
            response = "Port not found - verify device connection"
        finally:
            if 'ser' in locals() and ser.is_open:
                ser.close()
            print("response")
            return response

        print("serial console opened")
        ser.write(size) # Send data

        response = "Gave " + str(ser.readline()) + " treats" # Read response

        ser.close() # Close connection
        print("response")
        return response

        
        
                    
