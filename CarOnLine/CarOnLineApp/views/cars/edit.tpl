<html>
<body>

<form action="/cars/{{car.car_id}}/edit" method="POST">
Brand:<select name="brand">
%for b in brands:
%if b.name==car.brand.name:
<option id="{{b.name}}" selected>{{b.name}}</option>
%else:
<option id="{{b.name}}">{{b.name}}</option>
%end
%end
</select><br>
  Model: <input type="text" name="model" value="{{ car.model }}"/><br>
  Price: <input type = "text" name="price" value="{{car.price}}"><br>
  Availability: <input type="text" name="available" value="{{car.available}}"><br>
  <input type="submit" value="Save">
</form>

<a href="/cars">Back</a>
</body>
</html>
