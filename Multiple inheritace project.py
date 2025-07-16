# Project
class Device:
    def __init__(self,brand,battery_level):
        self.brand=brand
        self.battery_level=battery_level

    def show_device_info(self):
        print("Device Brand:",self.brand)
        print("Battery Level:",self.current_battery_level)
    
    def use_battery(self,battery):
        self.battery=battery
        self.current_battery_level=self.battery-self.battery_level

class NetworkEnable:
    def __init__(self):
        self.ip_address=1000.00
        self.connected=False
        print("IP Address:",self.ip_address)

    def connect(self):
        if self.connected==False:
            self.connected=True
            print("Sucessfully Connected",self.connected)
        elif self.connected==True:
            self.connected=False
            print("Not Connected",self.connected)
    
    def sync_data(self):
        if self.connected==True:
            print("Syncronised data sucessfully.")
        else:
            print("Syncronised data unsucessfully.")

class SmartHealthWatch(Device,NetworkEnable):
    def __init__(self,a,b):
        super().__init__(a,b)
        NetworkEnable.__init__(self)
        self.heart_rate=72
        self.steps=0

    def track_steps(self,ste):
        self.ste=0
        self.steps+=ste
        

    def measure_heart_rate(self,rate):
        rate=72
        self.heart_rate+=rate

    def health_summary(self):
        print(f"Steps Walked:{self.steps}. Total:{self.steps}")
        print("Heart Rate Updated:",self.heart_rate)


print("---SMART HEALTH WATCH---")
obj=SmartHealthWatch("Laptop",60)
obj.use_battery(100)
obj.show_device_info()
print("/n")
print("---Information after connection---")
print("==================================")
obj.track_steps(200)
obj.measure_heart_rate(0)
obj.show_device_info()
obj.connect()
obj.sync_data()
obj.health_summary()
