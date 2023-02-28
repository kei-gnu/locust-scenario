#from locust import HttpUser, task, between
import csv
import random
tasks = []
with open("sinario.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i in reader:
        tasks.append(i[1:])
lentasks = len(tasks)


class MyUser(HttpUser):
    wait_time =constant(1)
    
    @task
    def task(self):
        k = random.randint(0, lentasks)
        l =  [x[2:-2].split("', '") for x in tasks[k] if not x == '']
        for i in l:
            if i[0] == "GET":
                self.client.get(i[1])
            elif i[0] == "POST":
                self.client.post(i[1])
            elif i[0] == "HEAD":
                self.client.get(i[1])
            else:
                continue
