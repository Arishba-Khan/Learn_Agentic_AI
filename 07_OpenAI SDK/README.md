## 1️⃣ Why is the Agent class defined as a dataclass?
Using @dataclass makes the Agent class cleaner and easier to manage.

It automatically creates an __init__ method, which helps when defining agents with fixed properties like name, instructions, tools, etc.

This makes the agent’s structure declarative and readable.

---

## 2️⃣ Why is the system prompt stored in Agent.instructions, and why can it be callable?
instructions define the system prompt – like what role the agent is playing.

It can also be a callable (function) if the prompt needs to change based on input. This allows dynamic behavior.

## 2️⃣b) Why is the user prompt passed to Runner.run() and why is it a classmethod?
The user prompt is passed at runtime — it changes each time a user inputs something.

Runner.run() is a @classmethod so it can be called directly on the class (Runner.run(...)) without making an instance.

---

## 3️⃣ What is the purpose of the Runner class?
Runner manages how the agent runs: it takes in the prompt, calls the tools, handles outputs, and interacts with OpenAI behind the scenes.

It's like the manager that controls the Agent’s actions during runtime.

---

## 4️⃣ What are generics in Python and why use TContext?
Generics allow classes/functions to be written in a flexible way for different types.

TContext is a generic placeholder type. It helps the agent share data (context) during its run, while still keeping it type-safe.

