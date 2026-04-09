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
        self.mood = 2700

    def turn_on(self, brightness: int = 100):
        self.status = "on"
        self.brightness = brightness

    def turn_off(self):
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


""""Täydennä käyttäjäprofiilit"""
class User:
    def __init__(self):

    def guest(self):
        self.


    def staff(self):
        self.





class Room:
    def __init__(self, light_position: str):
        self.light_position = light_position
        self.lights: dict[str, Light] = {
            "living_room": Light("living_room"),
            "bed": Light("bed"),
            "desk": Light("bed"),
            "entrance": Light("entrance"),
            "bathroom": Light("bathroom")
        }
        self.areas = {
            "bathroom": ["bathroom"],
            "bed": ["bed"],
            "desk": ["desk"],
            "entrance": ["entrance"],
            "living_room": ["living_room"]
        }
        self.guest_present = False

    def enter_room(self, user: str):
        if self.user == user.staff:
            self.lights = "on"
        elif self.user == user.guest:
            self.areas = "entrance"
            lights.status = "on"
    


    def leave_room(self):
        """"Tähän funkio kun poistutaan huoneesta = kaikki valot sammuu"""

    def enter_area(self):
        """"Kun mennään johonkin arealle, vain se valo syttyy"""

    def leave_area(self):
      """"Kun poistutaan arealta, se valo sammuu"""

    def maintenance_status(self):
        """"Simuloidaan vika jossain valossa ja se näkyy sitten vikana huoltoon"""
        



def main():
    """Main CLI interface"""
    print("RoomLight protype simulator")
    print("Commands:")
    print(" user <user>     -Set user for room")
    print(" enter           -Enter room")
    print(" leave           -Leave room")
    print(" enter <area>    -Enter area (bathroom/bed/entrance/desk/living_room)")
    print(" leave <area>    -Lnter area (bathroom/bed/entrance/desk/living_room)")
    print(" mood <mood>     -Set room mood (relax/working/wakeup)")
    print(" reset           -Reset room")
    print(" dashboard       -Sow maintenance dashboard")



if __name__ == "__main__":
    main()