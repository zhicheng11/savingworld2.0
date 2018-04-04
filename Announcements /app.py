<!DOCTYPE html>
	<html>
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<link href = "css for main" type = "text/css" rel = "stylesheet">
			<link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
			<title>didUforGET?</title>
		</head>

		<body>
		    <div class="checklist">
		        <form action="/app" method="POST" id="form1">
			        {% for key, num in items.items() %}
			            {% if num == key  %}
    			            <div style="text-align: left" class="items">
                                <button type="submit" name= "action" value= {{ key }} class="button">x</button><input type="checkbox" name={{ num }} checked><del>{{ key }}</del>
                            </div>
                        {% else %}
                            <div style="text-align: left" class="items">
                                <button type="submit" name= "action" value= {{ key }} class="button">x</button><input type="checkbox" name={{ num }}>{{ key }}
                            </div>
                        {% endif %}
			        {% endfor %}
			</div>
            <div class="sticky">
			    	<input type="text" name="item" placeholder="Enter item" autocomplete="off"><br>
			    	<input type="submit" name="action" value="Enter" >
		    	</form>
			</div>
		</body>
	</html>
