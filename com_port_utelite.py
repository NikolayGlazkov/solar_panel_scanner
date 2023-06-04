from serial.tools import list_ports # отоброжение всех компортов
my_list = list_ports.comports()

for i in my_list:
    print(list(i))


# ser = serial.Serial('COM5', 9600)

# data = ser.read()
# print(data)