#!/usr/bin/env python3
"""
Convert Markdown presentation to PowerPoint outline format.
PowerPoint can import this text file and auto-generate slides.
"""

import sys
import re

def convert_md_to_outline(md_file, outline_file):
    """Convert Markdown to PowerPoint outline format."""

    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    outline = []
    skip_notes = False
    skip_yaml = False

    for line in lines:
        # Skip YAML frontmatter
        if line.strip() == '---':
            skip_yaml = not skip_yaml
            continue
        if skip_yaml:
            continue

        # Skip speaker notes
        if line.strip() == '::: notes':
            skip_notes = True
            continue
        if skip_notes and line.strip() == ':::':
            skip_notes = False
            continue
        if skip_notes:
            continue

        # Skip horizontal rules
        if line.strip() == '---':
            continue

        # Skip images
        if line.strip().startswith('!['):
            continue

        # Convert headings
        if line.startswith('# '):
            # H1 = Slide title (no indent)
            title = line.replace('# ', '').strip()
            outline.append(f"{title}\n")

        elif line.startswith('## '):
            # H2 = Subtitle or section (1 tab indent)
            subtitle = line.replace('## ', '').strip()
            outline.append(f"\t{subtitle}\n")

        elif line.startswith('### '):
            # H3 = Sub-point (2 tab indent)
            subpoint = line.replace('### ', '').strip()
            outline.append(f"\t\t{subpoint}\n")

        # Convert bullets
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            # Top-level bullet (1 tab)
            bullet = re.sub(r'^[\s\-\*]+', '', line).strip()
            outline.append(f"\t{bullet}\n")

        # Convert nested bullets
        elif line.strip().startswith('  - ') or line.strip().startswith('  * '):
            # Nested bullet (2 tabs)
            bullet = re.sub(r'^[\s\-\*]+', '', line).strip()
            outline.append(f"\t\t{bullet}\n")

        # Convert tables (simplified - just list rows)
        elif line.strip().startswith('|') and not line.strip().startswith('|---'):
            # Table row - convert to bullet
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and cells[0] and not cells[0].startswith('-'):
                # Skip header separator, keep content
                row_text = ' | '.join(cells)
                outline.append(f"\t{row_text}\n")

        # Regular paragraph text (1 tab indent)
        elif line.strip() and not line.strip().startswith('```'):
            # Skip code blocks
            if '```' in line:
                continue
            # Regular text becomes body text
            outline.append(f"\t{line.strip()}\n")

    # Write outline file
    with open(outline_file, 'w', encoding='utf-8') as f:
        f.writelines(outline)

    print(f"✓ Converted {md_file} → {outline_file}")
    print(f"  {len(outline)} lines generated")
    print()
    print("Next steps:")
    print("1. Open PowerPoint or LibreOffice Impress")
    print("2. File → Open → Select outline file")
    print("3. PowerPoint will auto-generate slides from outline")
    print()
    print("Or in PowerPoint:")
    print("1. View → Outline")
    print("2. Copy/paste contents of outline file")
    print("3. Slides auto-generate as you paste")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 md-to-outline.py input.md output.txt")
        sys.exit(1)

    convert_md_to_outline(sys.argv[1], sys.argv[2])
