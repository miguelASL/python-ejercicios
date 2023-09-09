```
### Usage

To use the application, open a terminal window and navigate to the directory where you cloned the repository. Then, run the following command:

```
python regla_de_tres.py
```

The application will open a window with a form that you can use to enter the values of the two known quantities and the relationship between them. The application will then calculate the value of the third quantity and display it in the window.

### Code Explanation

The code for the application is divided into two files:

* `regla_de_tres.py`: This file contains the main code for the application.
* `main.py`: This file imports the `regla_de_tres` module and creates the window for the application.

The `regla_de_tres` module contains the following functions:

* `calcular_regla_de_tres()`: This function calculates the value of the third quantity using the rule of three.
* `main()`: This function creates the window for the application and sets up the event handlers for the widgets.

The `main.py` file imports the `regla_de_tres` module and creates the window for the application. The window contains the following widgets:

* `lbl_instruccion`: A label that instructs the user to complete the phrase.
* `lbl_frase`: A label that displays the phrase that the user is to complete.
* `entry_valor_a`: A text entry widget where the user can enter the value of the first known quantity.
* `entry_valor_b`: A text entry widget where the user can enter the value of the second known quantity.
* `entry_valor_x