<html>
<head>
<style>
table,th,td{
	border: 1px solid black;
}
</style>
</head>
<body>
<h1>List of Cars</h1>
<a href="/">Home</a>
<a href="/cars/add">Add new car</a>
<a href="/">Back</a><br>
Search for car:<form action="/cars/search" method="POST"><input type="text" name="key" value=""><input type="submit" value="Search"></form></br>
%if len(cars)!= 0:
<table>
<tr><th>Brand</th><th>Model</th></tr>
%for c in cars:
    <tr>
	<td><a href="/brands/{{ c.brand.brand_id}}/"> {{ c.brand.name }}</a></td>
	<td><a href="/cars/{{ c.car_id}}/"> {{ c.model}}</a></td>
	<td><form action="/cars/{{c.car_id}}/delete" method="POST"><input type="submit" value="Delete"></form></td>
	<td><form action="/cars/{{c.car_id}}/edit"><input type="submit" value="Edit"></form></td>
	</tr>
%end
</table>
%else:
No cars to show.
%end
</body>
</html>

