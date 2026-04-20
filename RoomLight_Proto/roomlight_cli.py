"""
RoomLight Prototype - CLI Simulation

This is a prototype for Software production & Architecture - Mini project
Kempowercase

"""

import cmd

class Light:
    def __init__(self, position: str):
        self.position = position
        self.status = "off" # "on", "off", "faulty"
        self.brightness = 0

    def turn_on(self, brightness: int = 100):
        if self.status != "faulty":
            self.status = "on"
            self.brightness = brightness

    def turn_off(self):
        if self.status != "faulty":
            self.status = "off"
            self.brightness = 0

    def set_mood(self, mood: str):
        if self.status == "faulty":
            return
            
        moods = {
            "relax": 30,
            "working": 80,
            "wakeup": 50,
            "night": 10
        }
        if mood in moods:
            self.brightness = moods[mood]
            self.status = "on"

    def set_fault(self):
        self.status = "faulty"
        self.brightness = 0

    def reset_fault(self):
        self.status = "off"
        self.brightness = 0


class Room:
    def __init__(self):
        self.lights: dict[str, Light] = {
            "living_room": Light("living_room"),
            "bed": Light("bed"),
            "desk": Light("desk"),
            "entrance": Light("entrance"),
            "bathroom": Light("bathroom")
        }
        self.occupants = 0
        self.current_user_role = None

    def enter_room(self, role: str):
        self.occupants += 1
        self.current_user_role = role
        
        if role == "staff":
            for light in self.lights.values():
                light.turn_on(100)
            print("Staff entered, Turn on all lights (100%).")
        elif role == "guest":
            self.lights["entrance"].turn_on(100)
            print("Guest entered, turn on entrance light")

    def leave_room(self):
        if self.occupants > 0:
            self.occupants -= 1
            
        if self.occupants == 0:
            for light in self.lights.values():
                light.turn_off()
            self.current_user_role = None
            print("Room is empty, turn off all lights.")
        else:
            print(f"Room still has {self.occupants} person(s)")

    def enter_area(self, area: str):
        if area in self.lights:
            self.lights[area].turn_on(100)
            print(f"You step in '{area}': light on.")
        else:
            print(f"Error: Area '{area}' doesn't exists.")

    def leave_area(self, area: str):
        if area in self.lights:
            self.lights[area].turn_off()
            print(f"Leaved area: '{area}': light off")
        else:
            print(f"Error: Area '{area}' doesn't exist.")

    def set_mood(self, mood: str):
        for light in self.lights.values():
            light.set_mood(mood)
        print(f"Room mood has been set: {mood}")

    def print_visual_map(self):
        """Print ASCII - Floor plan of the room."""
        def get_icon(light_name):
            light = self.lights[light_name]
            if light.status == "faulty":
                return "\033[91m[!]\033[0m" # Punainen
            elif light.status == "on":
                return "\033[93m[*]\033[0m" # Keltainen
            return "[ ]"                    # Harmaa/valkoinen oletus
            
        print("\n=== Floor plan ===")
        print(f"      BATHROOM {get_icon('bathroom')} ")
        print(f"         |         ")
        print(f"       ENTRANCE {get_icon('entrance')} ")
        print(f"         |         ")
        print(f"     LIVING_ROOM {get_icon('living_room')} ")
        print(f"      /       \\   ")
        print(f"BED {get_icon('bed')}     DESK {get_icon('desk')}")
        print("====================\n")

    def print_dashboard(self):
        """Print visual board for maintenance using ANSI-colors"""
        print("\n=== MAINTENANCE DASHBOARD ===")
        print(f"Room Status: {'Occupied' if self.occupants > 0 else 'empty'} (Persons(s): {self.occupants})")
        print(f"User role: {self.current_user_role if self.current_user_role else 'Nobody'}")
        print("-" * 45)
        print(f"{'LIGHT':<15} | {'STATUS':<15} | {'BRIGHTNESS'}")
        print("-" * 45)
        
        for name, light in self.lights.items():
            raw_status = light.status.upper()
            
            # Add ANSI-codes
            # jotta sarakkeet pysyvät suorassa (ANSI-koodit sotkevat len()-funktion)
            if light.status == "faulty":
                status_text = f"\033[91m{raw_status:<15}\033[0m" 
            elif light.status == "on":
                status_text = f"\033[92m{raw_status:<15}\033[0m"           
            else:
                status_text = f"{raw_status:<15}"
                
            print(f"{name:<15} | {status_text} | {light.brightness}%")
        print("-" * 45 + "\n")


class RoomLightCLI(cmd.Cmd):
    intro = "\nRoomLight Prototype started.\nType 'help' or '?' to see the commands"
    prompt = "(RoomLight) "

    def __init__(self):
        super().__init__()
        self.room = Room()

    def do_enter(self, arg):
        """Entering room. Use : enter [guest | staff]"""
        role = arg.strip().lower()
        if role not in ["guest", "staff"]:
            print("Specify role: 'enter guest' or 'enter staff'")
            return
        self.room.enter_room(role)

    def do_leave(self, arg):
        """Leaving room. cmd: leave"""
        self.room.leave_room()

    def do_area_enter(self, arg):
        """Enter area. Use: area_enter [bathroom|bed|desk|entrance|living_room]"""
        self.room.enter_area(arg.strip().lower())

    def do_area_leave(self, arg):
        """Leave area. Use: area_leave [bathroom|bed|desk|entrance|living_room]"""
        self.room.leave_area(arg.strip().lower())

    def do_mood(self, arg):
        """Set mood to room lighting. Use: mood [relax|working|wakeup|night]"""
        mood = arg.strip().lower()
        if mood not in ["relax", "working", "wakeup", "night"]:
            print("Unknown mood. Choices: relax, working, wakeup, night")
            return
        self.room.set_mood(mood)

    def do_map(self, arg):
        """Show ASCII floor plan of the room and visual status of lights."""
        self.room.print_visual_map()

    def do_dashboard(self, arg):
        """Shom maintenance dashboard - Status and faults"""
        self.room.print_dashboard()

    def do_simulate_fault(self, arg):
        """Simulate fault in light. Use: simulate_fault [bathroom|bed|desk|entrance|living_room]"""
        light_name = arg.strip().lower()
        if light_name in self.room.lights:
            self.room.lights[light_name].set_fault()
            print(f"Fault simulated in: {light_name}")
        else:
            print("Where is the fault? Choices: bathroom, bed, desk, entrance, living_room")

    def do_reset_fault(self, arg):
        """Fix fault in light. Use: reset_fault [bathroom|bed|desk|entrance|living_room]"""
        light_name = arg.strip().lower()
        if light_name in self.room.lights:
            self.room.lights[light_name].reset_fault()
            print(f"Fault fixed: {light_name}")
        else:
            print("Reset light where? Choices: bathroom, bed, desk, entrance, living_room")

    def do_exit(self, arg):
        """Exit simulation."""
        print("Closing RoomLight...")
        return True
    
    def default(self, line):
        print(f"Unknown command: '{line}'. Write 'help' for list of commands.")

if __name__ == '__main__':
    RoomLightCLI().cmdloop()
