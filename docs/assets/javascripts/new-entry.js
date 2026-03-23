(function () {
  const initEntryComposer = () => {
    const composer = document.querySelector("[data-entry-composer]");
    if (!composer || composer.dataset.entryComposerReady === "true") return;
    composer.dataset.entryComposerReady = "true";

    const toggle = composer.querySelector("[data-entry-toggle]");
    const panel = composer.querySelector("[data-entry-panel]");
    const titleInput = composer.querySelector("[data-entry-title]");
    const contentInput = composer.querySelector("[data-entry-content]");
    const generateButton = composer.querySelector("[data-entry-generate]");
    const copyButton = composer.querySelector("[data-entry-copy]");
    const output = composer.querySelector("[data-entry-output]");
    const filename = composer.querySelector("[data-entry-filename]");
    const status = composer.querySelector("[data-entry-status]");

    const getToday = () => {
      const now = new Date();
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, "0");
      const day = String(now.getDate()).padStart(2, "0");
      return `${year}-${month}-${day}`;
    };

    const toTitleCase = (value) =>
      value
        .split(/\s+/)
        .filter(Boolean)
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");

    const slugify = (value) => {
      const cleaned = value
        .toLowerCase()
        .normalize("NFKD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9\s-]/g, "")
        .trim()
        .replace(/\s+/g, "-")
        .replace(/-+/g, "-");

      return cleaned || "new-entry";
    };

    const updateFilename = () => {
      const title = titleInput.value.trim();
      const date = getToday();
      filename.textContent = `${date}_${slugify(title)}.md`;
    };

    const buildMarkdown = () => {
      const rawTitle = titleInput.value.trim();
      const rawContent = contentInput.value.trim();

      if (!rawTitle || !rawContent) {
        status.textContent = "Add both a title and entry content before generating Markdown.";
        return;
      }

      const date = getToday();
      const title = toTitleCase(rawTitle);
      const markdown = [`# ${title}`, "", `**Date:** ${date}`, "", rawContent].join("\n");

      output.value = markdown;
      copyButton.disabled = false;
      status.textContent = "Markdown generated. Copy it and save it as the filename above.";
    };

    const copyMarkdown = async () => {
      if (!output.value) {
        status.textContent = "Generate the Markdown first.";
        return;
      }

      try {
        await navigator.clipboard.writeText(output.value);
        status.textContent = "Markdown copied to your clipboard.";
      } catch (error) {
        output.focus();
        output.select();
        status.textContent = "Clipboard access was unavailable, but the Markdown is selected for manual copy.";
      }
    };

    toggle.addEventListener("click", () => {
      const isHidden = panel.hasAttribute("hidden");
      if (isHidden) {
        panel.removeAttribute("hidden");
        titleInput.focus();
        status.textContent = `Today's date will be used: ${getToday()}.`;
      } else {
        panel.setAttribute("hidden", "");
        status.textContent = "";
      }
    });

    titleInput.addEventListener("input", updateFilename);
    generateButton.addEventListener("click", buildMarkdown);
    copyButton.addEventListener("click", copyMarkdown);

    updateFilename();
  };

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(initEntryComposer);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initEntryComposer, { once: true });
  } else {
    initEntryComposer();
  }
})();
