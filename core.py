# Lazy array proxying a function (index->value)
class LazyArray:
    def __init__(self,size,fun):
        self._size = size
        self._fun = fun
        self._cache = {}
    def __len__(self):
        return self._size
    def __getitem__(self,i):
        if isinstance(i,slice):
            start = i.start if i.start != None else 0
            end = i.stop if i.stop != None else self._size
            newlen = end-start
            return LazyArray(newlen,lambda ii: self[ii+start])
        else:
            if i >= self._size:
                raise KeyError('Accessing {} in an array with {} elements'.format(i,self._size))
                
            if i < 0:
                i += self._size

            if i in self._cache:
                return self._cache[i]
            else:
                self._cache[i] = val = self._fun(i)
                return val
        
# Tests the function against test cases in file located at txt
def test(fun,txt):
    with open(txt,'r') as tests:
        for test in tests:
            print(test,end='')
            if test[0]=='#':
                continue
            else:
                args, expected = [eval(x) for x in test.split('==')]
                result = fun(*args)
                if not result == expected:
                    raise Exception('Failed with expected {} != return value {}'.format(expected, result))