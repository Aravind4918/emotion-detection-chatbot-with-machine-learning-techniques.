

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *
from .tf import tf
from .tf2 import tf2
from .Prediction import Prediction
from django.db.models import F


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

# Create your views here.
def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.GET['aid']
    pwd=request.GET['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})

def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def signup(request):
    return render(request, 'signup.html')

def usignupaction(request):
    name=request.POST['name']
    mail=request.POST['mail']
    ph=request.POST['ph']
    pwd=request.POST['pwd']
    age=request.POST['age']
    gen=request.POST['gen']
    addr=request.POST['addr']
    
    print(name, mail, addr)
    d=users(name=name, email=mail, ph=ph, pwd=pwd, age=age, gen=gen, addr=addr, statu=0)
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    return render(request, 'signup.html',{'msg':'Registration is done !!'})



def viewusers(request):
    d=users.objects.all()
    
    print(list(d))
    for d1 in d:
        print(d1.name, d1.email, d1.ph, d1.gen)
    
    return render(request, 'viewusers.html',{'data':d})

    
def searchusers(request):

    keys=request.POST['keys']

    d=users.objects.filter(name__contains=keys).all()
    
    print(list(d))
    for d1 in d:
        print(d1.name, d1.email, d1.ph, d1.gen)
    
    return render(request, 'viewusers.html',{'data':d})

    


def ulogin(request):




    
    return render(request, 'user.html')

def userloginaction(request):

    uid=request.POST['mail']
    pwd=request.POST['pwd']

    d=users.objects.filter(email=uid).filter(pwd=pwd).count()
    
    print(d)

    if d==1:
        d=users.objects.filter(email=uid).all()
        name=''
        for d1 in d:
            name=d1.name
        request.session['email'] = uid
        request.session['name'] = name
        return render(request, 'userhome.html')
    else:
        return render(request, 'user.html', {'msg':'Login Fail'})


    

def userlogout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def userhome(request):
    if "email" in request.session:
        return render(request, 'userhome.html')
    else:
        return render(request, 'user.html')

def viewp(request):
    if "email" in request.session:
        email=request.session['email']
        d=users.objects.filter(email=email).all()
        return render(request, 'profile.html',{'data':d})


        
    else:
        return render(request, 'user.html',{'msg':'session expired'})


def training(request):
    return render(request, 'training.html')
def testing(request):
    return render(request, 'testing.html')
def prediction(request):
    return render(request, 'prediction.html')



def knntrain(request):
    from .KNNTrain import KNNTrain
    KNNTrain.train()

    return render(request, 'training.html', {'msg':"KNN Algorithm's training completed"})

def nbtrain(request):
    from .NBTrain import NBTrain
    NBTrain.train()

    return render(request, 'training.html', {'msg':"Naive Bayes Algorithm's training completed"})

def rftrain(request):
    from .RFTrain import RFTrain
    RFTrain.train()

    return render(request, 'training.html', {'msg':"Random Forest Algorithm's training completed"})

def svmtrain(request):
    from .SVMTrain import SVMTrain
    SVMTrain.train()

    return render(request, 'training.html', {'msg':"SVM Algorithm's training completed"})

def nntrain(request):
    from .NNTrain import NNTrain
    NNTrain.train()

    return render(request, 'training.html', {'msg':"Neural Networks Algorithm's training completed"})


def test(request):
    from .Testing import Testing
    file=request.POST['file']
    knn=Testing('knn_model.sav',file)
    nb=Testing('nb_model.sav',file)
    rf=Testing('rf_model.sav',file)
    nn=Testing('nn_model.sav',file)
    svm=Testing('svm_model.sav',file)


    d=accval.objects.all()
    d.delete()

    d=accval(alg_name='KNN', sc1=knn[0],sc2=knn[1],sc3=knn[2],sc4=knn[3])
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    

    d=accval(alg_name='NB', sc1=nb[0],sc2=nb[1],sc3=nb[2],sc4=nb[3])
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    

    d=accval(alg_name='RF', sc1=rf[0],sc2=rf[1],sc3=rf[2],sc4=rf[3])
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    

    d=accval(alg_name='NN', sc1=nn[0],sc2=nn[1],sc3=nn[2],sc4=nn[3])
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    

    d=accval(alg_name='SVM', sc1=svm[0],sc2=svm[1],sc3=svm[2],sc4=svm[3])
    d.save() # insert into users valyes(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
    



    return render(request, 'testing.html', {'msg':"Testing process is completed !!"})



def viewacc(request):

    d=accval.objects.all()
    val=dict({})
    for d1 in d:
        val[d1.alg_name]=d1.sc1

    from .Graphs import viewg
    viewg(val)
    return render(request, 'viewacc.html', {'data': d})




def predictionact(request):
    from .Prediction import Prediction
    st=request.POST['st']
    rs=Prediction.do(st)

    rs="Your Emotion is: "+rs
    
    return render(request, 'prediction.html', {'msg':rs})

def addq(request):
    if "adminid" in request.session:
        d = queries.objects.all()
        
        return render(request, 'queries.html', {'data': d})

    else:
        return render(request, 'admin.html')




def addquery(request):
    q=request.POST['q']
    a=request.POST['a']
    
        
    d=queries(q_n=q,an_s=a)
    d.save()
    
    d = queries.objects.all()
    return render(request, 'queries.html', {'data': d,'msg':'Query Added.'})


def chatpage(request):
    
    chat.objects.all().delete()
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data': d})


def chataction(request):
    message=request.POST['message']
    uemail=request.session["email"]
    uname=request.session["name"]
    d=chat(name='user',email=uemail,message=message)
    d.save()


    ans='Sorry, Not Understood'

    cid=tf.calc(message)
    if cid!=-1:
        d=queries.objects.filter(id__exact=cid)
        for d1 in d:
            ans=d1.an_s

        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()

        d=chat.objects.filter().all()
        return render(request, 'chat.html',{'data': d})

    
    else:
        
        r=Prediction.do(message)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',r)
        request.session['mood']=r


        
        if r=='joy':
            pass
        else:
            users.objects.filter(email = uemail).update(statu=F('statu')+1)
        if r=='joy':
            ans="Good to know, to enhance your mood go with following link"
            d=chat(name='chatbot',email='chatbot',message=ans)
            d.save()
            request.session['type']='c'
            d=chat.objects.filter().all()
            return render(request, 'chat.html',{'data': d,'bt':True})


        else:
            d=users.objects.filter(email = uemail)
            for d1 in d:

                if int(d1.statu)>3:
                    print('Consult')
                    ans="I'm Sorry, Based on your situation You need to consult therapist. Please go with following URL"
                    d=chat(name='chatbot',email='chatbot',message=ans)
                    d.save()
                    request.session['type']='t'
                    d=chat.objects.filter().all()
                    return render(request, 'chat.html',{'data': d,'bt':True})
                else:
                    print('Content')
                    if r=='anger':
                        ans="Control your angry,Please go with following URL"

                    elif r=='fear':
                        ans="Don't fear, Please go with following URL"
                    
                    d=chat(name='chatbot',email='chatbot',message=ans)
                    d.save()
                    request.session['type']='c'
                    
                    d=chat.objects.filter().all()
                    return render(request, 'chat.html',{'data': d,'bt':True})




def moredetails(request):

    t=request.session['type']
    if t=='t':
        d=tdetails.objects.filter().all()
        return render(request, 'therapist.html',{'data': d})
    else:
        r=request.session['mood']
        d=content.objects.filter(category=r).filter(d_type='image').all()
        i=[]
        for d1 in d:
            d1=d1.data
            i.append(d1)

        d=content.objects.filter(category=r).filter(d_type='music').all()
        m=[]
        for d1 in d:
            d1=d1.data
            m.append(d1)


        d=content.objects.filter(category=r).filter(d_type='video').all()
        v=[]
        for d1 in d:
            d1=d1.data
            v.append(d1)


        return render(request, 'viewdata.html',{'i': i, 'm':m, 'v':v})
    return render(request, r)



def adddata(request):
    if request.method=='POST':
        cat=request.POST['cat']
        t_ype=request.POST['t_ype']
        title=request.POST['title']
        data=request.POST['data']
        

        d=content(category=cat,d_type=t_ype,title=title,data=data)
        d.save()

        d=content.objects.filter().all()
        return render(request, 'adddata.html',{'data': d})

    else:
        d=content.objects.filter().all()
        return render(request, 'adddata.html',{'data': d})

def addt(request):
    if request.method=='POST':
        name=request.POST['name']
        qua=request.POST['qua']
        addr=request.POST['addr']
        city=request.POST['city']
        

        d=tdetails(name=name,qualification=qua,address=addr,city=city)
        d.save()

        d=tdetails.objects.filter().all()
        return render(request, 'addt.html',{'data': d})

    else:
        d=tdetails.objects.filter().all()
        return render(request, 'addt.html',{'data': d})
