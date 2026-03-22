# Async/Await Basics

**Topic:** `async`/`await`  
**Problem:** Nested `.then()` chains were hard to read  
**Solution:** Use `async`/`await` to write sequential code
**Tags:** #javascript #async

```js
async function loadUser(id) {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error('Failed to load user');
  return res.json();
}


// Before: promise chain
fetch("/api/users/42")
  .then(res => res.json())
  .then(user => console.log(user))
  .catch(err => console.error(err));

// After: async/await
async function loadUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error("Failed to load user");
    const user = await res.json();
    console.log(user);
  } catch (err) {
    console.error(err);
  }
}
```
