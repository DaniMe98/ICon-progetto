# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:29:16 2020

@author: Danilo
"""

from sklearn.datasets import load_iris
import pylab as pl
from sklearn.metrics import auc



dataset=load_iris()

X=dataset['data']
y=dataset['target']

def category_name(nuovo_test):  #output nome della categoria (virginica,setosa,versicolor)
    if nuovo_test==0:
        categoria1= dataset.target_names[0]
    elif nuovo_test==1:
        categoria1= dataset.target_names[1]
    else:
        categoria1= dataset.target_names[2]  
    return categoria1        




def pr_curve(pred,y_test,pred_SV,pred_knn):
        #definizione variabili
        precision=[]
        precision_SV=[]
        precision_knn=[]   
        
        recall=[]
        recall_SV=[]
        recall_knn=[]
        k=0
        
        #calcolo P-R per ogni predizione per il KNN
        for d in range(pred_knn.size):
            if(pred_knn[d]==y_test[d]):
                if d==0:
                    precision_knn.append(1)
                    k=k+1
                else:    
                    precision_knn.append((k/d)) #precisione =True Positive/(False Positive+True positive)
                    k=k+1
            else: 
                if d==0:
                    precision_knn.append(0)
                else:    
                    precision_knn.append(k/d) 
            recall_knn.append(k/pred_knn.size) #recall= True Positive/(True Positive+False Negative)
        
        k=0
        #calcolo P-R per ogni predizione per l'SVM
        for d in range(pred_SV.size):
            if(pred_SV[d]==y_test[d]):
                if d==0:
                    precision_SV.append(1)
                    k=k+1

                else:    
                    precision_SV.append((k/d))
                    k=k+1
            else: 
                if d==0:
                    precision_SV.append(0)
                else:    
                    precision_SV.append(k/d) 
            recall_SV.append(k/pred_SV.size)
        #calcolo P-R per ogni predizione per l'albero di decisione
        k=0
        for d in range(pred.size):
            if(pred[d]==y_test[d]):
                if d==0:
                    precision.append(1)
                    k=k+1
                else:    
                    precision.append((k/d))
                    k=k+1
            else: 
                if d==0:
                    precision.append(0)
                else:    
                    precision.append(k/d) 
            recall.append(k/pred.size)
           # print("{%0.2f}" %precision[d],d,"{%0.2f}" %recall[d])
    
        area = auc(recall, precision)
        area_sv=auc(recall_SV,precision_SV)
        area_k= auc(recall_knn,precision_knn)
        print("Area Under Curve(Decision Tree): %0.2f" % area)
        print("Area Under Curve(SVM): %0.2f" % area_sv)
        print("Area Under Curve(Knn): %0.2f" % area_k)
        
        pl.clf()
        pl.plot(recall, precision, label="Decision Tree")
        pl.plot(recall_SV,precision_SV, label="State Vector Machine")
        pl.plot(recall_knn,precision_knn, label="Knn")
        pl.xlabel("Recall")
        pl.ylabel("Precision")
        pl.ylim([0.0, 1.05])
        pl.xlim([0.0, 1.0])
        pl.title("Precision-Recall example: AUC=%0.2f" % ((area+area_sv+area_k)/3))
        pl.legend(loc="lower left")
        pl.show()

 





#output tutte le previsioni dei classificatori sul test-set e confronto con valori reali
def mostra_predizioni(x,pred,pred_SVC,y_test,X_test):
    for d in range(x):
       
        classe=category_name(pred[d])
        classe1=category_name(pred_SVC[d])
        classe2=category_name(y_test[d])
            
        print(X_test[d],"Alb:",classe," -SVC:",classe1,"-Classe:",classe2,"\n")
       