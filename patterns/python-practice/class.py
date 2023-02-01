class Car:
    color = 'red'
    wheels = 4

    def start(self):
        print('started')

    def stop(self):
        print('stopped')

nano = Car()
tesla = Car()
print(nano.color)
print(nano.wheels)
print(tesla.color)
print(tesla.wheels)
nano.start()
nano.stop()
tesla.start()
tesla.stop()
