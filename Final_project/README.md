  # My final project Todoer.py
    #### Video Demo:  <https://youtu.be/mHQ5h7-AZI4>
    #### Description:
    1. The program is to help freelance writers to keep tasks in order. I'm going to add database to it, so it can keep all the info in memory forever. To fo this I used libraries re and datetime.
    2. The program walks user through all the questions and returns a string with all the information.
    There's a class Task in which all the information is stored and later will be used for further operations. It consists of two dunder methods __init__ with 5 parameters besides self, which are defined through functions called in main function. __repr__ returns an object in format of a string. In main function the instance is initialized and all its parameters are defined via further functions.
    Function get_number  asks user for the number of the tasks and checks that it follows the rules using regular expressions, if it doesn't it promts users to input correct format of the number (three digits and three letters)
    Function get_deadline asks user for the deadline of the task and accepts any form of input via datetime library and returns a nice format of day in numbers, month in words and year in numbers
    Function get_topic asks user for the topic in a string value.
    Function get_pages asks user for the number of pages and returns integer value
    Finally, function get_payment returns salary for the task multiplying number of pages by the global variable wage
    3. The information is stored in the object Task and can be easily accessed by users in future. I'm planning to add sorting functions as well.
    4. The test tests all the functions and returns mistakes
      - as long as there is need to test output according to input, I used Mock class of unittest and patch function of an object
    5. The project itself is in the file called "project.py" and the test for it is the file called "test_project.py"