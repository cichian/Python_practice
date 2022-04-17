#_SD__baz = 99

class SD:
    
    def test(self):
        self.__baz = 99
        return __baz

print (SD().test())