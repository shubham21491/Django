**Installation**
  Prerequisites
    1.Install Python:
      Install python-3.7.2 and python-pip.
      Follow the steps from the below reference document based on your Operating System.
      Reference: https://docs.python-guide.org/starting/installation/
    
    2.Set Up Virtual Environment:
      # creating virtual environment:
      python -m venv <name of the environment>
      eg: pyhton -m venv <.venv>
    
      # activation of virtual environment:
      for windows:
        <name of the environment>\Scripts\activate
        eg: .venv\Scripts\activate
        if this command not working or giving an error then:
          check or give the authorization:
            windows key -> Power shell -> Run as Administrator 
            shell opens:
              Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
              
    3.Install Django:
      #install django on environment
      #there are many more methods but i had used this
      py -m pip install Django
      
**Starting Of Project**
  starting your project:
    django-admin startproject <name of the project>
    eg: django-admin startproject myfirstdjango
  running server:
    first get inside to the project which you had made
    cd <name of the project>
    eg: cd myfirstdjango
    then:
    python manage.py runserver
    

  
  
      

              

      


