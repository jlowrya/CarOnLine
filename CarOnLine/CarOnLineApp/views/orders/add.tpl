<html>
<body>
<form action="/orders/add" method="POST">
Customer:
<select name="cust">
%for c in custs:
<option value="{{c.cust_id}}">{{c.cust_id}} {{c.surname}}, {{c.name}}</option>
%end
</select> or <a href="customers/add">New customer</a><br>
Car(s):
<table>
%count = 0
<tr>
%for c in cars:
%if count/10==1:
</tr>
<td><input type="checkbox" name="car" value="{{c.car_id}}">{{c.brand.name}} {{c.model}}</input></td>
<tr>
%else:
<td><input type="checkbox" name="car" value="{{c.car_id}}">{{c.brand.name}} {{c.model}}</input></td>
%end
%count+=1
%end
</tr>
</table><br>


<input type="submit" value="Save">
</form>
</body>
</html>