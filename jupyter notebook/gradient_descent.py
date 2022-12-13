import numpy as np
def gradient_descent(x,y):
    #step 1 assume initail value of m_curr and c_curr
    m_curr=c_curr=0
    n=len(x)
    learning_rate=0.001
    #then take baby steps untill you reach global minimum
    #HENCE DEFINE THE NUMBER OF ITERATION/LOOP/BABY STEPS
    iterations=1000
    for i in range(iterations):
        #step 2
        #calculate the equation using y=mx+c
        y_predicted=m_curr*x+c_curr
        cost=(1/n)*sum([val**2 for val in(y-y_predicted)])
        #Step 3 :Find the derivative for m and c
        #use formula 
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        c_curr=c_curr-learning_rate*bd
        print("m:{},b:{},cost:{},iteration:{}".format(m_curr,c_curr,cost,i))

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y)