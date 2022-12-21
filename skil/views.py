from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from skil.models import Equestion, Nquestion, Epercent, Npercent

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.
lst_n=[]

def index(request):
    global lst_n
    lst_n=random.sample(range(1, 51), k=10)
    return render(request, 'skil/index.html')

def exceltest(request):
    if request.method == 'GET':
        excel = Equestion.objects.filter(pk__in=lst_n)
        data = {'excel':excel}
        return render(request, 'skil/excel_test.html', data)
    elif request.method == 'POST':
        op_lst=['option0','option1','option2','option3','option4','option5','option6','option7','option8','option9']
        ans_lst=[]
        your_ans=[]
        xs=[0,1,2,3,4,5,6,7,8,9]
        #ans = request.POST.get("option0")
        excel = Equestion.objects.filter(pk__in=lst_n)
        excela = list(excel.values())
        lst=[]
        cnt=0
        lst_e=['A', 'B', 'C']
        for ex in excela:
            lst.append(ex["answer"])
        for op in op_lst:
            ans = request.POST.get(op)
            your_ans.append(ans)
        for n in range(10):
            exc=Epercent.objects.get(pk=lst_n[n])
            if your_ans[n] == lst[n]:
                ans_lst.append('正解')
                exc.true += 1
                exc.save()
                cnt+=1
            else:
                ans_lst.append('不正解')
                exc.false += 1
                exc.save()
            exc.percent = (exc.true/(exc.true+exc.false))*100
            exc.save()
            if cnt>=9:
                eva=lst_e[0]
            elif cnt>=4:
                eva=lst_e[1]
            else:
                eva=lst_e[2]
        return render(request, 'skil/Eanswer.html', {'yans':your_ans, 'ans':ans_lst, 'excel':excela, 'xs':xs, 'cnt':cnt, 'eva':eva})
        

def nettest(request):
    if request.method == 'GET':
        net = Nquestion.objects.filter(pk__in=lst_n)
        data = {'net':net}
        return render(request, 'skil/net_test.html', data)
    elif request.method == 'POST':
        op_lst=['option0','option1','option2','option3','option4','option5','option6','option7','option8','option9']
        ans_lst=[]
        your_ans=[]
        #ans = request.POST.get("option0")
        net = Nquestion.objects.filter(pk__in=lst_n)
        neta = list(net.values())
        lst=[]
        cnt=0
        lst_e=['A', 'B', 'C']
        for nt in neta:
            lst.append(nt["answer"])
        for op in op_lst:
            ans = request.POST.get(op)
            your_ans.append(ans)
        for n in range(10):
            net=Npercent.objects.get(pk=lst_n[n])
            if your_ans[n] == lst[n]:
                ans_lst.append('正解')
                net.true += 1
                net.save()
                cnt+=1
            else:
                ans_lst.append('不正解')
                net.false += 1
                net.save()
            net.percent = (net.true/(net.true+net.false))*100
            net.save()
            if cnt>=9:
                eva=lst_e[0]
            elif cnt>=4:
                eva=lst_e[1]
            else:
                eva=lst_e[2]
        return render(request, 'skil/Nanswer.html', {'yans':your_ans, 'ans':ans_lst, 'net':neta, 'cnt':cnt, 'eva':eva})

def Eanswer(request):
    #if request.method == 'GET':
    excel = Equestion.objects.filter(pk__in=lst_n)
    data = {'excel':excel}
    return render(request, 'skil/Eanswer.html', data)

def Nanswer(request):
    net = Nquestion.objects.filter(pk__in=lst_n)
    data = {'net':net}
    return render(request, 'skil/Nanswer.html', data)

def epercent(request):
    excels = Equestion.objects.all()
    paginator = Paginator(excels, 10) # 1ページに10件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    excel = paginator.get_page(p) # 指定のページのArticleを取得

    per=Epercent.objects.all()
    paginator = Paginator(per, 10)
    percent = paginator.get_page(p)
    return render(request, 'skil/epercent.html', {'excel': excel, 'p': p, 'percent':percent})
    
def npercent(request):
    nets = Nquestion.objects.all()
    paginator = Paginator(nets, 10) # 1ページに10件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    net = paginator.get_page(p) # 指定のページのArticleを取得

    per=Npercent.objects.all()
    paginator = Paginator(per, 10)
    percent = paginator.get_page(p)
    return render(request, 'skil/npercent.html', {'net': net, 'p': p, 'percent':percent})