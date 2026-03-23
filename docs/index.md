# Dev Journal

Short, practical notes from learning **JavaScript**, **React**, and **.NET** that map directly to real work.

- Keep entries tiny (problem → solution → snippet)
- Tag consistently (e.g., `#async`, `#linq`, `#hooks`)
- Review weekly (Sun PM: scan last 7 days)

Use the search box to find snippets fast.

## Browse Notes

- [Recent notes](recent-notes.md)
- [JavaScript note index](javascript/note-index.md)
- [React note index](react/note-index.md)
- [.NET note index](dotnet/note-index.md)

## New Entry

<section class="entry-composer" data-entry-composer>
  <button type="button" class="entry-composer__toggle" data-entry-toggle>
    Create a New Journal Entry
  </button>

  <div class="entry-composer__panel" data-entry-panel hidden>
    <div class="entry-composer__intro">
      Build a Markdown note in the browser, then copy it into the repo when you're ready.
    </div>

    <label class="entry-composer__field">
      <span>Title</span>
      <input type="text" name="title" placeholder="Example: Debugging fetch errors" data-entry-title />
    </label>

    <label class="entry-composer__field">
      <span>Entry content</span>
      <textarea
        name="content"
        rows="8"
        placeholder="Write your journal entry here..."
        data-entry-content
      ></textarea>
    </label>

    <div class="entry-composer__actions">
      <button type="button" class="md-button md-button--primary" data-entry-generate>
        Generate Markdown
      </button>
      <button type="button" class="md-button" data-entry-copy disabled>
        Copy Markdown
      </button>
    </div>

    <p class="entry-composer__meta">
      <strong>Filename:</strong> <span data-entry-filename>Waiting for a title...</span>
    </p>

    <label class="entry-composer__field">
      <span>Generated Markdown</span>
      <textarea
        name="markdown"
        rows="14"
        readonly
        placeholder="Your generated Markdown will appear here."
        data-entry-output
      ></textarea>
    </label>

    <p class="entry-composer__status" data-entry-status aria-live="polite"></p>
  </div>
</section>
