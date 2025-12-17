import binascii
import machine

class MCU:
    
    @staticmethod
    def unique_id(self):
        """
        获取MCU唯一ID
        """
        return binascii.hexlify(machine.unique_id()).decode().upper()
