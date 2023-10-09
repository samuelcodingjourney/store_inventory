Assignment 2:
1. Firstly create a github account and then to initialize a new repository with the command git init. Next, to configure the username and email that will be associated with the commits. In order to verify you I needed to write a command of git config --list --local to see the informations. The next step that I had to do was to create a new repository on github that I opened in my browser. I would need to add a README.md file in my local project directory as well. Doing this would allow me to then run git status and then git commit -m "<My comment>" to create a commit with a comment message by firstly checking if there is a file that could be commited due to some changes or new files being created in my local repository. Then, I need to connect my local repository with the remote repository on github by using command prompt to run git branch -M main and git remote add origin <HTTPS URL of the repository in github> to connect. Last command in this case is to push to github by running the command git push -u origin main to push all the changes made in the current branch in the local repository to the main branch in the github repository in this case. The next thing that I have to do is to create a virtual environment using command python -m venv env. Activatin git in windows requires env\Scripts\activate.bat. In the same directory I have to create a requirements.txt file and add some dependencies on it so that later on i can use pip install on the requirements.txt file to install the dependencies. Create a django project by using the command django-admin startproject <Project Name> . command. Next I needed to add * to ALLOWED_HOSTS in settings.py to allow access to any host and accessible widely. To run the Django server use the command python manage.py runserver. To stop the server I could just press Ctrl+C in Windows and deactivate command to deactivate the virtual environment. Lastly, to create .gitignore file to specify files and directories that Git should ignore and then perform add, commit, and push from the local repository. Then I could deploy to Adaptable.io but first I must have an account there. When I was building the Django project I used the MTV concept. I needed to create a new application called main in the directory and then register main to INSTALLED_APPS in settings.py file to register the application main. I will also need to create a main.html template inside a templates direcotry within main application. Then I need to modify the models.py file in the main application. To apply model migrations or when there are changes in the model I must do migrations. To connect the views to templates I need to open the views.py file located in the main appllication and implement a show_main function. To configure url routing, I just need to create a urls.py file inside main directory and fill it with the corresponding urls and what it will show for example the show_main method created before. To add URL routing of the project to the main view, just open the urls.py file inside the project's directory and add URL pattern to direct it to main within the urlpatterns. Some unit testing can be done by opening and fillling the tests.py file in the main application directory. To run the tests use the command python manage.py test. 
2. 
![Screenshot (520)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/9587f708-c86f-4cdd-913b-7c1d40e8ec61)

3. Virtual environment is used by Django to execute an application. Python provides tool to do this which is virtualenv to create that Python environment that is isolated. Also because there is a need to produce multiple projects of Django on one system requiring different versions of Python and third-party Python packages/dependencies such that it is necessary to have virtual environment in order to create a Django web app. A virtual environment itself is a tool that helps to make dependencies isolated or seperate from each other when required by different projects. 
4. The Model-View-Controller(MVC) Pattern is a pattern that suggests splitting the code into 3 components or layers. Those are model where this stores the data of the application, view where the user inferface or the one that holds the components visible on the screen lies, and lastly controller where this component establishes the connection between View and Model by containing the core application logic. The Model-View-Presenter(MVP) Pattern on the other hand provides an easier way to structure the project codes. It is also compromised of three layers which are model, view, and presenter. This pattern has been proven to be providing modularity, testability, and a more clean and maintainable codebase. The Model-View-ViewModel suggest the seperation of data presentation logic with the core business logic part of the application while also having three layers of model, view, and viewmodel. The main difference between them is that the role of a mediator component. MVC and MVP both have a controller that acts as mediator between the model and the view while on the other hand, MVVM involves a viewmodel that serves as the mediator between the model and the view. So all in all MVC is the simplest of these patterns and the more flexible ones are MVP and MVVM.

Assignment 3:
1. The difference between POST form and GET form in Django is that the POST form is when the login form is returned and the browser would bundle the form data and encode it for transmission. However, GET is when it Django bundles the submitted data into a string to compose a url.
2. In XML, just by reading the document, the people reading could understand the information that is conveyed. The information itself is wrapped within tags and must contain a root element. JSON on the other hand, is derived from JavaScript Objects and the data is stored using key and value pairs. Lastly, HTML is a markup language that is used for creating structures of web pages. Can be using text, graphs like paragraphs, or even list of points. It also uses tags for creating the elements.
3. JSON has many advantages over other schemas like XML, where JSON is very easy to understand because it is based on key-value pairs. Softwares can easily parse and generate it too and also it is often used for network structured data exchange like between an application and a server.
4. To implement this week checklist, the first thing that I did was to understand what is HTML, XML, and JSON. Next, I needed to prepare a base template that will be seen once user access each url on the respective schema. But, I have to create the form and to show the product data after whcih I could do using classes and some variables to store or accepts new item data. Now, I need to know how to return the data as XML or JSON. I just need to import some classes from django in the views.py file and also create some methods that will accepts request as a parameter and return previously fetched data in the format of each respective schema. I could also retrieve based on ID given by anyone who enters it into the url as long as there is a variable inside the function to store the query result and specific ID of it from the model. XML and JSON can be differentiated here when setting the type of content parameter inside the functions in views.py. Lastly, do not forget to add the urlpatterns that could trigger each method just created. 

Postman Screenshots Results:
![Screenshot (536)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/91238da2-e5d4-422d-9721-559714e4db79)

![Screenshot (537)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/f0687619-22be-415b-b9e2-b914afdb869f)

![Screenshot (538)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/ff5ca7d6-bbfa-418d-94e5-0d6d795be6b3)

![Screenshot (539)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/fd789576-009c-4069-b948-2c051cbf0bdc)

![Screenshot (540)](https://github.com/samuelcodingjourney/store_inventory/assets/94734973/55fa80a5-ddc2-4732-ac59-98c6a6784077)

Assignment 4:
1. What is UserCreationForm in Django? Explain its advantages and disadvantages.
The UserCreationForm is one of the inbuilt feature of the Django ModelForm class to create new user form. We can edit the from created using UserCreationForm to include necessary fields. This can be use by importing from django.contrib.auth.forms.
2. What is the difference between authentication and authorization in Django application? Why are both important?
In Django, authentications means to verify if a user is who they say they are while authorization means to set up the things that the person who was authenticated could do. Since Django provides the system to apply both, they are very important to verify user credentials and also define the features or actions they could do or perform.
3. What are cookies in website? How does Django use cookies to manage user session data?
When users are visiting website, the cookies are able to identify them by first being generated by the web server to send to the web browser in order to remember the information about the visit. When a user already logged in to a website, the session ID will be stored in the browser as a cookie and the browser will attach it to the HTTP request, therefore every time there is an incoming request it can read the session ID in the request cookie. Django uses cookies to manage user session data by doing this, although you would need to add a cookie() method to set cookies that the server sends to user browser and then the browser will save the data. 
4. Are cookies secure to use? Is there potential risk to be aware of?
Cookies could still produce security risks such as people impersonating the user, collecting valuable and hidden data, or even fully steal their accounts. Therefore, it is always best to just store the session ID in the client-side and then the data of the session on the server-side in order to prevent attacks that could not benefit the user by using cookies.
5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).
The first checklist is implementing the registration. This was done by first creating the form itself using Django UserCreationForm. Login and logout functions could also be implemented by creating their functions or methods in the views.py and also setting up their urls also their HTML templates. Next to use data from cookies by displaying last login by adding a new key and value pair in the context of the show_main function to display last login and modifying the logout method so that when user logout, the cookie would get deleted. 
After that, I could create the two user accounts and three dummy data entries per account using the model. Connecting the Product model with user could be done by make the migrations to set user ID to 1 and apply migrations because the models.py file was modified earlier to add the user information. The reason for this is that we would want the products created by certain user being owned only to those users.
Assignment 5:
1. There are three types of CSS selectors which are element selector, ID selector, and class selector. Element selector is used when we want to apply the same styles to all elements with that HTML tag. With only a format of tag_name, the element can act as a selector in a CSS file. The second one which is ID selector uses ID as its selector. ID itself is unique for every web page. It can be associated with the tags like div and to use it as a selector the format is just #id_name, therefore the # here is always used to differentiate ID selector from other selector. Lastly, the class selector. This selector allows grouping elements of similar characteristics. For example, multiple div tags with no hierarchy between them could just simply use the same class without any problem, making it easier when applying CSS to it because in order to use this selector one could just use format of .class_name. This time, it must always be preceded by . in order to differentiate this selector with the others. 
2. Some of the HTML5 tags that I know are article tag which is used for specifying independent content and commonly used in a newspaper article website, the body tag which is famous as it is the tag that specifies the whole body of the website itself, button tag to specify a button that could be pushed, div tag which is used for sections in a web page, and one more example is footer tag which is a section to contain information about the author, copyright information, contact number, or any other sources. 
3. Differences between margin and padding is that margin means the space around the border and padding is the space around the content. Padding is inside the border and contains the content itself, while on the other hand margin exist outside of the border.
4. Tailwind is a CSS framework that uses pre-defined utility classes and combining them in order to build the layout. The file size itself is also smaller compared to Bootstrap which is another CSS framework because it only loads those pre-defined utility classes. Therefore, Tailwind is a good choice when developers want high flexibility and adaptability when creating or developing projects. Although, learning how to combine those utility classes to the needs of the project could take quite a while. On the other hand, Bootstrap is famous for providing predefined styles or components that can be used directly. However, this causes a large CSS file and the design can be quite boring because it often produces consistent designs. Developers can easily learn and even master Bootstrap even as beginners, amateurs, or even experts level.
5. In order for me to implement the checklist step-by-step, first I needed to add one of the CSS framework which is in this case is Bootstrap. Also by adding a meta tag with name=viewport in templates/base.html this helps on the web page to adapt to size or behavior of mobile devices. I also create a script tag on one line in order to enable Javascript to be used in the future. 

Then, I created the Navbar. The navbar contains my name as well as the logout option. As seen in first and second picture below.
Then, I added the edit function to the application by creating edit_product method to edit the products and then creating its own HTML file in main/templates subdirectory. After that, importing the function to urls.py and add the path to the urlpatterns list. The same goes to the delete function for my application. The pictures can be seen below. 
Lastly, I modified the main page, login, register, edit product, and add new product page.

Assignment 6:
1. The difference between asynchronous programming and synchronous programming is that asynchronous programming deals with independent tasks. Cases of using this programming such as developing responsive UI. The reason for this is because when for example loading the font size we would have to wait for it to load the history and then do the update. Due to asynchronous working in multi-thread or operations can run in parallel, non-blocking which means it can send multiple requests to a server, and for that reason increases the throughput because multiple operations run at the same time. On the other hand, synchronous programming is single-thread meaning thaat only one of the operation can run at a time, there is blocking meaning that the request being send at the server is one at the time and have to wait for the request to be answered or a response is send by the server. Basically, asynchronous allows for tasks to run simultaneously and synchronous means that each task have to be completed first before wanting to execute the other operations. For each operation, a waiting time for the response from the server is also required.
2. Event-driven programming paradigm is about program execution surrounded by upcoming events and the actions that can be taken in response to those input events, usually a callback function would be triggered when a main loop in the program detected one of such events. An example in this assignment is when we are clicking the login button in the login page. This is an event of mouse clicking and then a callback function will be triggered which is the login_user method. This will check the authencity of the user trying to log in.
3. Implementation of asynchronous programming in AJAX can be exxplained in some steps. Firstly, when an event occurs for example a button was pressed, an XMLHttpRequest object is created by JavaScript. Next, the XMLHttpRequest object will send a request to the server. After server had finished processing the request, the server will return a response to the web page. Javascript will then read the response and subsequent actions will be triggered based on how pre-defined steps on how to handle things on the task.
4. Since in this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Specific for this assignment, AJAX was used in the web browser by using the fetch() function provided by JavaScript. This Fetch API method is more powerful and flexible replacement for XMLHttpRequest since being introduced in ECMAScript 2020. Generally, it simplifies AJAX requests. Using AJAX methods with JQuery could give the programmers more lines of code to implement which in turn could create unnecessary file load  and some delays on the loading time causing less speed in turn. Fetch on the other hand is flexible on a lot of browsers. Using Fetch() method developers do not need to use any additional object to interact with server instea, it just request to the server thorugh the method in order to load the information. 
5. In order to implement the steps above, firstly, I had to create a method of get_product_json that takes in the request object. Then, another method of add_product_ajax to accept the request object also and add the new product to the database using AJAX. By doing this, I needed to import csrf_exempt from django.views.decorators.csrf. Also, adding the decorator @csrf_exempt. After this, I also needed to import the methods get_Product_json and add_product_ajax in the urls.py file also adding the URL paths of those method to the urlpatterns list. Then I also have to delete the previous table code and replace it with a new table tag with id of product_table. After this is where the script part of Javascript needs to be added at the bottom of the html file in the main.html file. In this script tag I needed to create a nethiod of getProducts which uses the fetch() API to get JSON data and also parsed to a JavaScript object. Another function is refreshProducts() to refresh the product data asynchronously. After the method is defined, I also needed to call the refreshProducts method also to refresh the table everytime we open the web page. Now I was introduced to something called a form modal in Bootstrap for my application. I needed to apply the template and to show the modal form, a button is needed which is also the button to create new products using AJAX. In order to add new product using form data, a addProduct method must be created where the data from form modal would be wrapped using the FormData object before sending it to the server. This method would be a callback function when the button of add product is being pressed.