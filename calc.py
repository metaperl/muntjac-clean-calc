
from muntjac.api import Application, Button, GridLayout, Label, Window

from muntjac.ui.button import IClickListener

from pure_calc import PureCalc

class Calc2(Application, IClickListener):
    """A simple calculator using Muntjac."""

    def __init__(self):
        super(Calc2, self).__init__()

        # All variables are automatically stored in the session.
        self._current = 0.0
        self._stored = 0.0
        self._lastOperationRequested = 'C'

        self.pure_calc = PureCalc()

        # User interface components
        self._display = Label('0.0')


    def init(self):

        layout = GridLayout(4, 5)

        self.setMainWindow(Window('Calculator Application', layout))

        layout.addComponent(self._display, 0, 0, 3, 0)

        operations = ['7', '8', '9', '/', '4', '5', '6',
                '*', '1', '2', '3', '-', '0', '=', 'C', '+']

        for caption in operations:
            # Create a button and use this application for event handling
            button = Button(caption)
            button.addListener(self)

            # Add the button to our main layout
            layout.addComponent(button)


    def buttonClick(self, event):
        # Event handler for button clicks. Called for all the buttons in
        # the application.

        # Get the button that was clicked
        button = event.getButton()

        # Get the requested operation from the button caption
        requestedOperation = button.getCaption()[0]

        self.pure_calc.proc_char(requestedOperation)
        if self.pure_calc.digit_operation(requestedOperation):
            newValue = self.pure_calc._current
        else:
            newValue = self.pure_calc._stored

        # Update the result label with the new value
        self._display.setValue(newValue)


if __name__ == '__main__':
    from muntjac.main import muntjac
    muntjac(Calc2, nogui=True, forever=True, debug=True)
