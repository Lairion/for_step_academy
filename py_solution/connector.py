from tuya_iot import TuyaOpenAPI, AuthType
from setting import (
    ENDPOINT,
    ACCESS_ID,
    ACCESS_KEY,
    USERNAME,
    PASSWORD
)


class TuyaConnector():
    
    def __init__(self) -> None:
        # Initialization of tuya openapi	
        self.openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)	
        print(self.openapi)
        print(self.openapi.connect(USERNAME, PASSWORD))
        
    def make_device_command(self, device_id:str, command_dict:dict) -> bool:
        result = self.openapi.post(
            f'/v1.0/iot-03/devices/{device_id}/commands',
            {"commands": [command_dict]}
        )
        print(result)
        return result["success"]