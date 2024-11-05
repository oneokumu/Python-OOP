# Engine class
class Engine:
    def start(self):
        print("Engine has started.")

    def stop(self):
        print("Engine has stopped.")

# Car class that uses an Engine instance
class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Demonstration of composition
car = Car()
car.start_engine()
car.stop_engine()
