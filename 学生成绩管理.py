# 此项目运行结果，可在公共场所展示
# 先定义一个存储学生信息的字典，232XXX为键，关联的值是具有两个键（name，grades）值对的字典
students = {
    '23201013129': {'name': 'Peter', 'grades': {'语文': 89, '数学': 45, '英语': 77, 'Python': 64, 
                                                 '化学': 93, '物理': 17, 'MySQL': 50}},
    '23201013126': {'name': 'Alex', 'grades': {'语文': 20, '数学': 17, '英语': 21, 'Python': 75, 
                                                 '化学': 41, '物理': 90, 'MySQL': 50}},
    '23201013127': {'name': 'Warren', 'grades': {'语文': 97, '数学': 60, '英语': 93, 'Python': 91, 
                                                 '化学': 64, '物理': 10, 'MySQL': 89}},
    '23201013128': {'name': 'Rock', 'grades': {'语文': 74, '数学': 80, '英语': 85, 'Python': 91, 
                                                 '化学': 100, '物理': 100, 'MySQL': 90}}
}
print()
print('学生信息如下：')
for key, value in students.items():  # 逐行输出学生信息
    print(f'{key}:{value}')
    print()

# 添加成绩 （接收四个参数，以下同理）
def add_grade(students, student_id, course, grade):
# 判断在下方调用该函数时，输入的学生id在不在字典中
    if student_id in students:
        students[student_id]['grades'][course] = grade
    else:
        print("学生信息未找到。")

# 修改成绩
def update_grade(students,student_id, course, grade):

    # 判断下方调用函数中，输入的学生ID和课程是否存在于字典中
    if student_id in students and course in students[student_id]['grades']:
        students[student_id]['grades'][course] = grade
    else:
        print("学生信息或课程未找到。")

# 查看成绩的函数
def view_grades(students, student_id, name):
    """ 括号中students参数是必要的，它代表存储学生信息的字典，当调用view_grades函数时，需要传递这个字典，
        函数才能访问和处理特定学生的信息
    student_id是要查看成绩的特定学生的id
    name是与student_id对应的名字
      调用view_grades函数时，需要告诉它在哪个学生字典中查找，
      哪个学生的成绩需要被查看，并且获取到的信息与字典中对应的信息（输入的姓名是否对应字典中的姓名）是否匹配。
      如果没有students参数，函数就不知道去哪里查找学生的成绩 """

    # 下方调用查看成绩函数时，输入的学生ID和学生姓名，是否与字典中的相匹配
    if student_id in students and students[student_id]['name'] == name:
        print(f"\n{name} 的成绩如下：")
        for course, grade in students[student_id]['grades'].items():
            print(f"{course}: {grade}")
    else:
        print("\n学生信息不匹配或未找到。")

# 定义打印所有学生信息函数，并按学号升序排序
def print_stu(students):
    for student_id in sorted(students):   # 遍历排序后的学生ID  sorted：升序（小-大），若在括号中students后加上 reverse=True，就是降序
        student_info = students[student_id]
        print(f"学号： {student_id}, 姓名：{student_info['name']}, 成绩：{student_info['grades']}")

#定义成绩统计函数
def grade_statistics(students):
    # 初始化课程成绩统计字典
    course_statistics = {}
    
    # 遍历学生信息，统计每门课程的成绩分布
    for student_id, student_info in students.items():
        for course, grade in student_info['grades'].items():
            if course not in course_statistics:
                course_statistics[course] = {"不及格": 0, "及格": 0, "中等": 0, "良好": 0, "优秀": 0}
            
            # 根据成绩划分等级
            if grade < 60:
                course_statistics[course]["不及格"] += 1
            elif 60 <= grade < 70:
                course_statistics[course]["及格"] += 1
            elif 70 <= grade < 80:
                course_statistics[course]["中等"] += 1
            elif 80 <= grade < 90:
                course_statistics[course]["良好"] += 1
            elif grade >= 90:
                course_statistics[course]["优秀"] += 1
    
    return course_statistics

# 函数一定要在被调用之前去定义，一般函数的定义写在文件顶部或主函数之前，因为在主函数中会调用函数，保证在调用之前就定义好


# 主函数
# 作用：控制程序的流程：main函数通常包含程序的主要逻辑，它调用其他函数，并根据用户的输入或其他事件控制程序的流程
#      模块化：将程序的启动逻辑放在main函数中，可以将代码作为模块导入到其他文件中
# 例如：在其他文件中把这个文件作为模块导入进去，直接使用 import 语句(导入到的某个文件与该文件在同一级目录下)  如：import test  即可访问这个模块中定义的所有函数和变量
# import后的模块名，只能包含数字、字母、下划线
# 若调用 添加成绩函数，需要先 import test 再调用 import test.add_grade(students, '004','数学',95)
# 若不在同一级目录下，需要使用 sys.path.append()添加模块所在的目录到搜索路径  例如：sys.path.append('D:/projects/school_system')
""" 
import sys
sys.path.append('/path/to/your/module/directory')
import test
 """
# 若只想导入模块中的特定函数，而不是整个模块，使用from ... import ...
# 导入添加成绩函数和修改成绩函数   如： from test import add_grade, update_grade
def main():

    # 主循环，作用是处理用户的输入信息
    while True:
        # 获取用户输入的信息，进行判断
        choice = input("\n输入1进入教师系统，输入2进入学生系统，输入sorted_id输出按学号排序后的学生信息，按esc退出：")

        # 如果获取的信息是1，进入教师系统循环
        if choice == '1':
            # 教师系统，内嵌三个判断条件（三个循环）
            # 获取教师系统中，输入的信息
            teacher_choice = input("\n输入a添加成绩，输入r修改成绩，输入s进行统计，按esc退出：")

            # 添加成绩
            if teacher_choice == 'a':
                # 获取输入的信息
                student_id = input("\n请输入学生学号：")
                course = input("请输入课程名称：")
                grade = float(input("请输入成绩："))
                add_grade(students, student_id, course, grade)  # 调用上方添加成绩函数，再通过获取用户的信息，获取三个参数
            # 注意判断条件的等级，要在教师系统循环中，不能与主循环同级
            # 修改成绩，逻辑与 添加成绩同理   
            elif teacher_choice == 'r':                
                student_id = input("\n请输入学生学号：")
                course = input("请输入课程名称：")
                new_grade = float(input("请输入新成绩：")) # 将输入的内容转换为浮点数
                update_grade(students, student_id, course, new_grade)

            # 统计成绩
            elif teacher_choice == 's':
                statistics = grade_statistics(students)
                for course, distribution in statistics.items():
                    print()
                    print(f"{course} 成绩分布：")
                    
                    for grade_category, count in distribution.items():
                        print(f"{grade_category}: {count}人")
            # 获取信息为esc，跳出教师系统循环，回到主循环，继续通过输入信息进行判断    
            elif teacher_choice == 'esc':
                break

        # 主函数中的学生系统部分
        elif choice == '2':
        # 学生系统

            stu_choice = input("\n当前已进入学生系统\n输入'check'查看成绩, 输入'esc'退出：")
            if stu_choice == 'check':
                student_id = input('\n请输入学生学号：')
                name = input('请输入学生姓名：')
                view_grades(students, student_id, name)
                    
                # 退出学生系统
            elif stu_choice == 'esc':
                continue  
        # 主循环中，获取的输入信息是esc，则退出整个循环
        elif choice == 'esc':
            break

        # 排序，调用上方排序函数
        elif choice == 'sorted_id':
            print()
            print('排列后的信息如下：')
            print_stu(students)  # 调用函数

        continue
    
if __name__ == "__main__":
    main()
"""用于判断当前的模块是被直接运行还是被导入到其他的模块中，可以把它当作一个检查点
例如：当直接运行该文件时，则下面的main（）函数将被执行
若文件被导入到另一个文件中，将不会执行main（）函数，防止了在导入时不必要的代码运行
如果想在导入模块后被直接运行main函数，可以在导入模块的文件中调用main函数 如：import test.main(),与上方注释中，调用函数同理 """
