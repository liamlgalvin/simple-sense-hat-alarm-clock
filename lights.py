import colours

class Lights:
    def __init__(self, sense_hat):
        self.sense_hat = sense_hat
        self.colour = colours.orange
        self.intensity = 4
        self.lights_on = True
        self.set_lights()

    def __str__(self):
        return f"Sense HAT Object: \nColor: {self.colour}\nIntensity: {self.intensity}\nLights On: {self.lights_on}"

    def resetLights(self):
        for i in range(8):
            for j in range(8):
                print()
                #self.sense_hat.set_pixel(i, j, colours.nothing)

    def set_lights(self):
        self.resetLights()

        if self.lights_on == False:
            return

        for i in range(self.intensity * 2):
            for j in range(8):
                print()
                #self.sense_hat.set_pixel(i, j, self.colour)

    def change_colour(self, new_colour):
        self.colour = new_colour
        self.set_lights()
    

    def change_intensity(self, new_intensity):
        if new_intensity < 1 or new_intensity > 4:
            print(self, "intensity must be between 1 and 4")
            return
    
        self.intensity = new_intensity
        self.set_lights()

    def inc_intensity(self):
        self.change_intensity(self.intensity + 1)

    def dec_intensity(self):
        self.change_intensity(self.intensity - 1)

    def toggle_lights_on(self):
        self.lights_on = not(self.lights_on)
        self.set_lights()
    