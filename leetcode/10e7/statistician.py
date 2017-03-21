from datetime import datetime, timedelta


class Historian:
    def __init__(self, memory=10):
        if memory % 2 != 0:
            raise Exception('Memory must be a power of two')

        self.buffer = [None]*memory
        self.next = 0


    def remember(self, dt, counter):
        self.buffer[self.next] = (dt, counter)
        self.next = (self.next+1) % len(self.buffer)


    def average_speed(self):
        if self.buffer[self.next] is None:
           raise Exception('Buffer has not yet filled!')

        [s_t, s_c] = self.buffer[self.next]
        [e_t, e_c] = self.buffer[self.next-1]
        return (e_c-s_c)/(e_t-s_t).seconds


    def expected(self, target=10e7):
        [l_t, l_c] = self.buffer[self.next-1]
        return datetime.now() + timedelta(seconds=(target-l_c)/self.average_speed())