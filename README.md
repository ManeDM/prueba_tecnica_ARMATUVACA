<h1>Card payment simulation</h1>

<p>This is a simple backend server built in Django 5.0 & Using Django Restframework that allow users to simulate card payment process. This project contains one main model, <strong>PaymentInfo</strong></p>

<h2>PaymentInfo Model</h2>

<p>The <strong>PaymentInfo</strong> model represents a object which contains the following fields</p>

<ul>
 <li><strong>Name</strong>Payer username</li>
 <li><strong>Surname</strong>Payer Lastname</li>
 <li><strong>Card_number</strong>Card number</li>
 <li><strong>Card_cvv</strong>Security code number</li>
 <li><strong>TotalValue</strong>Amount to be paid</li>
 <li><strong>Extra_description</strong>additional payment information</li>
 <li><strong>comission_value</strong>commission to be paid</li>
</ul>

<h2>Usage</h2>

<p>To run this server, you must have Django installed on your computer. Next, you need to clone this repository and then navigate to the project directory and run the following command lines</p>

<textarea readonly onclick="this.select()" rows="2" cols="1">pip install -r requirements.txt
python manage.py runserver</textarea>

<p>This will install all the necessary dependencies and start the Django development server. You can then access the application by navigating to http://127.0.0.1:8000/api/payment-tc/process/ in your web browser.</p>

<p>Finally, in the test environment for HTTP requests of Django Restframework, you can pass a JSON object that looks like the following example</p>

<textarea>
{
    "name": "ALberto",
    "surname": "Ramirez",
    "card_number": 7845235689651254,
    "card_cvv": 123,
    "total_value": 60000,
    "extra_description": "Información adicional opcional"
}
</textarea>


