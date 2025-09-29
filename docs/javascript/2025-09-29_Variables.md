# Async/Await Basics

**Topic:** `let`/`const`  
**Problem:** Nested `.then()` chains were hard to read  
**Solution:** Use `async`/`await` to write sequential code

```js
if(true) {
    let name = "Nathan";
}

console.log(name)  // Error: name is not defined

`var` is a global variable that should not be used today

`let` is used to define a variable tht can change - camelCase is a common format

`const` is used to define a fixed variable that cannot change - typically ALL_CAPS are used to make stand out