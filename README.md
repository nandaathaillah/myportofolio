Name    : Nanda Athaillah Nurano

NPM     : 2506557425

Class   : PBP KKi


1. Explain what happens when a user opens the new portfolio page, starting from the request received by the project until the data appears in the browser. In your answer, explain the roles of the project’s 
urls.py, the application’s urls.py, the view, the model, and the template.
Answer
The user's browser asks the server for a specific URL (like /awards/). The project's urls.py forwards the request to the app's urls.py, which matches the URL path and triggers the correct View. The View asks the Model for data. The Model grabs this data from the database and hands it back to the View. The View passes that data into the Template (A.K.A the HTML file). The template plugs the data into its layout, and the finished HTML is sent back to the user's browser.


2. Why should the data for the new portfolio section be stored in a model instead of being written directly in the template? Explain how this choice affects application maintenance and future development.

Storing data in a Model separates your actual content from your website's design.

Maintenance: You can safely add, edit, or delete data through the database without ever touching or risking breaking your HTML code.

Future Development: It makes your app scalable. If you add 100 new awards, a template loop handles them automatically. It also allows you to easily sort, filter, or search your data using Python later.


3. What is the difference between makemigrations and migrate in Django? Give an example of a model change that requires you to run both commands.
answer: Makemigrations makes and prepares the files for migrations(Makes some sort of blueprint), while migrate migrates the files(Executes the blueprint). For example is if you add a new school_name field to your Experience model, you must run makemigrations to write the instruction to "add a new column," and then run migrate to actually create that column in your database.
