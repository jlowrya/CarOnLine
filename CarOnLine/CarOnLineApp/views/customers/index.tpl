<html>
<head>
<style>
table,th,td{
	border: 1px solid black;
}
</style>
</head>
<body>
<h1>List of Customers</h1>
<a href="/">Home</a>
<a href="/customers/add">Add new customer</a>
<a href="/">Back</a><br>
Search for customer:<form action="/customers/search" method="POST"><input type="text" name="key" value=""><input type="submit" value="Search"></form></br>
%if len(custs)!=0:
<table>
<tr><th>Name</th><th>Phone number</th></tr>
%for c in custs:
    <tr>
	<td><a href="/customers/{{c.cust_id}}/">{{ c.surname }}, {{c.name}}</a></td>
	<td><a href="/customers/{{c.cust_id}}/">{{c.phone}}</a></td>
	<td><form action="/customers/{{c.cust_id}}/delete" method="POST"><input type="submit" value="Delete"></form></td>
	<td><form action="/customers/{{c.cust_id}}/edit"><input type="submit" value="Edit"></form></td>
	</tr>
%end
</table>
%else:
No customers to show.
%end
</body>
</html>