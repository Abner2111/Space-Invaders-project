import json
import csv
class CSV:
    def __init__(self):
        pass
    def read_csv(self):
        with open('data/users.csv', 'r') as Users:
            reader = csv.reader(Users)
            for row in reader:
                print(row)
        Users.close()


    def write_csv(self, Name, Score):

        UsersR = open('data/users.csv', 'r')
        reader = list(csv.reader(UsersR))
        Duplicate = False
        UsersR.close()

        '''for i in range(len(reader)):
            if Name == reader[i][0]:
                Duplicate = True
                reader[i][1]=Score'''
        reader = self.check_dupl(reader, Name, Score, Duplicate, len(reader), 0)[0]
        Duplicate = self.check_dupl(reader, Name, Score, Duplicate, len(reader), 0)[1]
        if not Duplicate:
            reader += [[Name, Score]]
        with open('data/users.csv','w', newline = '') as Users:
            writer = csv.writer(Users)
            writer.writerows(reader)
        Users.close()

    def check_dupl(self, Mat, name, score, duplicate,n, i):
        if i == n or duplicate:
            return Mat, duplicate
        elif name == Mat[i][0]:
            if int(Mat[i][1]) < score:
                Mat[i][1] = score
            duplicate = True
            return self.check_dupl(Mat, name, score, duplicate, n, i+1)
        else:
            return self.check_dupl(Mat, name, score, duplicate, n, i+1)


    def clear_csv(self):
        with open('data/users.csv', 'w', newline = '') as Users:
            writer = csv.writer(Users)
            writer.writerow(["Name","Score"])
        Users.close()


    def ordenar_csv(self):
        UsersR = open('data/users.csv', 'r')
        reader = list(csv.reader(UsersR))[1:] #pasa el archivo csv a una lista menos el titulo
        return self.selectSort(reader, len(reader), 0)

    def selectSort(self, arr, n, i):
        if i == n:
            return arr
        else:
            min_inx=i
            min_inx2=self.selectSort_Aux(arr, n, i+1, min_inx)
            arr[i],arr[min_inx2]=arr[min_inx2], arr[i]
            return self.selectSort(arr, n, i+1)

    def selectSort_Aux(self, arr, n, j, cont):
        if j<n:
            if arr[cont][1]< arr[j][1]:

                return self.selectSort_Aux(arr, n, j+1, j)
            else:
                return self.selectSort_Aux(arr, n, j+1, cont)
        else:
            return cont

    def save_to_json():
        top = dict(ordenar_csv()[:5]) #convierte a diccionario una lista ordenada en orden de puntuacion de usuarios, con los primeros 5 elementos
        Json = open('data/top_users.json', 'w')
        json.dump(top, Json)




