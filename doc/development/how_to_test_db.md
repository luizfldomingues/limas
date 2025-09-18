## How to execute db methods from outside of the application
Since we are using the application context to handle the database connections, an extra step is needed for executing db methods outside of the application.
One can do that doing simulating an application context doing:

```python3
from app import *
with app.app_context():
    db.example()
```
