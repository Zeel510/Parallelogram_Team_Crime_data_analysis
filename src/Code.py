import matplotlib.pyplot as plt
import pandas as pd

Crimedata = pd.read_csv(r""File path"")
print(Crimedata)

Deployed = Crimedata['Close_Open']
plt.pie(Deployed,startangle=140) 

plt.title('Crime Data')

plt.show()

plt.scatter(Crimedata['City'], Crimedata["Victim Gender"], color='blue', marker="^")

plt.xlabel('Date')
plt.ylabel('Crime')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')

plt.title('Crime Data')

plt.show()

plt.scatter(Crimedata['Victim Age'], Crimedata["City"], color='red', marker="x")

plt.xlabel('Date')
plt.ylabel('Crime')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')

plt.title('Crime Data')

plt.show()
