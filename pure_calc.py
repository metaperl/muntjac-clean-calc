
class PureCalc():
    """A pure calculator"""

    def __init__(self):

        self._current = 0.0
        self._stored = 0.0
        self._lastOperationRequested = 'C'


    def proc(self, s):
        for c in s:
            self.proc_char(c)

    def digit_operation(self, c):
        return c in "7894561230"

    def proc_char(self, c):
        if self.digit_operation(c):
            self.handle_digit(c)
        else:
            self.handle_store(c)

    def handle_digit(self, d):
        self._current = ((self._current * 10) + float('' + d))

    def handle_store(self, requested_operation):
        last = self._lastOperationRequested
        if last == '+':
            self._stored += self._current
        elif last == '-':
            self._stored -= self._current
        elif last == '/':
            try:
                self._stored /= self._current
            except ZeroDivisionError:
                pass
        elif last == '*':
            self._stored *= self._current
        elif last == 'C':
            self._stored = self._current

        self._lastOperationRequested = requested_operation
        self._current = 0.0

        if requested_operation == 'C':
            self._stored = 0.0


def run_test(s):
    c = PureCalc()
    c.proc(s)
    print "{0} -> {1}".format(s, c._stored)



if __name__ == '__main__':
    tests = [ '444+2=', '55*2=', '787/2=', '999-222=' ]
    for test in tests:
        run_test(test)
