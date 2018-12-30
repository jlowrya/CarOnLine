<h1>Car: {{ car.brand.name }} {{car.model}}</h1>
Brand: {{car.brand.name}}</br>
Model: {{car.model}}</br>
Price: £{{car.price}}</br>
Units available: {{car.available}}</br>

<a href="/">Home</a>
<a href="/cars">Back</a>
<a href="/cars/{{car.car_id}}/edit">Edit</a>
