Name    : Nanda Athaillah Nurano

NPM     : 2506557425

Class   : PBP KKi


1. Explain why we use Django’s ModelForm instead of creating HTML forms manually. Additionally, explain why we are required to add {% csrf_token %} to these forms!
  Django ModelForm automatically generates HTML inputs and handles data validation directly from the database model, so I don't have to manually write and map the forms. The {% csrf_token %} is a mandatory security measure that prevents Cross-Site Request Forgery attacks by ensuring the form submission originated directly from your actual website, not a malicious third party.

2. In Tutorial 03, we discussed JSON and XML data formats. Why is JSON preferred in modern web application development compared to XML?
JSON is preferred over XML because it is much lighter and parses instantly into native JavaScript objects. It uses a simple key-value structure that perfectly matches modern programming languages, avoiding bulky, slow and hard to read opening and closing tags required by XML.

3. Explain the flow that occurs when you use a view function to return your portfolio data in JSON format. Why do we need to perform the serialization process on Django models before returning the data?
When a view requests data, Django returns a Python QuerySet. Because web browsers and internet protocols cannot read language-specific Python objects, we must perform serialization. This process converts the complex Python data into a universal, plain-text JSON string so it can be successfully transmitted via an HttpResponse and read by the client. 
