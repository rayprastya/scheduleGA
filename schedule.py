import numpy as np


class Schedule:
    """Class Schedule.
    """
    def __init__(self, classRoomId, categoryId, courseId):
        """Init
        Arguments:
            classRoomId: int, unique flight id.
            categoryId: int, unique class id.
            courseId: int, unique destination id.
        """
        self.classRoomId = classRoomId
        self.categoryId = categoryId
        self.courseId = courseId

        self.roomId = 0
        self.weekDay = 0
        self.slot = 0

    def random_init(self, roomRange):
        """random init.

        Arguments:
            roomSize: int, number of classrooms.
        """
        self.roomId = np.random.randint(1, roomRange + 1, 1)[0]
        self.weekDay = np.random.randint(1, 8, 1)[0]
        self.slot = np.random.randint(1, 8, 1)[0]


def schedule_cost(population, elite):
    """calculate conflict of class schedules.

    Arguments:
        population: List, population of class schedules.
        elite: int, number of best result.

    Returns:
        index of best result.
        best conflict score.
    """
    conflicts = []
    n = len(population[0])

    for p in population:
        conflict = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # print(p[i].courseId, p[j].courseId)
                # check flight in same time and same room 
                if p[i].roomId == p[j].roomId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    # print("ini konfliknya", p[i].roomId,  p[j].roomId)
                    conflict += 1
                # check flight for one class in same time
                if p[i].categoryId == p[j].categoryId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check flight for one destination in same time
                # if p[i].courseId == p[j].courseId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                #     conflict += 1
                # check same flight for one class in same day
                if p[i].categoryId == p[j].categoryId and p[i].classRoomId == p[j].classRoomId and p[i].weekDay == p[j].weekDay:
                    conflict += 1

        conflicts.append(conflict)

    index = np.array(conflicts).argsort()

    return index[: elite], conflicts[index[0]]
