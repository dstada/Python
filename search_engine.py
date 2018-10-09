"""Simple Search Engine

Imagine you have a database which stores a large amount of user data.
The user data stored in the database may have the following fields:
- name (string, for example, "John Smith")
- profession (string, for example, "Software Engineer")
- age (number, for example, 31)

You can add new fields or modify the existing if you would like.

The data can be structured or unstructured. The manner in which the data is organized is up to you.


Create a search engine which will search the entire database and return the information related to the search query.

Example of data:
1: {name: "Alice", profession: "UI/UX Designer", age: "27"}
2: {name: "John", profession: "QA Engineer", age: "33"}
3: {name: "Stuart", profession: "Constructor", age: "19"}
4: …

If the user searches for "Alice" or "designer", the result should be this:


name: "Alice", profession: "UI/UX designer", age: "27"


If the user does not type anything in the search input field, then all the entries in the database
should be printed to the screen. Use any data for your tests. You can use a random data generator.
"""

# dbase data generated with mockaroo.com:

dbase = [{"id":1,"first_name":"Alis","last_name":"Pidwell","email":"apidwell0@blinklist.com","gender":"Female","ip_address":"53.251.180.248"},
{"id":2,"first_name":"Chere","last_name":"Coppenhall","email":"ccoppenhall1@fastcompany.com","gender":"Female","ip_address":"252.42.82.23"},
{"id":3,"first_name":"Melita","last_name":"McWilliams","email":"mmcwilliams2@netlog.com","gender":"Female","ip_address":"123.87.178.129"},
{"id":4,"first_name":"Lisbeth","last_name":"Cockarill","email":"lcockarill3@unblog.fr","gender":"Female","ip_address":"146.104.39.27"},
{"id":5,"first_name":"Onida","last_name":"Bumphrey","email":"obumphrey4@theguardian.com","gender":"Female","ip_address":"56.38.153.19"},
{"id":6,"first_name":"Jasper","last_name":"Westberg","email":"jwestberg5@tmall.com","gender":"Male","ip_address":"206.59.167.36"},
{"id":7,"first_name":"Alwyn","last_name":"Antonovic","email":"aantonovic6@livejournal.com","gender":"Male","ip_address":"231.237.53.47"},
{"id":8,"first_name":"Cull","last_name":"Saltrese","email":"csaltrese7@chicagotribune.com","gender":"Male","ip_address":"193.23.161.152"},
{"id":9,"first_name":"Darlene","last_name":"Center","email":"dcenter8@uol.com.br","gender":"Female","ip_address":"143.24.131.249"},
{"id":10,"first_name":"Oates","last_name":"Spradbery","email":"ospradbery9@people.com.cn","gender":"Male","ip_address":"205.167.127.132"}]

print(dbase[0])