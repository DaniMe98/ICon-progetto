# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:19:34 2020

@author: Danilo
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dc
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import utils as u
from sklearn.neighbors import KNeighborsClassifier





dataset= load_iris() #carico il dataset
dataset1=pd.read_csv(r'C:\Users\Danilo\Downloads\Ing.Conoscenza\prove\iris.csv')

X= dataset['data']   #divido i dati in due categorie: i dati morfologici
y= dataset['target']        #e l'ultima colonna contiene la classe di appartenenza del fiore

C = 10

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)    #*train porzione di dati su cui fare training

Alb_dec=dc()
StateVector=SVC(gamma=2, kernel='linear', C=C)
knn= KNeighborsClassifier(3)

StateVector.fit(X_train,y_train)      #☻addestramento dei classificatori sul training-set
Alb_dec.fit(X_train,y_train)
knn.fit(X_train,y_train)

#creazione curva precision-recall

pred_tra=Alb_dec.predict(X_train)      #calcolo delle predizioni per il test-set
pred=Alb_dec.predict(X_test)
pred_SVC=StateVector.predict(X_test)
pred_knn=knn.predict(X_test)

u.pr_curve(pred,y_test,pred_SVC,pred_knn)#curva precision recall

#u.mostra_predizioni(pred.size,pred,pred_SVC,y_test,X_test) 

 
print("Accuratezza delle predizioni sul test-set (Albero decisione) %0.1f%% "%(accuracy_score(pred,y_test)*100))  
print("Accuratezza delle predizioni sul test-set (SVC) %0.1f%% " %(accuracy_score(pred_SVC,y_test)*100))  
print("Accuratezza delle predizioni sul test-set (knn) %0.1f%% " %(accuracy_score(pred_knn,y_test)*100)) 


"""suggestion per nuovo fiore da cercare 4.9,3.1,1.5,0.1 Iris-setosa
                                         5.6,2.8,4.9,2.0 Iris-virginica
                                         6.3,2.3,4.4,1.3 Iris-versicolor"""
nuovo_fiore=[[4.9,3.1,1.5,0.1]]

nuovo_test_a =Alb_dec.predict(nuovo_fiore)
nuovo_test_b=StateVector.predict(nuovo_fiore)
nuovo_test_c=knn.predict(nuovo_fiore)

categoria= u.category_name(nuovo_test_a)
categoria2= u.category_name(nuovo_test_b)
categoria3= u.category_name(nuovo_test_c)
 

print(f'Categoria nuovo Fiore -->  Albero decisione:{categoria}\n\t\t\t   SVC:{categoria2}\n\t\t\t   Knn:{categoria3}')

