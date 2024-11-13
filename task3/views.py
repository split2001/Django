from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'third_task/platform.html')


def game(request):
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay'
    context = {'game1': game1,
               'game2': game2,
               'game3': game3
               }
    return render(request, 'third_task/games.html', context)


def cart(request):
    return render(request, 'third_task/cart.html')


def platform(request):
    return render(request, 'third_task/platform.html')
