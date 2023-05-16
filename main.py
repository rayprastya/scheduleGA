import prettytable 
from datetime import datetime, timedelta
from schedule import Schedule
from genetic import GeneticOptimize


def vis(schedule):
    """visualization Class Schedule.

    Arguments:
        schedule: List, Class Schedule
    """
    # 7 ke kanan
    # 7 kebawah

    start_time = datetime.strptime("07:00", "%H:%M")  # Set the initial start time
    col_labels = ['kelas/jam']

    increment = timedelta(minutes=50)  # Set the increment value

    for _ in range(90):
        col_labels.append(start_time.strftime("%H:%M"))  # Append the current time to the list
        start_time += increment  # Increment the time by 50 minutes

    table_vals = [[i + 4] + ['']*90 for i in range(7)]

    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = 'id kelas: {} \n jenis kelas: {} \n room: {} \n matkul: {}'.format(s.classRoomId, s.categoryId, s.roomId, s.courseId)
        table_vals[weekDay - 1][slot] = text

    for row in table_vals:
        table.add_row(row)

    print(table)


if __name__ == '__main__':
    schedules = []

    # add schedule
    schedules.append(Schedule(201, "biasa", "METODOLOGI PENELITIAN"))
    schedules.append(Schedule(201, "biasa", "SISTEM OPERASI"))
    schedules.append(Schedule(202, "biasa", "PEMROGRAMAN VISUAL "))
    schedules.append(Schedule(202, "biasa", "FINANCIAL TECHNOLOGY"))
    schedules.append(Schedule(203, "biasa", "REKAYASA PERANGKAT LUNAK"))
    schedules.append(Schedule(203, "biasa", "INTERAKSI MANUSIA"))
    schedules.append(Schedule(206, "biasa", "E-BUSINESS"))
    schedules.append(Schedule(206, "biasa", "PROYEK KONSULTANSI"))

    schedules.append(Schedule(202, "khusus", "METODE NUMERIK"))
    schedules.append(Schedule(202, "khusus", "SISTEM KONTROL"))
    schedules.append(Schedule(204, "khusus", "TEKNIK SIMULASI "))
    schedules.append(Schedule(204, "khusus", "TEKNIK RISET OPERASI"))
    schedules.append(Schedule(206, "khusus", "SISTEM OPERASI"))
    schedules.append(Schedule(206, "khusus", "SOSIAL DAN INOVASI MEDIA"))

    schedules.append(Schedule(201, "khusus", "METODOLOGI PENELITIAN"))
    schedules.append(Schedule(201, "khusus", "SISTEM OPERASI"))
    schedules.append(Schedule(202, "khusus", "PEMROGRAMAN VISUAL"))
    schedules.append(Schedule(202, "khusus", "FINANCIAL TECHNOLOGY"))
    schedules.append(Schedule(203, "biasa", "REKAYASA PERANGKAT LUNAK"))
    schedules.append(Schedule(203, "biasa", "INTERAKSI MANUSIA "))
    schedules.append(Schedule(206, "biasa", "E-BUSINESS"))
    schedules.append(Schedule(206, "biasa", "PROYEK KONSULTANSI"))

    # schedules.append(Schedule(203, "biasa", ""))
    # schedules.append(Schedule(203, "biasa", ""))
    # schedules.append(Schedule(204, "biasa", ""))
    # schedules.append(Schedule(204, "biasa", ""))
    # schedules.append(Schedule(205, "biasa", ""))
    # schedules.append(Schedule(205, "biasa", ""))
    # schedules.append(Schedule(206, "biasa", ""))
    # schedules.append(Schedule(206, "biasa", ""))

    # optimization
    ga = GeneticOptimize(popsize=50, elite=10, maxiter=100)
    res = ga.evolution(schedules, 3)

    # visualization
    vis_res = []
    for r in res:
        print("id ruangan", r.categoryId)
        print("class", r.classRoomId)
        print("matkul", r.courseId)

        print("room", r.roomId)
        print("weekday", r.weekDay)
        print("slot", r.slot)

        print("===============\n")
        # if r.classId == "eksekutif":
        #     vis_res.append(r)
        vis_res.append(r)
    vis(vis_res)
