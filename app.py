import os
from flask import Flask, request,render_template
from datetime import date

app = Flask(__name__)

today = date.today().strftime("%m_%d_%y")
today2=date.today().strftime("%d_%B_%Y")

if "tasks.txt" not in os.listdir("."):
    with open("tasks.txt","w") as f:
        f.write('')


def get_task():
    with open('tasks.txt', 'r') as f:
        task_list = f.readlines()
    return task_list

def create_new_task():
    os.remove('tasks.txt')
    with open('tasks.txt','w') as f:
        f.write("")

def update_task(task):
    os.remove('tasks.txt')
    with open('tasks.txt','w') as f:
        for i in range(len(task)):
            f.write (str(task[i]))


#*****************Routes***************

@app.route('/')
def home():
    #return render_template('home.html',today2=today2,tasklist=get_task(),l=len(get_task()))
    return render_template('home.html')

@app.route('/clear')
def clear_list():
    create_new_task()              
    return render_template('home.html',today2=today2,tasklist=get_task(),l=len(get_task())) 

@app.route('/addtask', methods=['POST'])
def add_task():
    task = request.form.get('newtask')
    with open('tasks.txt','a') as f:
        f.writelines(str(task)+'\n')
    return render_template('home.html',today2=today2,tasklist=get_task(),l=len(get_task())) 

@app.route('/deltask', methods=['GET'])
def remove_task():
    task_index = int(request.args.get("deltaskid"))
    task_list = get_task()
    print(task_index)
    print(task_list)
    if task_index < 0 or task_index >len(task_list):
        return render_template('home.html',today2=today2,tasklist=get_task(),l=len(get_task()),mess= "Invalid Index") 
    else :
        removed_task = task_list.pop(task_index)
    update_task(task_list)
    return render_template('home.html',today2=today2,tasklist=get_task(),l=len(get_task())) 


if __name__=='__main__ ':
    app.run(debug = True)

