## The aims of the lessons
* To write functions that take programmer-defined objects as parameters and return them as results.
* To present functional programming style.

### Time


### Pure Functions
Pure function does not modify any of the objects passed to it as arguments and it has no effect, like displaying a vlue or getting user input, other than returning a value.

### Modifiers
Sometimes it is useful for a function to modify the objects it gets as parameters. 
In that case, the changes are visible to the caller. Functions that work this way are called modifiers.

There is some evidence that programs that use pure functions are faster to develop and less error-prone than programs that use modifiers. But modifiers are convenient at times, and functional programs tend to be less efficient.

#### Functional Programming
Write pure functions whenever it is reasonable and resort to modifiers only if there is a compelling advantage. This approach might be called functional programming.

### Prototyping versus Planning



### Debugging
Invariant(불변식) is a requirement that should always be true.
  
  * int | 0 <= min < 60
  * 0 <= sec < 60
  * hour > 0

Assert statements are useful because they distinguish code that deals with normal conditions from code that checks for errors.
