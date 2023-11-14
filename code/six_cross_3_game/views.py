from django.http import HttpResponse
from django.shortcuts import render
from static.grid_6_x_3_game import start_game
from spin.models import Spins


def game(request):
    final = start_game()
    data = {'grid': final}
    win=final[1]
    strip1=final[0][0][0]+','+final[0][1][0]+','+final[0][2][0]
    strip2=final[0][0][1]+','+final[0][1][1]+','+final[0][2][1]
    strip3=final[0][0][2]+','+final[0][1][2]+','+final[0][2][2]
    strip4=final[0][0][3]+','+final[0][1][3]+','+final[0][2][3]
    strip5=final[0][0][4]+','+final[0][1][4]+','+final[0][2][4]
    strip6=final[0][0][5]+','+final[0][1][5]+','+final[0][2][5]

    new_spin = Spins(strip1=strip1,
                     strip2=strip2, strip3=strip3, strip4=strip4, strip5=strip5, strip6=strip6,win=win)
    new_spin.save()

    return render(request, "index.html", data)
