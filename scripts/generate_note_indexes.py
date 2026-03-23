from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
SECTION_ORDER = ("javascript", "react", "dotnet")
SKIP_FILES = {"README.md", "note-index.md"}
DATE_PREFIX = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})")
TITLE_LINE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
TAGS_LINE = re.compile(r"^\*\*Tags:\*\*\s+(?P<tags>.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Note:
    section: str
    title: str
    date: str
    display_date: str
    tags: list[str]
    relative_path: str


def main() -> None:
    notes = collect_notes()

    for section in SECTION_ORDER:
        write_section_index(section, notes.get(section, []))

    write_recent_notes(notes)


def collect_notes() -> dict[str, list[Note]]:
    notes_by_section: dict[str, list[Note]] = {}

    for section in SECTION_ORDER:
        section_dir = DOCS_DIR / section
        section_notes: list[Note] = []

        for path in sorted(section_dir.glob("*.md")):
            if path.name in SKIP_FILES:
                continue

            content = path.read_text(encoding="utf-8")
            date = parse_date(path)
            section_notes.append(
                Note(
                    section=section,
                    title=parse_title(path, content),
                    date=date,
                    display_date=format_date(date),
                    tags=parse_tags(content),
                    relative_path=path.name,
                )
            )

        notes_by_section[section] = sorted(section_notes, key=lambda note: note.date, reverse=True)

    return notes_by_section


def parse_date(path: Path) -> str:
    match = DATE_PREFIX.match(path.name)
    if not match:
        raise ValueError(f"Expected date-prefixed filename, got {path.name}")
    return match.group("date")


def parse_title(path: Path, content: str) -> str:
    match = TITLE_LINE.search(content)
    if not match:
        raise ValueError(f"Missing H1 title in {path}")
    return match.group("title")


def parse_tags(content: str) -> list[str]:
    match = TAGS_LINE.search(content)
    if not match:
        return []
    return match.group("tags").split()


def format_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").strftime("%b %d, %Y")


def write_section_index(section: str, notes: list[Note]) -> None:
    section_title = section_display_name(section)
    lines = [
        f"# {section_title} Note Index",
        "",
        f"Auto-generated list of {section_title} notes, newest first.",
        "",
        f"[Back to {section_title} overview](README.md)",
        "",
    ]

    if not notes:
        lines.extend(
            [
                "No notes yet.",
                "",
            ]
        )
    else:
        for note in notes:
            tags = f" | {' '.join(note.tags)}" if note.tags else ""
            lines.append(f"- {note.display_date} | [{note.title}]({note.relative_path}){tags}")
        lines.append("")

    output_path = DOCS_DIR / section / "note-index.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_recent_notes(notes_by_section: dict[str, list[Note]]) -> None:
    all_notes = [note for notes in notes_by_section.values() for note in notes]
    all_notes.sort(key=lambda note: note.date, reverse=True)

    lines = [
        "# Recent Notes",
        "",
        "Auto-generated cross-topic view of the newest journal entries.",
        "",
    ]

    if not all_notes:
        lines.extend(
            [
                "No notes yet.",
                "",
            ]
        )
    else:
        for note in all_notes:
            tags = f" | {' '.join(note.tags)}" if note.tags else ""
            lines.append(
                f"- {note.display_date} | {section_display_name(note.section)} | "
                f"[{note.title}]({note.section}/{note.relative_path}){tags}"
            )
        lines.append("")

    output_path = DOCS_DIR / "recent-notes.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")


def section_display_name(section: str) -> str:
    return {
        "javascript": "JavaScript",
        "react": "React",
        "dotnet": ".NET",
    }[section]


if __name__ == "__main__":
    main()
