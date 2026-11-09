Name    : Nanda Athaillah Nurano

NPM     : 2506557425

Class   : PBP KKi

## Assigment 5:
1. Explain why we use Django’s ModelForm instead of creating HTML forms manually. Additionally, explain why we are required to add {% csrf_token %} to these forms!
  Django ModelForm automatically generates HTML inputs and handles data validation directly from the database model, so I don't have to manually write and map the forms. The {% csrf_token %} is a mandatory security measure that prevents Cross-Site Request Forgery attacks by ensuring the form submission originated directly from your actual website, not a malicious third party.

2. In Tutorial 03, we discussed JSON and XML data formats. Why is JSON preferred in modern web application development compared to XML?
JSON is preferred over XML because it is much lighter and parses instantly into native JavaScript objects. It uses a simple key-value structure that perfectly matches modern programming languages, avoiding bulky, slow and hard to read opening and closing tags required by XML.

3. Explain the flow that occurs when you use a view function to return your portfolio data in JSON format. Why do we need to perform the serialization process on Django models before returning the data?
When a view requests data, Django returns a Python QuerySet. Because web browsers and internet protocols cannot read language-specific Python objects, we must perform serialization. This process converts the complex Python data into a universal, plain-text JSON string so it can be successfully transmitted via an HttpResponse and read by the client. 

## Assigment 6:
1. Explain what REST means and why returning JSON alone isn’t enough to call an API RESTful. Also explain the difference between PUT and PATCH, with an example of when each should be used. Answer: REST is an architecture based on stateless, client and server interactions using standard HTTP methods on resource-based URLs. Returning just JSON isn't enough, the specified URL and HTTP method conventions must also be followed.
    - PUT: Replaces an entire resource (cth: updating an award's title, description, and year all at once).
    - PATCH: Modifies it partially (cth: only updating the year, leaving the rest alone). 

2. Explain the role of a serializer in Django REST Framework. What are its advantages over manually assembling a dictionary with JsonResponse as in Tutorial 05?
A serializer converts complex Django models into JSON-ready Python types, and vice versa. It is much better than manual JsonResponse dictionaries because it automatically handles data validation (like rejecting invalid text), reduces boilerplate code, and easily generates read-only computed fields like the star count.

3. Explain the difference between authentication and authorization in Django REST Framework. Why must access rights be checked with a permission class on the server, rather than only by hiding a button in the template?
Authentication verifies who the user is (e.g., logging in).Authorization determines what they can do (e.g., Editors can edit, but cannot delete).
    - Access rights must be checked on the server because hiding a frontend button only stops honest users. 
    - A malicious user can easily bypass the HTML and send a direct DELETE request to the API using Developer Tools or Postman.   

4. Explain why requests that change data still need a CSRF token when an API uses SessionAuthentication. Why isn’t a test using force_authenticate enough to prove that CSRF protection works? Answer: SessionAuthentication uses browser cookies, which are automatically sent with every request—even if that request was secretly triggered by a malicious third-party site. A CSRF token acts as a password to prove the request actually came from your frontend. force_authenticate skips standard middleware, bypassing the CSRF check entirely, so it cannot prove your CSRF protection actually works in a real browser scenario.