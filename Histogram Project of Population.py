import matplotlib.pyplot as plt
import numpy as np

w=0.25
x=list(np.arange(1,6))
male=[58.243056,46.809027,104.480510,37.612306,54.278157]
female=[54.243056,44.467088,95.331831,35.014503,49.821295]
# plt.ylim(0,100000000)

bar2=[i+w for i in x]

plt.xlabel('STATE',labelpad=14,fontdict={'size':15,'color':'green'})
plt.ylabel('POPULATION (Millions)',labelpad=10,fontdict={'size':15,'color':'green'})

plt.bar(x,male,-w,align='edge',label='Male')
plt.bar(bar2,female,-w,align='edge',label='Female')

plt.text(0.77,60,'58.2M')
plt.text(1.03,55.7,'54.2M')

plt.text(1.77,48,'46.8M')
plt.text(2.03,46,'44.4M')

plt.text(2.77,106,'104.4M')
plt.text(3.03,97,'95.3M')

plt.text(3.77,39,'37.6M')
plt.text(4.03,37,'35M')

plt.text(4.77,56,'54.3M')
plt.text(5.03,51,'49.8M')

# plot the literacy graph
l3,=plt.plot([0.86,1.86,2.86,3.86,4.86] ,[51.47,42.44,82.74,29.33,36.75],"ro--" ,markeredgecolor='black',label='Literacy Male')
l4,=plt.plot([1.1,2.1,3.1,4.1,5.1],[41.15,42.92,56.53,20.73,26.68],'bo--',markeredgecolor='black',label='Literacy Female')

plt.xticks(x,['Maharashtra','West Bengal','Uttar Pradesh','Madhya Pradesh','Bihar'])
plt.legend(ncol=2,shadow=True,columnspacing=2,facecolor='aqua')

plt.title('CENSUS 2011',pad=14,color='green',fontsize=14)
plt.show()

