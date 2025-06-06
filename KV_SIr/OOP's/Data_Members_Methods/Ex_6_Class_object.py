# this program is used to read the student records from file
# by using un-pickling with Classes and Objects
import pickle,sys
class StudentUnPick:
    def get_stu_records(self):
        try:
            with open("student.txt",'rb') as fp:
                print("------ Student Record -------")
                while True:
                    try:
                        obj = pickle.load(fp)
                        obj.dis_stu_data()
                    except EOFError:
                        print("="*50)
                        sys.exit()
        except FileNotFoundError:
            print("Don't Exist This File ")


# main program
sup = StudentUnPick()
sup.get_stu_records()
