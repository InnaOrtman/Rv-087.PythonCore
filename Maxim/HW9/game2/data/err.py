class MyErr(Exception):
    """Not a valid data user input"""

    def __init__(self, errMsg):
        self.errMsg = errMsg

    def __str__(self):
        return self.errMsg
