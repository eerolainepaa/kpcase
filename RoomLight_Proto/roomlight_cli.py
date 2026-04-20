import cmd

class Light:
    def __init__(self, position: str):
        self.position = position
        self.status = "off" # Vaihtoehdot: "on", "off", "faulty"
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
            print("Henkilökunta saapui: Kaikki valot sytytetty (100%).")
        elif role == "guest":
            self.lights["entrance"].turn_on(100)
            print("Vieras saapui: Eteisen valo sytytetty.")

    def leave_room(self):
        if self.occupants > 0:
            self.occupants -= 1
            
        if self.occupants == 0:
            for light in self.lights.values():
                light.turn_off()
            self.current_user_role = None
            print("Huone on tyhjä: Kaikki valot sammutettu.")
        else:
            print(f"Huoneessa on vielä {self.occupants} henkilöä.")

    def enter_area(self, area: str):
        if area in self.lights:
            self.lights[area].turn_on(100)
            print(f"Astuttu alueelle '{area}': Valo sytytetty.")
        else:
            print(f"Virhe: Aluetta '{area}' ei löydy.")

    def leave_area(self, area: str):
        if area in self.lights:
            self.lights[area].turn_off()
            print(f"Poistuttu alueelta '{area}': Valo sammutettu.")
        else:
            print(f"Virhe: Aluetta '{area}' ei löydy.")

    def set_mood(self, mood: str):
        for light in self.lights.values():
            light.set_mood(mood)
        print(f"Huoneen teemaksi asetettu: {mood}")

    def print_visual_map(self):
        """Tulostaa huoneen ASCII-pohjapiirroksen."""
        def get_icon(light_name):
            light = self.lights[light_name]
            if light.status == "faulty":
                return "\033[91m[!]\033[0m" # Punainen
            elif light.status == "on":
                return "\033[93m[*]\033[0m" # Keltainen
            return "[ ]"                    # Harmaa/valkoinen oletus
            
        print("\n=== POHJAPIIRROS ===")
        print(f"      KYLPYHUONE {get_icon('bathroom')} ")
        print(f"         |         ")
        print(f"       ETEINEN {get_icon('entrance')} ")
        print(f"         |         ")
        print(f"     OLOHUONE {get_icon('living_room')} ")
        print(f"      /       \\   ")
        print(f"SÄNKY {get_icon('bed')}     TYÖPÖYTÄ {get_icon('desk')}")
        print("====================\n")

    def print_dashboard(self):
        """Tulostaa visuaalisen taulukon huollolle ANSI-väreillä."""
        print("\n=== HUOLLON OHJAUSPANEELI ===")
        print(f"Huoneen tila: {'Varattu' if self.occupants > 0 else 'Tyhjä'} (Henkilöitä: {self.occupants})")
        print(f"Käyttäjärooli: {self.current_user_role if self.current_user_role else 'Ei ketään'}")
        print("-" * 45)
        print(f"{'VALO':<15} | {'TILA':<15} | {'KIRKKAUS'}")
        print("-" * 45)
        
        for name, light in self.lights.items():
            raw_status = light.status.upper()
            
            # Lisätään ANSI-koodit, mutta tehdään pad/tasaus raakatekstille
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
    intro = "\nRoomLight Prototyyppi käynnistetty.\nKirjoita 'help' tai '?' nähdäksesi komennot."
    prompt = "(RoomLight) "

    def __init__(self):
        super().__init__()
        self.room = Room()

    def do_enter(self, arg):
        """Astutaan huoneeseen. Käyttö: enter [guest|staff]"""
        role = arg.strip().lower()
        if role not in ["guest", "staff"]:
            print("Määritä rooli: 'enter guest' tai 'enter staff'")
            return
        self.room.enter_room(role)

    def do_leave(self, arg):
        """Poistutaan huoneesta. Käyttö: leave"""
        self.room.leave_room()

    def do_area_enter(self, arg):
        """Mennään tietylle alueelle. Käyttö: area_enter [bathroom|bed|desk|entrance|living_room]"""
        self.room.enter_area(arg.strip().lower())

    def do_area_leave(self, arg):
        """Poistutaan tietyltä alueelta. Käyttö: area_leave [bathroom|bed|desk|entrance|living_room]"""
        self.room.leave_area(arg.strip().lower())

    def do_mood(self, arg):
        """Asetetaan valaistusteema koko huoneeseen. Käyttö: mood [relax|working|wakeup|night]"""
        mood = arg.strip().lower()
        if mood not in ["relax", "working", "wakeup", "night"]:
            print("Tuntematon teema. Vaihtoehdot: relax, working, wakeup, night")
            return
        self.room.set_mood(mood)

    def do_map(self, arg):
        """Näyttää huoneen ASCII-pohjapiirroksen ja valojen visuaalisen tilan."""
        self.room.print_visual_map()

    def do_dashboard(self, arg):
        """Näyttää huollon ohjauspaneelin (Status ja viat)."""
        self.room.print_dashboard()

    def do_simulate_fault(self, arg):
        """Simuloi vian halutussa valossa. Käyttö: simulate_fault [bathroom|bed|desk|entrance|living_room]"""
        light_name = arg.strip().lower()
        if light_name in self.room.lights:
            self.room.lights[light_name].set_fault()
            print(f"Vika simuloitu valossa: {light_name}")
        else:
            print("Valoa ei löydy. Vaihtoehdot: bathroom, bed, desk, entrance, living_room")

    def do_reset_fault(self, arg):
        """Korjaa vian halutussa valossa. Käyttö: reset_fault [bathroom|bed|desk|entrance|living_room]"""
        light_name = arg.strip().lower()
        if light_name in self.room.lights:
            self.room.lights[light_name].reset_fault()
            print(f"Vika korjattu valosta: {light_name}")
        else:
            print("Valoa ei löydy. Vaihtoehdot: bathroom, bed, desk, entrance, living_room")

    def do_exit(self, arg):
        """Sulkee simulaation."""
        print("Suljetaan RoomLight...")
        return True
    
    def default(self, line):
        print(f"Tuntematon komento: '{line}'. Kirjoita 'help' nähdäksesi listan komennoista.")

if __name__ == '__main__':
    RoomLightCLI().cmdloop()
