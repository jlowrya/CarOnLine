<html>
<body>
<form action="/cars/add" method="POST">
Brand:<select name="brand">
%for b in brands:
<option id="{{b.name}}">{{b.name}}</option>
%end
</select><br>
Model:<input type="text" name="model" value=""><br>
Price:<input type="text" name="price" value=""><br>
Availibility: <input type="text" name="available" value=""><br>
<input type="submit" value="Save">
</form>
</body>
</html>