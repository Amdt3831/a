class RoseDictionary(object):
    def __init__(self):
        self.t = {}

    def __setitem__(self, key, value):
        self.t[key] = value

    def __getitem__(self, item):
        return self.t[item]

    def pop_item(self, raise_error=False, default=None,
                 error_msg=None):
        if len(list(self.t)) != 0:
            a = self.t[list(self.t)[-1]]
            del self.t[list(self.t)[-1]]
            return a
        elif raise_error is False and default is not None:
            return default
        elif raise_error is False and default is None:
            if error_msg is not None:
                return print(error_msg)
            else:
                return print('Dictionary was empty and no default value/message was specified.')
        elif raise_error is True and error_msg is not None:
            raise KeyError(error_msg)
        elif raise_error is True and error_msg is None:
            return 'Dictionary was empty and no default value/message was specified.'

    def get_item(self,key, raise_error=False, default=None,
                 error_msg=None):
        if key in self.t:
            return self.t[key]
        elif raise_error is False and default is not None:
            return default
        elif raise_error is False and default is None:
            if error_msg is not None:
                return print(error_msg)
            else:
                return print('Value was not found and no default value/message was specified.')
        elif raise_error is True and error_msg is not None:
            raise KeyError(error_msg)
        elif raise_error is True and error_msg is None:
            return 'Value was not found and no default value/message was specified.'


