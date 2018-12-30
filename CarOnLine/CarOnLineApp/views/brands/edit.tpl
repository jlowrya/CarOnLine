<form action="/brands/{{brand.brand_id}}/edit" method="POST">
  Name: <input type="text" name="name" value="{{ brand.name }}"/></br>
  Nationality: <input type="text" name="nation" value="{{brand.nation}}"/></br>
  <input type="submit" value="Save">
</form>
