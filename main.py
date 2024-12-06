import Project as pj
import Task as tsk
def main():

    myP = pj.ProjectClass("SWE Internship Grind")

    print(myP.get_proj_name())

    task1 = tsk.TaskClass('11/23/2025', ' 1500 Applications')
    task2 = tsk.TaskClass('04/12/2025', 'LowCalProj Finish')
    task3 = tsk.TaskClass('04/12/2025', '100 Connections')

    task1.add_atrs('non-urgent')

    print(type(task1))
    
    myP.add_task(task1)
    myP.add_task(task2)
    

    for task in myP:
        print(type(task))
        task.get_info()

if __name__ == '__main__':
    main()
