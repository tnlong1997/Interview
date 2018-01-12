
class Elevator:

    def __init__(self, index, curr_floor, dest_floor, direction):
        self.index = index
        self.curr_floor = curr_floor
        self.direction = direction

    def getCurrentFloor(self):
        return self.curr_floor

    def getDirection(self):
        return self.direction

    def getIndex(self):
        return self.index

    def getDestination(self):
        return self.dest_floor

    def updateDestination(self, dest_floor):
        if (self.direction < 0 and self.dest_floor > dest_floor):
            self.dest_floor = dest_floor
        elif (self.direction > 0 and self.dest_floor < dest_floor):
            self.dest_floor = dest_floor
        elif (self.direction == 0):
            self.dest_floor = dest_floor
            if (self.dest_floor > self.curr_floor):
                self.direction = 1
            elif (self.dest_floor < self.curr_floor):
                self.direction = -1
        return self.dest_floor

    def update(self):

        self.curr_floor = self.curr_floor + self.direction
        if (self.curr_floor == self.dest_floor):
            self.direction = 0
            self.dest_floor = -1
        return self.curr_floor

    def __print__(self):
        if (self.direction == 0):
            state = "standing"
        elif (self.direction == 1):
            state = "going up"
        else:
            state = "going down"
        print("Elevator number %d is at floor %d and is %s" % (self.index,
                                                               self.curr_floor,
                                                               state))


class Request:

    def __init__(self, index, curr_floor, dest_floor):
        self.curr_floor = curr_floor
        self.dest_floor = dest_floor

    def getCurrentFloor(self):
        return self.curr_floor

    def getDestination(self):
        return self.dest_floor

    def getIndex(self):
        return self.index

def find_elevator(curr, dest):
    found = False
    elevator_index = 0
    if (curr > dest):
        # Find nearest going down elevator
        found = False
        for i in range(0, m):
            if (elevators[i].direction < 0 and elevators[i].getCurrentFloor >= curr):
                if not found or elevators[elevator_index].getCurrentFloor > elevators[i].getCurrentFloor:
                    elevator_index = i
                    found = True
        if not found:
            # Find nearest standing elevator
            for i in range(0, m):
                if (elevators[i].direction == 0):
                    if not found or elevators[elevator_index].getCurrentFloor > elevators[i].getCurrentFloor:
                        elevator_index = i
                        found = True

    elif (curr < dest):
        found = False
        for i in range(0, m):
            if (elevators[i].direction > 0 and elevators[i].getCurrentFloor <= curr):
                if not found or elevators[elevator_index].getCurrentFloor < elevators[i].getCurrentFloor:
                    elevator_index = i
                    found = True
        if not found:
            # Find nearest standing elevator
            for i in range(0, m):
                if (elevators[i].direction == 0):
                    if not found or elevators[elevator_index].getCurrentFloor < elevators[i].getCurrentFloor:
                        elevator_index = i
                        found = True

    return (found, elevator_index)


def simulator():
    inp = input("Enter number of floors: ")
    n = int(inp)
    inp = input("Enter number of elevators: ")
    m = int(inp)

    elevators = []

    for i in range(0, m):
        elevators = elevators.append(Elevator(i, 0, 0))

    time = 0
    requests = []
    inp = input("Enter action at time %d" % time)
    while (inp != "End"):
        curr, dest = inp.split(" ", 2)
        curr = int(curr)
        dest = int(dest)
        requests.append(Request(Request(time, curr, dest)))

        for request in requests:
            found, elevator_index = find_elevator(request.getCurrentFloor(), request.getDestination())
            elevators[elevator_index].updateDestination()
            if found:
                print("Request %d requests elevator %d" % (request.getIndex(), elevator_index))
                requests.remove(request)

        for i in range(0, m):
            elevators[i].update()


elevators = []
simulator()
