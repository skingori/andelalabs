UPWARDS = 1
DOWNWARDS = 1
print("Please Enter Floor Number ")
FLOOR_NUMBER = input()


class LiftWork(object):
    def __init__(self):
        self.to_floor = None
        self.callbacks = None

    def on_press(self, floor, direction):

        self.to_floor = floor

    def on_selected_floor(self, floor):

        self.to_floor = floor

    def on_changed_floor(self):

        if self.to_floor == self.callbacks.this_floor:
            self.callbacks.motor_direction = None

    def when_ready(self):

        if self.to_floor > self.callbacks.this_floor:
            self.callbacks.motor_direction = UPWARDS
            print("Lift is going Up")

        elif self.to_floor < self.callbacks.this_floor:
            self.callbacks.motor_direction = DOWNWARDS
            print("Lift is going down")

        else:
            print("Error,press alarm for assistance")
