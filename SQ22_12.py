#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 30-06-2022
#	TITLE : SQ22-12 - (30-06-2022)
#   SUBTITLE : InfoVis Design
#	REDACTED FOR : ADV COURSE ON COMPUTER VISUALIZATION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
import networkx as nx
from matplotlib.pyplot import *
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

researchers = ["A","B","C","D"]
collab = [("A","B"),("A","C"),("A","D"),("B","A"),("B","D"),("C","A"),("C","B"),("D","A"),("D","C")]
acm = [80,20,60,50]
tvcg = [30,0,5,8]
ieee = [100,10,20,100]
rev = [500,20,200,300]
mails = [300,15,150,120]

net = nx.DiGraph()
net.add_nodes_from(researchers)
net.add_edges_from(collab)


colors = ['blue','orange','green','red']

fig, ax = subplots(2,3)
fig.suptitle('Statistics on Researchers',fontsize='xx-large',fontweight='bold')
nx.draw_networkx(net,ax=ax[0,0],node_color=colors,font_color='white')
ax[0,0].set_title('Collaboration Network')
ax[0,1].bar(researchers,acm,color=colors)
ax[0,1].set_title('ACM publications')
ax[0,2].bar(researchers,tvcg,color=colors)
ax[0,2].set_title('TVCG publications')
ax[1,0].bar(researchers,ieee,color=colors)
ax[1,0].set_title('IEEE publications')
ax[1,1].bar(researchers,rev,color=colors)
ax[1,1].set_title('Paper reviews')
ax[1,2].bar(researchers,mails,color=colors)
ax[1,2].set_title('E-mails per day')

show()

print('END TESTS')
#####################################################################################################################################