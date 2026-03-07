# There are three design pattern used, which are factory method, singleton and observer pattern.


1. The Factory Method pattern is used to create objects without exposing the creation logic to the client.
Instead of directly instantiating Helper or Friend objects in main.py, the Maker class handles object creation
based on the given unit_type. This allows the program to decide at runtime which subclass of Unit should be created,
while the calling code remains unchanged.

    # Advantages

    Promotes loose coupling between object creation and usage
    Makes the system easy to extend (new unit types can be added easily)
    Improves code readability and maintainability

    # Disadvantages

    Factory class can become complex if many types are added
    Requires updating the factory method when new unit types are introduced



2. The Singleton pattern ensures that only one instance of the Keeper class exists throughout the application.
This is achieved using a metaclass that controls object creation. In main.py, even if Keeper() is called multiple times,
the same instance is returned. This ensures that all units are managed by a single central manager.

    # Advantages

    Guarantees a single shared instance
    Useful for managing shared resources or global state
    Prevents accidental creation of multiple managers

    # Disadvantages

    Introduces global state, which can make testing harder
    Reduces flexibility if multiple instances are needed in the future
    Can lead to tight coupling if overused



3. The Observer pattern allows multiple objects to be notified of an event without tightly coupling them to the event source.
In this project, Screen and Record act as observers that respond to unit actions by displaying or recording messages.
In main.py, both observers are notified whenever a unit completes an action.

    # Advantages

    Promotes loose coupling between event producers and consumers
    Easy to add new observers without modifying existing logic
    Supports event-driven design

    # Disadvantages

    Notification order is not guaranteed
    Can be harder to debug when many observers are involved
    Performance may degrade if many observers are added