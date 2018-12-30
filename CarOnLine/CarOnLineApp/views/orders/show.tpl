<html>
<body>
<h1>Order number:{{order.order_num}}</h1>
<a href="/">Home</a>
<a href="/orders/{{order.order_num}}/edit">Edit order</a><br/>
Customer:{{order.cust.name}} {{order.cust.surname}}<br>
Purchase date: {{order.pdate}}<br>
Total:£{{order.total}}<br>
Cars bought:
<ul>
%for car in order.cars:
<li>{{car.brand.name}} {{car.model}}</li>
%end
</ul>
<a href="/orders">Back</a 
</body>
</html>