import csv

def read_csv():
    with open('users.csv', 'r') as Users:
        reader = csv.reader(Users)
        for row in reader:
            print(row)
    Users.close()
 
def write_csv(Name, Score):
    
    UsersR = open('users.csv', 'r')
    reader = list(csv.reader(UsersR))
    Duplicate = False
    UsersR.close()
    
    for i in range(len(reader)):
        if Name == reader[i][0]:
            Duplicate = True
            reader[i][1]=Score
    if not Duplicate:
        reader += [[Name, Score]]
    with open('users.csv','w', newline = '') as Users:
        writer = csv.writer(Users)
        writer.writerows(reader)
    Users.close()
def clear_csv():
    with open('users.csv', 'w', newline = '') as Users:
        writer = csv.writer(Users)
        writer.writerow(["Name","Score"])
    Users.close()
