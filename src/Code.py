import matplotlib.pyplot as plt
import pandas as pd

Trafficdata = pd.read_csv(r""File path"")
print(Trafficdata)

Deployed = Trafficdata['Close_Open']
plt.pie(Deployed,startangle=140) 

plt.title('Crime Data')

plt.show()

plt.scatter(Trafficdata['City'], Trafficdata["Victim Gender"], color='blue', marker="^")

plt.xlabel('Date')
plt.ylabel('Crime')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')

plt.title('Crime Data')

plt.show()

plt.scatter(Trafficdata['Victim Age'], Trafficdata["City"], color='red', marker="x")

plt.xlabel('Date')
plt.ylabel('Crime')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')

plt.title('Crime Data')

plt.show()
