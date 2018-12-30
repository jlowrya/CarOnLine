<html>
<body>
<form action="/customers/{{cust.cust_id}}/edit" method="POST">
  Name: <input type="text" name="name" value="{{ cust.name }}"/><br>
  Surname: <input type = "text" name="surname" value="{{cust.surname}}"><br>
  Phone: <input type="text" name="phone" value="{{cust.phone}}"><br>
  <input type="submit" value="Save">
</form>

<a href="/customers">Back</a>
</body>
</html>
