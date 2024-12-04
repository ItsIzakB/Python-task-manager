import Project as pj
import Task as tsk
def main():

    myP = pj.ProjectClass("SWE Intership Grind")

    task1 = tsk.Task('11/23/2025', ' 1500 Applications')

    print(isinstance(task1.get_info()))


if __name__ == 'main': #TODO Need this to work
   main()

