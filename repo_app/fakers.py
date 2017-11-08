from loremipsum import get_sentences
from django.contrib.auth.models import User
from .models import Project, Task, Category, Membership
import random


def all():
    users = User.objects.all()
    for i in users:
        print i.first_name, i.last_name

def gen_projects():
    # get the adjectives
    adjs = []
    f = open('adjective-list.txt', 'r')
    for line in f:
        s = line.rstrip('\n')
        adjs.append(s)
    f.close()

    # get the nouns
    nouns = []
    f = open('noun-list.txt', 'r')
    for line in f:
        s = line.rstrip('\n')
        nouns.append(s)
    f.close()

    # get sentences
    sentences_list = get_sentences(len(adjs))

    print len(adjs), len(nouns), len(sentences_list)

    for i in adjs:
        t = i + nouns[random.randint(0, len(nouns)-1)]
        d = sentences_list[random.randint(0, len(sentences_list)-1)]
        p = Project(title=t, description=d)
        p.save()

    # projects = Project.objects.all()

def gen_tasks():
    cats = Category.objects.all()
    projs = Project.objects.all()

    for project in projs:
        num_tasks = random.randint(1, 10) 
        for future_task in range(num_tasks):
            t = "TASK " + str(future_task+1)
            d = get_sentences(1)
            c = cats[random.randint(0,3)]
            task = Task(title=t, description=d, order=future_task, project=project, category=c)
            task.save()


def gen_cats():
    # preparation, implementation, deployment, and data analysis
    c = Category(label='preparation')
    c.save()
    c = Category(label='implementation')
    c.save()
    c = Category(label='deployment')
    c.save()
    c = Category(label='data analysis')
    c.save()

    cats = Category.objects.all()
    for i in cats: print i.label


def gen_membership():
    # for each project
    projs = Project.objects.all()
    users = User.objects.all()

    for i in projs:
        num_mems = random.randint(1, 3)
        for j in range(num_mems):
            owner = (j == 0)
            rand_user = random.randint(0, users.count()-1)
            m = Membership(member=users[rand_user], project=i, is_owner=owner)
            m.save()












