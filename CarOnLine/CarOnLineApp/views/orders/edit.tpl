<html>
<body>
<form action="/orders/{{order.order_num}}/edit" method="POST">
Customer:
<select name="cust">
%for c in custs:
%if c.cust_id == order.cust.cust_id:
<option value="{{c.cust_id}}" selected>{{c.cust_id}} {{c.surname}}, {{c.name}}</option>
%else:
<option value="{{c.cust_id}}">{{c.cust_id}} {{c.surname}}, {{c.name}}</option>
%end
%end
</select><br>

Car(s):
<table>
%count = 0
<tr>
%for c in cars:
%checked = False
%for i in curr_car_ids:

%if c.car_id == i:

%if count/5==1:
</tr>
<td><input type="checkbox" name="car" value="{{c.car_id}}" checked>{{c.brand.name}} {{c.model}}</input></td>
<tr>
%else:
<td><input type="checkbox" name="car" value="{{c.car_id}}" checked>{{c.brand.name}} {{c.model}}</input></td>
%end
%checked = True
%break
%end

%end
%if not checked:
%if count/5==1:
</tr>
<td><input type="checkbox" name="car" value="{{c.car_id}}">{{c.brand.name}} {{c.model}}</input></td>
<tr>
%else:
<td><input type="checkbox" name="car" value="{{c.car_id}}">{{c.brand.name}} {{c.model}}</input></td>
%end
%end
%count+=1
%end
</tr>
</table><br>


<input type="submit" value="Save">
</form>
</body>
</html>