# Basic Example

```python
# Import necessary modules from the differentiable systems framework
from differentiable_systems import System

# Define a simple system
class BasicSystem(System):
    def __init__(self):
        super().__init__()
        self.state = 0

    def step(self):
        # Update the state
        self.state += 1

    def get_state(self):
        return self.state

# Create an instance of the system
system = BasicSystem()

# Run the system for 5 steps
for _ in range(5):
    system.step()
    print(system.get_state())
```

# This example demonstrates a basic usage of a system within the differentiable systems framework,
# showing how to define a system class, update its state, and retrieve the state after multiple steps.