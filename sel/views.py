from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
import random
import time
# Create your views here.

class Games:
    def __init__(shelf):
        shelf.H = 6
        shelf.W = 6

        shelf.name = ''
        shelf.count = 0
        shelf.turn = 0
        shelf.who = {}
        spell = 'abcdefghijklmnopqrstuvwx'
        shelf.board = spell*2

        shelf.params = {
        'title':shelf.name,
        'user':[],
        'board':shelf.board,
        'entry':0,
        'turn':{},
        'color':{},
        'acount':{},
        'point':{},
        'get':{},
        'all_get':{},
        'che':{},
        'before':{},
        'before_x':{},
        'before_y':{},
        'group':[],
        'group_num':0,
        'member_num':{},
        'next_player':[],
        'wait':0,
    }

    def all_check(shelf, user, mem):
        shelf.params['message'] = 'check_def'
        if len(shelf.params['all_get'][user]) != 0:
            shelf.params['message'] = 'check_if'
            for i in range(shelf.H):
                for j in range(shelf.W):
                    cot = 0
                    for mass in shelf.params['all_get'][user]:
                        if mass == shelf.params['acount'][user][i][j]:
                            shelf.params['che'][user][i][j] = mass
                            cot = 1
                            break

                    if cot == 0:
                        shelf.params['che'][user][i][j] = '*'

        else:
            shelf.params['message'] = 'check_else'
            for i in range(shelf.H):
                for j in range(shelf.W):
                    shelf.params['che'][user][i][j] = '*'

        try:
            for enemy in shelf.params['group'][mem]:
                shelf.params['che'][enemy] = shelf.params['che'][user].copy()

        except:
            a = 'None'


    def cot(shelf, req):
        user_check = str(req.user)

        if req.method == 'POST':

            if 'hit' in req.POST:
                hw = str(req.POST['hit']).split('/')
                height = int(hw[0])
                width = int(hw[1])

                shelf.params['before_y'][user_check].append(height)
                shelf.params['before_x'][user_check].append(width)

                shelf.params['message'] = 'hit'
                shelf.params['height'] = str(height)
                shelf.params['width'] = str(width)

                mass = shelf.params['acount'][user_check][height][width]
                shelf.params['word'] = mass

                if shelf.params['turn'][user_check] == 1:
                    shelf.params['turn'][user_check] = 2
                    shelf.params['before'][user_check] = mass
                    shelf.params['che'][user_check][height][width] = mass

                elif shelf.params['turn'][user_check] == 2:
                    shelf.params['che'][user_check][height][width] = mass
                    shelf.params['message'] = 'double'

                    if shelf.params['before'][user_check] == mass:
                        shelf.params['get'][user_check].append(mass)
                        shelf.params['all_get'][user_check].append(mass)
                        mem = shelf.params['member_num'][user_check]

                        try:
                            for enemy in shelf.params['group'][mem]:
                                shelf.params['all_get'][enemy] = shelf.params['all_get'][user_check].copy()
                                shelf.params['che'][enemy] = shelf.params['che'][user_check].copy()

                        except:
                            a = 'None'

                        shelf.params['turn'][user_check] = 100

                    else:
                        shelf.params['turn'][user_check] = 3


            elif 'load' in req.POST:
                shelf.params['message'] = 'load'
                if 3 <= shelf.params['turn'][user_check]:

                    shelf.params['message'] = 'loads'
                    shelf.params['before'][user_check] = '*'
                    shelf.params['turn'][user_check] = 0

                    mem = int(shelf.params['member_num'][user_check])
                    many = len(shelf.params['group'][mem])

                    shelf.all_check(user_check, mem)

                    shelf.params['before_y'][user_check] = []
                    shelf.params['before_x'][user_check] = []

                    shelf.params['message'] = 'loads2'

                    for i in range(many):
                        shelf.params['message'] = 'loads3'
                        if shelf.params['group'][mem][i] == user_check:
                            if i == many-1:
                                shelf.params['next_player'][mem] = shelf.params['group'][mem][0]

                            else:
                                shelf.params['next_player'][mem] = shelf.params['group'][mem][i+1]

                    next_player = shelf.params['next_player'][mem]
                    shelf.params['turn'][next_player] = 1

            else:
                shelf.params['message']='None'
                return redirect(to='/sel/ans')

        return redirect(to='/sel/ans')

    def ans(shelf, req):
        return render(req, 'sel/ans.html', shelf.params)

    def look(shelf, req):
        return render(req, 'sel/look.html', shelf.params)


    def all_logout(shelf, req):
        user_check = str(req.user)

        shelf.params['entry'] -= 1
        shelf.params['turn'].pop(user_check)
        shelf.params['user'].remove(user_check)
        shelf.params['get'].pop(user_check)
        shelf.params['all_get'].pop(user_check)
        shelf.params['before'].pop(user_check)
        shelf.params['before_y'].pop(user_check)
        shelf.params['before_x'].pop(user_check)

        try:
            shelf.params['enemy'].pop(user_check)
            return redirect(to='/sel/login')

        except:
            return redirect(to='/sel/login')


        try:
            mem = shelf.params['member_num'][user_check]
            shelf.params['group'][mem].pop(user_check)
            return redirect(to='/sel/login')

        except:
            return redirect(to='/sel/login')

        return redirect(to='/sel/login')


    def signup(shelf, req):
        #user_check = req.user
        shelf.params['username'] = 'sel'
        if req.method == 'POST':
            username = req.POST['username_data']
            password = req.POST['password_data']
            print('username=', username, 'password=', password)
            try:
                user = User.objects.create_user(username, '', password)
                shelf.params['username'] = 'just recomend'

            except IntegrityError:
                shelf.params['username'] = 'already'

        return render(req, 'sel/signup.html', shelf.params)

    def login(shelf, req):
        if req.method == 'POST':
            username_data = req.POST['username_data']
            password_data = req.POST['password_data']
            user = authenticate(req, username=username_data, password=password_data)

            if user is not None:
                if username_data in shelf.params['user']:
                    return redirect(to='/sel/login')

                else:
                    shelf.params['user'].append(username_data)
                    login(req, user)

                    shu = ''.join(random.sample(shelf.board, len(shelf.board)))

                    cell = [[] for i in range(shelf.H)]
                    k = 0
                    for i in range(shelf.H):
                        for j in range(shelf.W):
                            cell[i].append(shu[k])
                            k += 1


                    shelf.params['acount'][str(username_data)] = cell.copy()
                    shelf.params['get'][str(username_data)] = []
                    shelf.params['before'][str(username_data)] = '*'

                    shelf.params['before_x'][str(username_data)] = []
                    shelf.params['before_y'][str(username_data)] = []

                    shelf.params['all_get'][str(username_data)] = []

                    check = [['*'] * shelf.W for i in range(shelf.H)]
                    shelf.params['che'][str(username_data)] = check.copy()

                    shelf.params['entry']+=1

                    if shelf.params['wait'] == 2:
                        goal_time = time.time()

                        if goal_time - shelf.params['start_time'] < 60:
                            shelf.params['turn'][str(username_data)] = 0

                            entry_a = str(shelf.params['user'][shelf.params['entry']-3])
                            entry_b = str(shelf.params['user'][shelf.params['entry']-2])
                            entry_c = str(shelf.params['user'][shelf.params['entry']-1])


                            shelf.params['acount'][entry_c] = shelf.params['acount'][entry_b].copy()
                            shelf.params['che'][entry_c] = shelf.params['che'][entry_b].copy()
                            shelf.params['all_get'][entry_c] = shelf.params['all_get'][entry_b].copy()

                            shelf.params['wait'] += 1


                            shelf.params['member_num'][str(username_data)] = shelf.params['group_num']
                            shelf.params['group'][shelf.params['group_num']].append(str(username_data))
                            shelf.params['group_num'] += 1

                        else:
                            shelf.params['wait'] = 0
                            shelf.params['turn'][str(username_data)] = 1
                            shelf.params['wait'] += 1


                            shelf.params['group'].append([str(username_data)])
                            shelf.params['group_num'] += 1
                            shelf.params['member_num'][str(username_data)] = shelf.params['group_num']
                            shelf.params['next_player'].append([str(username_data)])


                    elif shelf.params['wait'] == 0:
                        shelf.params['turn'][str(username_data)] = 1
                        shelf.params['wait'] += 1


                        shelf.params['group'].append([str(username_data)])
                        shelf.params['member_num'][str(username_data)] = shelf.params['group_num']
                        shelf.params['next_player'].append([str(username_data)])


                    elif shelf.params['wait'] == 1:
                        shelf.params['turn'][str(username_data)] = 0

                        entry_a = str(shelf.params['user'][shelf.params['entry']-2])
                        entry_b = str(shelf.params['user'][shelf.params['entry']-1])


                        shelf.params['acount'][entry_b] = shelf.params['acount'][entry_a].copy()
                        shelf.params['che'][entry_b] = shelf.params['che'][entry_a].copy()
                        shelf.params['all_get'][entry_b] = shelf.params['all_get'][entry_a].copy()


                        shelf.params['wait'] += 1
                        shelf.params['start_time'] = time.time()


                        shelf.params['member_num'][str(username_data)] = shelf.params['group_num']
                        shelf.params['group'][shelf.params['group_num']].append(str(username_data))


                    if shelf.params['wait'] == 3:
                        shelf.params['wait'] = 0

                    return redirect(to='/sel/ans')

        return render(req, 'sel/login.html', shelf.params)

    def loc(shelf, req):
        if req.method == 'POST':
            username = req.POST['username_data']
            password = req.POST['password_data']

            if username == 'XXX':
                if password == 'XXX':
                    shelf.params['pass'] = 'OK'
                    return redirect(to='/sel/look')

            return redirect(to='/sel/loc')

        return render(req, 'sel/loc.html', shelf.params)
