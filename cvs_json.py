import csv

def read_csv():
    with open('users.csv', 'r') as Users:
        reader = csv.reader(Users)
        for row in reader:
            print(row)
    Users.close()
 
def write_csv(Name, Score):
    with open('users.csv','a', newline = '') as Users:
        writer = csv.writer(Users)
        writer.writerow([Name, Score])
    Users.close()

def clear_csv():
    with open('users.csv', 'w', newline = '') as Users:
        writer = csv.writer(Users)
        writer.writerow(["Name","Score"])
    Users.close()
