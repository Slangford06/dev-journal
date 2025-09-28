# React `useEffect` Cleanup

**Topic:** Abort fetch on unmount  
**Problem:** State update after unmount → memory leak warning  
**Solution:** AbortController in cleanup

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(r => r.json())
    .then(setData)
    .catch(err => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort();
}, []);
