<html>
<head>
<style>
table,th,td{
	border: 1px solid black;
}
</style>
</head>
<body>
<h1>Search Results</h1>
<a href="/">Home</a>
<a href="/orders/add">Add new Order</a>
<a href="/orders">Back</a><br>
Search orders:<form action="/orders/search" method="POST"><input type="text" name="key" value=""><input type="submit" value="Search"></form></br>
%if len(orders)!=0:
<table>
<th>Order Number</th><th>Date Purchased</th><th>Customer name</th><th>Order total</th>
%for o in orders:
    <tr>
	<td><a href="/orders/{{o.order_num}}/">{{o.order_num}}</a></td>
	<td>{{o.pdate}}</td>
	<td>{{o.cust.surname}}, {{o.cust.name}}</td>
	<td>£{{o.total}}</td>
	<td><form action="orders/{{o.order_num}}/delete", method="POST"><input type="submit" value="Delete"></form></td>
	<td><form action="orders/{{o.order_num}}/edit"><input type="submit" value="Edit"></form></td>
	</tr>
%end
</table>
%else:
No orders matched your search criteria.
%end
</body>
</html>