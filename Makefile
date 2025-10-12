# Makefile to convert Lam Research EE interview markdown files to PDFs
# Searches for .md files in source/ directory
# All PDFs are created in the artifacts/ directory

# ============================================================================
# CONFIGURATION
# ============================================================================

PANDOC = pandoc
PDF_ENGINE = xelatex
FONT = DejaVu Sans
STYLE = style/table-style.tex
MARKDOWN_OPTS = -f markdown+pipe_tables+line_blocks

# Standard document options
STD_MARGIN = 0.75in
STD_FONTSIZE = 10pt
STD_TOC = --toc --toc-depth=2
STD_OPTS = --pdf-engine=$(PDF_ENGINE) \
           -V geometry:margin=$(STD_MARGIN) \
           -V fontsize=$(STD_FONTSIZE) \
           -V mainfont="$(FONT)" \
           $(MARKDOWN_OPTS) \
           --include-in-header=$(STYLE) \
           $(STD_TOC)

# Presentation options (larger font, no TOC)
PRES_MARGIN = 1.0in
PRES_FONTSIZE = 12pt
PRES_OPTS = --pdf-engine=$(PDF_ENGINE) \
            -V geometry:margin=$(PRES_MARGIN) \
            -V fontsize=$(PRES_FONTSIZE) \
            -V mainfont="$(FONT)" \
            $(MARKDOWN_OPTS) \
            --include-in-header=$(STYLE)

# Rubric options (compact, deeper TOC)
RUBRIC_MARGIN = 0.5in
RUBRIC_FONTSIZE = 9pt
RUBRIC_TOC = --toc --toc-depth=3
RUBRIC_OPTS = --pdf-engine=$(PDF_ENGINE) \
              -V geometry:margin=$(RUBRIC_MARGIN) \
              -V fontsize=$(RUBRIC_FONTSIZE) \
              -V mainfont="$(FONT)" \
              $(MARKDOWN_OPTS) \
              --include-in-header=$(STYLE) \
              $(RUBRIC_TOC)

# ============================================================================
# FILE LISTS - Auto-discover .md files in artifacts/
# ============================================================================

# Find all .md files in artifacts/ directory
ARTIFACTS_MD_FILES = $(wildcard artifacts/*.md)

# Generate PDF paths by replacing .md with .pdf
ARTIFACTS_PDF_FILES = $(ARTIFACTS_MD_FILES:.md=.pdf)

# Find all .md files in source/ directory
SOURCE_MD_FILES = $(wildcard source/*.md)

# Generate PDF paths for source files (source/foo.md -> artifacts/foo.pdf)
SOURCE_PDF_FILES = $(patsubst source/%.md,artifacts/%.pdf,$(SOURCE_MD_FILES))

# All PDF files to be created
PDF_FILES = $(ARTIFACTS_PDF_FILES) $(SOURCE_PDF_FILES)

# ============================================================================
# BUILD RULES - Pattern-based rules for auto-discovery
# ============================================================================
# NOTE: For requirement artifact generation, use Claude Code slash commands:
#   /req-yaml-to-md, /req-audit, /req-trace, /req-risk-report
# These cannot be automated in Makefile as they require Claude Code context

# Default target - convert all markdown files to PDF
all: $(PDF_FILES)

# Convert .md files in artifacts/ directory (in-place: artifacts/foo.md -> artifacts/foo.pdf)
artifacts/%.pdf: artifacts/%.md $(STYLE)
	@echo "Converting $<..."
	@if echo "$<" | grep -qE "(rubric|metrics)"; then \
		echo "  Using RUBRIC_OPTS (compact format)"; \
		$(PANDOC) $< -o $@ $(RUBRIC_OPTS); \
	elif echo "$<" | grep -q "presentation"; then \
		echo "  Using PRES_OPTS (large font, no TOC)"; \
		$(PANDOC) $< -o $@ $(PRES_OPTS); \
	else \
		echo "  Using STD_OPTS (standard format)"; \
		$(PANDOC) $< -o $@ $(STD_OPTS); \
	fi
	@echo "Created $@"

# Convert source/*.md to artifacts/*.pdf
artifacts/%.pdf: source/%.md $(STYLE)
	@echo "Converting $< -> $@..."
	@if echo "$<" | grep -qE "(rubric|metrics)"; then \
		echo "  Using RUBRIC_OPTS (compact format)"; \
		$(PANDOC) $< -o $@ $(RUBRIC_OPTS); \
	elif echo "$<" | grep -q "presentation"; then \
		echo "  Using PRES_OPTS (large font, no TOC)"; \
		$(PANDOC) $< -o $@ $(PRES_OPTS); \
	else \
		echo "  Using STD_OPTS (standard format)"; \
		$(PANDOC) $< -o $@ $(STD_OPTS); \
	fi
	@echo "Created $@"

# Clean target - remove all generated PDFs
clean:
	rm -f artifacts/*.pdf
	@echo "Cleaned all PDF files from artifacts/"

# Rebuild target - clean and rebuild all
rebuild: clean all

# Build only presentation materials
presentation: artifacts/presentation.pdf
	@echo "Presentation PDF ready for interview"

# Build only technical analysis
analysis: artifacts/technical-analysis.pdf
	@echo "Technical analysis PDF created"

# Build only rubrics
rubrics: $(RUBRIC_PDFS)
	@echo "All rubric PDFs created"

# Print all PDFs to default printer
print: $(PDF_FILES)
	@echo "Printing $(words $(PDF_FILES)) PDFs to default printer..."
	@for pdf in $(PDF_FILES); do \
		echo "  Printing $$pdf..."; \
		lpr $$pdf; \
	done
	@echo "All PDFs sent to printer"

# Print to specific printer (usage: make print-to PRINTER=printer_name)
print-to: $(PDF_FILES)
	@if [ -z "$(PRINTER)" ]; then \
		echo "Error: Please specify PRINTER=printer_name"; \
		exit 1; \
	fi
	@echo "Printing $(words $(PDF_FILES)) PDFs to $(PRINTER)..."
	@for pdf in $(PDF_FILES); do \
		echo "  Printing $$pdf..."; \
		lpr -P $(PRINTER) $$pdf; \
	done
	@echo "All PDFs sent to $(PRINTER)"

# Email presentation (usage: make email-pres EMAIL=recruiter@email.com)
email-pres: artifacts/presentation.pdf
	@if [ -z "$(EMAIL)" ]; then \
		echo "Error: Please specify EMAIL=recruiter@email.com"; \
		exit 1; \
	fi
	@echo "Emailing presentation to $(EMAIL)..."
	@echo "Opening email client with attachment..."
	xdg-email --subject "Lam Research EE Interview - Presentation Materials" \
	          --body "Please find attached my presentation materials for the upcoming interview." \
	          --attach artifacts/presentation.pdf \
	          $(EMAIL)

# List all markdown files and PDFs
list:
	@echo "Markdown files in source/:"
	@ls -1 source/*.md 2>/dev/null | sed 's|.*/||' || echo "  No markdown files found"
	@echo ""
	@echo "Rubric in project root:"
	@ls -1 interview-rubric.md 2>/dev/null || echo "  Not found"
	@echo ""
	@echo "PDF files in artifacts/:"
	@ls -1 artifacts/*.pdf 2>/dev/null | sed 's|.*/||' || echo "  No PDF files found"

# Check for missing source files
check:
	@echo "Checking for required markdown files..."
	@test -f source/technical-analysis.md || echo "  MISSING: source/technical-analysis.md"
	@test -f source/presentation.md || echo "  MISSING: source/presentation.md"
	@test -f source/phase1-quality-metrics.md || echo "  MISSING: source/phase1-quality-metrics.md"
	@test -f source/phase2-quality-metrics.md || echo "  MISSING: source/phase2-quality-metrics.md"
	@test -f source/phase1-rubric.md || echo "  MISSING: source/phase1-rubric.md"
	@test -f source/phase2-rubric.md || echo "  MISSING: source/phase2-rubric.md"
	@test -f interview-rubric.md || echo "  MISSING: interview-rubric.md"
	@test -f $(STYLE) || echo "  MISSING: $(STYLE)"
	@echo "Check complete"

# Show help
help:
	@echo "Lam Research EE Interview PDF Conversion Makefile"
	@echo "=================================================="
	@echo ""
	@echo "This Makefile converts markdown files to PDFs:"
	@echo "  - source/           (for source documents)"
	@echo "  - project root      (for interview rubric)"
	@echo ""
	@echo "All PDFs are created in artifacts/ directory"
	@echo ""
	@echo "Configuration:"
	@echo "  Font:      $(FONT)"
	@echo "  Engine:    $(PDF_ENGINE)"
	@echo "  Style:     $(STYLE)"
	@echo ""
	@echo "Targets:"
	@echo "  make all                     - Convert all .md files to PDF"
	@echo "  make presentation            - Build only presentation PDF"
	@echo "  make analysis                - Build only technical analysis PDF"
	@echo "  make rubrics                 - Build only rubric PDFs"
	@echo "  make clean                   - Remove all PDF files"
	@echo "  make rebuild                 - Clean and rebuild all PDFs"
	@echo "  make check                   - Check for missing source files"
	@echo "  make list                    - List all markdown and PDF files"
	@echo "  make print                   - Print all PDFs to default printer"
	@echo "  make print-to PRINTER=name   - Print all PDFs to specific printer"
	@echo "  make email-pres EMAIL=addr   - Email presentation PDF"
	@echo "  make help                    - Show this help message"
	@echo ""
	@echo "Special handling:"
	@echo "  - presentation.md            → larger font ($(PRES_FONTSIZE)), no TOC"
	@echo "  - *-rubric.md, *-metrics.md  → compact ($(RUBRIC_FONTSIZE)), deep TOC"
	@echo "  - technical-analysis.md      → standard format ($(STD_FONTSIZE))"
	@echo ""
	@echo "Requirements:"
	@echo "  - pandoc"
	@echo "  - xelatex (texlive-xetex package)"
	@echo "  - $(STYLE) file"
	@echo "  - $(FONT) font"
	@echo ""
	@echo ""
	@echo "Requirement Artifact Generation:"
	@echo "  Use Claude Code slash commands (not Makefile):"
	@echo "    /req-yaml-to-md    - Generate requirements.md from YAML"
	@echo "    /req-audit         - Validate SMART compliance"
	@echo "    /req-trace         - Generate traceability matrix"
	@echo "    /req-risk-report   - Risk-rank assumptions"

.PHONY: all clean rebuild presentation analysis rubrics print print-to email-pres list check help
