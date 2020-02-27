## Objects Overview
- Form objects:
    - Provide an area which can contain widget objects. 
    - Additional functions: 
        - Handling menus; 
        - Routines will be run when user click "ok" button.
        - Operations between key-presses.
        - Operations when user navigate throught the Form.

- Widget object:
    - Text box, labels, sliders, etc.

- Application object:
    - These object provide a convenient way to manage the running of your application.
    - ```NPSAppManaged``` is almost the best way to manage your application, unless you have good reasons.
        - You don't need to write your own main loop, ```NPSAppManaged``` will manage the display of each Form of your application.
        - Set up yoru Forms and simply call ```UserClass(NPSAppManaged).run()```.
    

#### ```NPSAppManaged```
- Letting ```NPSAppManaged``` manage your forms
    - ```NPSAppManaged.addForm(id, FormClass, *args)```
        - Create a new Form (of FormClass), and register it with NPSAppManaged instance.
        - **id** should be a unique **str**.

    - ```NPSAppManaged.addFormClass(id, FormClass, ...)```
        - This version will register a class rather than an instance.
        - A new instance will be created everytime it's edited.

    - ```NPSAppManaged.registerForm(id, FormObject)```
    
    - All forms registered with an NPSAppManaged instance can access the controlling application object using ```self.parentApp```

    - To remove a form, you can do the ```UserClass.removeForm(id)``` method.

- Running an NPSApplicationManaged application

    - ```run()```
        - Start an NPSAppManaged application mainloop.

        - **Your Form Entrance should have id "MAIN".**

        - **This method will activate the default form, which should have the id "MAIN".**

    - ```NPSAppManaged.NEXT_ACTIVATE_FORM```

        - The next form to be displayed will be the one specified by the variable **NEXT_ACTIVATE_FORM**. Should use ```setNextForm(formid)``` to define the next displaying form.

        - all forms registered which do not have the ```activate()``` method will have the ```afterEditing()``` called; Logic to determine which form to display next should go into the ```afterEditing()``` method.

    - ```NPSAppManaged.STARTING_FROM```:
        - change the name of default form.

    - ```NPSAppManaged.setNextForm(formid)```
        - set the form to be displayed **when current one exits.**

    - ```NPSAppManaged.setNextFormPrevious()```:
        - Set the previous form as the one to be displayed **when the current one exits**.

    - ```NPSAppManaged.swithcForm(formid)```
        - Immediately switch to the form with formid.
        - Will skip all exit logic of the current form.

    - ```NPSAppManaged.switchFormPrevious()```
        - Immediately switch to the previous Form.

- Additional method (partial)
    - ```NPSAppManaged.onStart()```
        - will be called when the Manager starts running.

    - ```NPSAppManaged.onCleanExit()```
        - Override this method to perform any cleanup when applicatoin is exiting without error.

    - ```NPSAppManaged.getHistory()```
        - return a list of previous forms visted.

    - ```NPSAppManaged.resetHistory()```
        - forget the previous forms visited.
