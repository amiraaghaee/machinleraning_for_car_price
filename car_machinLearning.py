import mysql.connector
from sklearn import tree
from sklearn import preprocessing


cnx = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='cardata')
                              
cursor = cnx.cursor()
query = 'SELECT * FROM dataf;'
cursor.execute(query)

x = []
y = []

data = list(cursor)
for i in range(len(data)):
    x.append(data[i][0:5])
    y.append(data[i][5])






le = preprocessing.LabelEncoder()

le = lex.fit(x)

le = lex.classes_

le = ley.transform(x)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(le, y)


# new_data = [['name', 'model', 'productYear', 'traveled', 'city', 'price']]

# answer = clf.predict(new_data)
