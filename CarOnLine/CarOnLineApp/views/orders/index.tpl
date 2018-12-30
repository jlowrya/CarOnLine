<html>
<head>
<style>
table,th,td{
	border: 1px solid black;
}
</style>
</head>
<body>
<h1>List of Orders</h1>
<a href="/">Home</a>
<a href="orders/add">New Order</a>
<a href="/">Back</a><br>
<form action="orders/search", method='POST'><input type='text' name='key' value=''><input type='submit' value='Search'></form>
%if len(orders) == 0:
<p>No orders to show</p>
%else:
<table>
<tr>
<th>Order Number</th><th>Date Purchased</th><th>Customer name</th><th>Order total</th>
</tr>
%for o in orders:
    <tr>
	<td><a href="/orders/{{o.order_num}}/">{{o.order_num}}</a>
	<td>{{o.pdate}}</td>
	<td>{{o.cust.surname}}, {{o.cust.name}}</td>
	<td>£{{o.total}}</td>
	<td><form action="orders/{{o.order_num}}/delete", method="POST"><input type="submit" value="Delete"></form></td>
	<td><form action="orders/{{o.order_num}}/edit"><input type="submit" value="Edit"></form></td>
	</tr>
%end
</table>
</body>
</html>