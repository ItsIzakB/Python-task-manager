import Project as pj
import Task as tsk
def main():

    myP = pj.ProjectClass("SWE Internship Grind")

    task1 = tsk.Task('11/23/2025', ' 1500 Applications')

    task2 = tsk.Task('04/12/2025', 'LowCalProj Finish')

    print(isinstance(task1))

    myP.addTask(task1)

    myP.addTask(task2)

    for task in myP:
        task.get_info()



if __name__ == 'main': #TODO Need this to work
   main()

