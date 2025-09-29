# Variables/let/const Basics

**Topic:** `let`/`const`  
**Problem:** `var` is global and can cause errors  
**Solution:** Use `let`/`const` to set variables after 2015

```js
if(true) {
    let name = "Nathan";
}

console.log(name)  // Error: name is not defined

`var` is a global variable that should not be used today

`let` is used to define a variable tht can change - camelCase is a common format

`const` is used to define a fixed variable that cannot change - typically ALL_CAPS are used to make stand out