import csv

in_path = '/home/jlsj/JetBrains/PycharmProjects/ocean_result/journal_total/'
out_path = '/home/jlsj/JetBrains/PycharmProjects/ocean_result/journal_year/'
# input_filename = 'aaa_final.csv' #2
# input_filename = 'AIAA.csv' #2
input_filename = 'AICHE_JOURNAL.csv'   #2
# input_filename = 'Applied_Mechanics.csv' #2
# input_filename = 'applied_physics.csv' #2
# input_filename = 'China_OE.csv' #2
# input_filename = 'Hydrodynamics.csv' #2
# input_filename = 'Marine_Science.csv' #2
# input_filename = 'China_Technological.csv' #2

# input_filename = 'Computers_Fluids.csv' #3
# input_filename = 'Computional_Physics.csv' #3
# input_filename = 'Engineering_Structures.csv' #3
# input_filename = 'fluids_and_structures_final.csv' #3
# input_filename = 'OceanEngineering_final.csv' #3
output_filename='AICHE_JOURNAL_2018.csv'
input_file = csv.reader(open(in_path+input_filename,'r',encoding='UTF-8'))
input_list= list(input_file)
# for i in range(0,100):
#     if '2019' in input_list[i][2]:
#         print('2019'+input_list[i][2])
#     else:
#         print(input_list[i][2])

with open(out_path+output_filename, 'a', newline='',encoding='UTF-8') as f:
    writer = csv.writer(f)
    count = 0
    num = 0
    for i in range(0,len(input_list)):
        count =count+1

        if '2018' in input_list[i][2]:
            num = num + 1
            print(num)
            print(input_list[i])
            writer.writerow(input_list[i])
        else:
            pass
