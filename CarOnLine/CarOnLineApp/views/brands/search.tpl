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
<a href="/brands/add">Add new brand</a><br/>
Search for car:<form action="/brands/search" method="POST"><input type="text" name="key" value=""><input type="submit" value="Search"></form></br>
%if len(brands)!=0:
<table>
<tr><th>Name</th><th>Country of origin</th></tr>
%for b in brands:
    <tr>
	<td><a href="/brands/{{ b.name}}/"> {{ b.name }}</a></td>
	<td>{{b.nation}}</td>
	<td><form action="/brands/{{b.brand_id}}/delete" method="POST"><input type="submit" value="Delete"></form></td>
	<td><form action="/brands/{{b.brand_id}}/edit"><input type="submit" value="Edit"></form></td>
	</tr>
%end
</table>
%else:
No brands match your search criteria.
%end
</body>
</html>