Do the following steps.:

Copy the  docker-compose.yml file
First run the docker-compose.yml file as:   “Docker-compose up”
Then Stop the process by : “ctrl+c”
Run command only once in separate terminal - “docker run --name mysql -e MYSQL_ROOT_PASSWORD=pizzeria -d mysql”
Now finally run “Docker-compose up”
The port will be http://127.0.0.1:8000
Hit the end point - http://127.0.0.1:8000/placeorders to place order as per the syntax :
{
  "pizzas": [
   {
      "pizzabase": ["Thincrust"],
      "cheese": ["Mozerella"],
      "toppings": ["olive", "chicken", "pepperoni", "jalapeno", "mushroom"]
    },
{
      "pizzabase": ["Cheeze burst"],
      "cheese": ["Cheddar"],
      "toppings": ["Green pepper", "Fresh basil", "pepperoni", "Fresh garlic", "Tomato"]
    }
  ]
}

Hit the end point - http://127.0.0.1:8000/trackorders to get the status of the orders in the database: 
Refresh/Get after 1 minute, the status should change from ‘Accepted’ to ‘Preparing’
Refresh/Get after 3 minutes it should change from ‘Preparing’ to ‘Dispatched’
Refresh/Get after 5 minutes it should read ‘Delivered’

