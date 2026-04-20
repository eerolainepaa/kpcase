"""
RoomLight Prototype - CLI Simulation

This is a prototype for Software production & Architecture - Mini project
Kempowercase

9.4 - Tässä on runko tähän tehtävään, saa täydentää ja korjata / Jooel
"""


class Light:
    def __init__(self, position: str):
        self.position = position
        self.status = "off" # On, Off, faulty
        self.brightness = 0

    def turn_on(self, brightness: int = 100):
        if self.status != "faulty":
            self.status = "on"
            self.brightness = brightness

    def turn_off(self):
        if self.status != "faulty":
            self.status = "off"
            self.brightness = 0

    def mood(self, mood = str):
        moods = {
            "relax": {"brightness": 30},
            "working": {"brightness": 80},
            "wakeup": {"brightness": 50}
        }
        if mood in moods:
            self.brightness = moods[mood]["brightness"]
            self.status = "on"

    def fault(self):
        self.status = "faulty"
        self.brightness = 0


class Room:
    def __init__(self):
        self.current_user = None
        self.current_area = None
        self.current_mood = None
        self.lights: dict[str, Light] = {
            "living_room": Light("living_room"),
            "bed": Light("bed"),
            "desk": Light("desk"),
            "entrance": Light("entrance"),
            "bathroom": Light("bathroom")
        }

    def set_user(self, user: str):
        if user in ["staff", "guest"]:
            self.current_user = user
            print(f"User has been set: {user}\n")
        else:
            print(f"Unknown user, use 'staff' or 'guest'\n")

    def enter_room(self):
        if self.current_user == "staff":
            for light in self.lights.values():
                light.turn_on()
                self.current_area = "all"
            print(" Staff entered, turn all lights on (100%)\n")
        elif self.current_user == "guest":
            self.lights["entrance"].turn_on()
            self.current_area = "entrance"
            print("Guest entered room. Turn entrance ON\n")
        else:
            print("Error, Set user first at command 'user <guest/staff>'\n")
    

    def leave_room(self):
        for light in self.lights.values():
            light.turn_off()
        print("Room is empty, turning all lights off\n")
        self.current_area = None

    def enter_area(self, area: str):
            """"When entering area, that light turns on"""
            if area in self.lights:
                if self.current_area and self.current_area != area:
                    self.lights[self.current_area].turn_off()
                    print(f"Turning light off from previous area: {self.current_area}\n")
                
                if self.current_mood:
                    self.lights[area].mood(self.current_mood)
                else:
                    self.lights[area].turn_on()
                
                current_brightness = self.lights[area].brightness
                print(f"Entered area: {area}: light ON, brightness {current_brightness}%\n")
                
            self.current_area = area


    def set_room_mood(self, mood: str):
            valid_moods = ["relax", "working", "wakeup"]
            if mood in valid_moods:
                self.current_mood = mood

                if self.current_area and self.current_area != "all":
                    self.lights[self.current_area].mood(mood)
                    print(f"Room mood has been set to: {mood}\n")
            else:
                print(f"Error, Invalid mood. Use: {valid_moods}\n")

    def maintenance_status(self):
        """"simulate fault and show it in maintenace dashboard"""
        print("\n=== MAINTENANCE DASHBOARD ===")
        for name, light in self.lights.items():
            status_text = light.status.upper()

            if light.status == "faulty":
                status_text = "FAULTY"
            print(f" - {name:<12} | Status: {status_text:<8} | Brightness: {light.brightness}%")
        print("=============================\n")

    def trigger_fault(self, area: str):
        if area in self.lights:
            self.lights[area].fault()
            print(f"Light has broken in area: {area}\n")


    def reset_room(self):
        self.current_area = None
        self.current_mood = None
        self.current_user = None

        for light in self.lights.values():
            light.status = "off"
            light.brightness = 0
        print("Room has been reseted to default\n")

def print_help():
    print("\nAvailable commands:")
    print(" user <staff/guest>  - Set user role for the room")
    print(" enter           -Enter room")
    print(" leave           -Leave room")
    print(" enter <area>    -Enter area (bathroom/bed/entrance/desk/living_room)")
    print(" mood <mood>     -Set room mood (relax/working/wakeup)")
    print(" reset           -Reset room")
    print(" dashboard       -Sow maintenance dashboard")

def main():
    """Main CLI interface"""
    print("RoomLight protype simulator")
    print("Commands:")
    print(" user <staff/guest>  - Set user role for the room")
    print(" enter           -Enter room")
    print(" leave           -Leave room")
    print(" enter <area>    -Enter area (bathroom/bed/entrance/desk/living_room)")
    print(" mood <mood>     -Set room mood (relax/working/wakeup)")
    print(" reset           -Reset room")
    print(" dashboard       -Sow maintenance dashboard")

    room = Room()

    while True:
        try:
            command = input("Command: ").strip().lower().split()
            if not command:
                continue
            
            cmd = command[0]
            args = command[1:] if len(command) > 1 else []

            if cmd == "quit":
                print("Prototype CLI ended, Goodbye\n")
                break

            elif cmd == "help":
                print_help()

            elif cmd == "user":
                if args:
                    room.set_user(args[0])
                else:
                    print("ERROR give user: user <guest/staff>\n")

            elif cmd == "enter":
                if args:
                    room.enter_area(args[0])
                else:
                    room.enter_room()
                    
            elif cmd == "leave":
                room.leave_room()
                    
            elif cmd == "mood":
                if args:
                    room.set_room_mood(args[0])
                else:
                    print("ERROR. Set the mood: mood <relax/working/wakeup>\n")

            elif cmd == "reset":
                room.reset_room()
                    
            elif cmd == "dashboard":
                room.maintenance_status()
                
            elif cmd == "break":
                if args:
                    room.trigger_fault(args[0])
                else:
                    print("ERROR give area that breaks: break <area>\n")
                    
            else:
                print(f"ERROR Unknown error '{cmd}'. type 'help' to see cmds.\n")
                
        except Exception as e:
            print(F"Error: {e}")


if __name__ == "__main__":
    main()