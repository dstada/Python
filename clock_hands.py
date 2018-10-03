# overlaps = (['12:00']['1:05']['2:10']['3:16']['4:21']['5:27']['6:32']['7:38']['8:43']['9:49']['10:54']['00:00'])
overlaps = ("12:00", "1:05", "2:10", "3.16", "4:21", "5:27", "6:32", "7:38", "8:43", "9:49", "10:54", "00:00")
tijd = "13:30"

print(overlaps[0].split(':')[0])
print(overlaps[0].split(':')[1])


startTime = input("Start time as hh:mm ")
endTime = input("End time as hh:mm ")

print("DUs van {} to {} uur.".format(startTime, endTime))
uurverschil = int(endTime.split(':')[0]) -  int(startTime.split(':')[0]) -1
print(uurverschil)

# Overlap times in decimal hours:
overlaps_dec = (0, 1.09083, 2.18194, 3.27277, 4.36361, 5.45472, 6.54555, 7.63638, 8.72722, 9.81833, 10.90917, 12,
                13.09083, 14.18194, 15.27277, 16.36361, 17.45472, 18.54555, 19.63638, 20.72722, 21.81833, 22.90917, 24)

for tijd in overlaps_dec:
    print(tijd)

# Als begintijd < eindtijd (dus tussen 0 en 24):

# 1:00 - 4:00 --> Eerste uit overlaps_dec die groter is dan 1:00 is 1.09083,
# dan doortellen voor elke in overlaps_dec die groter is dan 4:00.



#
# print(overlaps[0].split(':')[0])
# min = int(input("minuten "))
# sec = int(input("seconden "))
#
# print(((min * 60) + sec) / 3600)