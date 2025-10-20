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
# ARTIFACT GENERATION - Python scripts
# ============================================================================

# Generate architecture artifacts from YAML/CSV sources
arch-gen:
	@echo "Generating architecture artifacts..."
	@python3 scripts/generate_arch_artifacts.py
	@echo "✅ Architecture artifacts generated"

# Generate trade-off analysis charts (two-stage pipeline)
# Stage 1: Extract data from YAML sources into JSON
tradeoff-extract:
	@echo "Extracting trade-off data from YAML sources..."
	@python3 scripts/extract_tradeoff_data.py
	@echo "✅ Data extracted to data/tradeoff-data.json"

# Stage 2: Plot charts from extracted JSON data
tradeoff-plot:
	@echo "Plotting trade-off charts from JSON data..."
	@python3 scripts/plot_tradeoff_charts.py
	@echo "✅ Charts plotted to source/images/"

# Full pipeline: Extract → Plot
tradeoff-charts: tradeoff-extract tradeoff-plot
	@echo "✅ Trade-off analysis complete"

# Generate all artifacts (architecture + requirements + charts)
# NOTE: Requirement artifacts use Claude Code slash commands:
#   /req-yaml-to-md, /req-audit, /req-trace, /req-risk-report
artifacts: arch-gen tradeoff-charts
	@echo "✅ All artifacts generated"

# ============================================================================
# BUILD RULES - Pattern-based rules for auto-discovery
# ============================================================================

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
	elif echo "$<" | grep -qE "(presentation|practice)"; then \
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

# ============================================================================
# APPENDIX PDF GENERATION - Reference materials for presentation
# ============================================================================

# Create appendix directory
artifacts/appendix:
	@mkdir -p artifacts/appendix

# Convert key markdown files to appendix PDFs
artifacts/appendix/requirements.pdf: artifacts/requirements.md $(STYLE) | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ $(STD_OPTS)
	@echo "✓ Created $@"

artifacts/appendix/architecture.pdf: artifacts/architecture.md $(STYLE) | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ $(STD_OPTS)
	@echo "✓ Created $@"

artifacts/appendix/architecture-comparison.pdf: artifacts/architecture-comparison-matrix.md $(STYLE) | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ $(STD_OPTS)
	@echo "✓ Created $@"

# Convert CSV BOMs to PDF (via pandoc CSV reader)
artifacts/appendix/bom-piezo-eco.pdf: artifacts/bom/arch-piezo-eco-bom.csv | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ --pdf-engine=$(PDF_ENGINE) -V geometry:margin=0.5in -V fontsize=9pt -V mainfont="$(FONT)"
	@echo "✓ Created $@"

artifacts/appendix/bom-sol-eco.pdf: artifacts/bom/arch-sol-eco-bom.csv | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ --pdf-engine=$(PDF_ENGINE) -V geometry:margin=0.5in -V fontsize=9pt -V mainfont="$(FONT)"
	@echo "✓ Created $@"

artifacts/appendix/bom-piezo-dlx.pdf: artifacts/bom/arch-piezo-dlx-bom.csv | artifacts/appendix
	@echo "Converting $< -> $@..."
	$(PANDOC) $< -o $@ --pdf-engine=$(PDF_ENGINE) -V geometry:margin=0.5in -V fontsize=9pt -V mainfont="$(FONT)"
	@echo "✓ Created $@"

# Generate all appendix PDFs
appendix: artifacts/appendix/requirements.pdf \
          artifacts/appendix/architecture.pdf \
          artifacts/appendix/architecture-comparison.pdf \
          artifacts/appendix/bom-piezo-eco.pdf \
          artifacts/appendix/bom-sol-eco.pdf \
          artifacts/appendix/bom-piezo-dlx.pdf
	@echo ""
	@echo "✅ All appendix PDFs generated in artifacts/appendix/"
	@echo ""
	@echo "Reference from presentation PDF using relative paths:"
	@echo "  appendix/requirements.pdf"
	@echo "  appendix/architecture.pdf"
	@echo "  appendix/bom-piezo-eco.pdf"
	@echo ""

# Clean appendix PDFs
appendix-clean:
	rm -rf artifacts/appendix
	@echo "Cleaned appendix PDFs"

# ============================================================================
# PRACTICE GUIDE - Quick PDF generation for practice sessions
# ============================================================================

# Generate practice guide PDF (large font for reading while practicing)
practice: source/practice-guide.md $(STYLE)
	@echo "Converting practice guide to PDF..."
	$(PANDOC) source/practice-guide.md -o artifacts/practice-guide.pdf $(PRES_OPTS)
	@echo "✓ artifacts/practice-guide.pdf generated"
	@echo ""
	@echo "Print this for practice sessions or reference on mobile device"
	@echo ""

# ============================================================================
# PRESENTATION GENERATION - Markdown → PPTX workflow
# ============================================================================

# Generate presentation with Marp (RECOMMENDED: HTML presentation + PDF export)
marp: source/presentation-marp.md
	@echo "Generating presentation with Marp..."
	@echo "Copying images to artifacts/images/ for HTML presentation..."
	@mkdir -p artifacts/images
	@cp -f source/images/* artifacts/images/ 2>/dev/null || true
	@marp source/presentation-marp.md -o artifacts/presentation-marp.html --allow-local-files
	@marp source/presentation-marp.md -o artifacts/presentation-marp.pdf --allow-local-files --pdf
	@echo "✓ artifacts/presentation-marp.html generated (HTML presentation)"
	@echo "✓ artifacts/presentation-marp.pdf generated (PDF for distribution)"
	@echo ""
	@echo "RECOMMENDED: Present from HTML (fully editable Markdown source)"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Present: firefox artifacts/presentation-marp.html (press F11 for fullscreen)"
	@echo "  2. Edit: vim source/presentation-marp.md (then 'make marp' to regenerate)"
	@echo "  3. Share PDF: artifacts/presentation-marp.pdf"
	@echo ""
	@echo "Navigation: Arrow keys, Space=next, Shift+Space=prev"
	@echo "Font control: Edit 'style:' section in source/presentation-marp.md"
	@echo ""
	@echo "⚠️  NOTE: PPTX export exists but slides are NOT EDITABLE (images only)"
	@echo "   If you need editable PPTX: Upload HTML to Google Slides instead"

# Clean presentation files
presentation-clean:
	rm -f artifacts/presentation-marp.html artifacts/presentation-marp.pdf
	rm -rf artifacts/images
	@echo "Cleaned Marp presentation files and images"

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
email-pres: artifacts/presentation-marp.pdf
	@if [ -z "$(EMAIL)" ]; then \
		echo "Error: Please specify EMAIL=recruiter@email.com"; \
		exit 1; \
	fi
	@echo "Emailing presentation to $(EMAIL)..."
	@echo "Opening email client with attachment..."
	xdg-email --subject "Lam Research EE Interview - Presentation Materials" \
	          --body "Please find attached my presentation materials for the upcoming interview." \
	          --attach artifacts/presentation-marp.pdf \
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
	@echo "Artifact Generation (Python):"
	@echo "  make arch-gen                - Generate architecture docs/BOMs from YAML/CSV"
	@echo "  make tradeoff-extract        - Extract trade-off data (YAML → JSON)"
	@echo "  make tradeoff-plot           - Plot charts from JSON data"
	@echo "  make tradeoff-charts         - Full pipeline (extract + plot)"
	@echo "  make artifacts               - Generate all artifacts (arch + requirements + charts)"
	@echo ""
	@echo "Presentation Generation:"
	@echo "  make marp                    - Generate HTML presentation with Marp"
	@echo "  make practice                - Generate practice guide PDF (large font)"
	@echo "  make presentation-clean      - Remove generated presentation files"
	@echo ""
	@echo "PDF Conversion (Pandoc):"
	@echo "  make all                     - Convert all .md files to PDF"
	@echo "  make appendix                - Generate appendix PDFs (requirements, BOMs, architecture)"
	@echo "  make appendix-clean          - Remove appendix PDFs"
	@echo "  make analysis                - Build only technical analysis PDF"
	@echo "  make rubrics                 - Build only rubric PDFs"
	@echo "  make clean                   - Remove all PDF files"
	@echo "  make rebuild                 - Clean and rebuild all PDFs"
	@echo ""
	@echo "Utilities:"
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
	@echo "  - marp-cli (npm install -g @marp-team/marp-cli) - for HTML presentations"
	@echo "  - pandoc - for PDF generation"
	@echo "  - xelatex (texlive-xetex package) - for PDF generation"
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

.PHONY: all clean rebuild marp practice presentation-clean analysis rubrics print print-to email-pres list check help arch-gen tradeoff-extract tradeoff-plot tradeoff-charts artifacts appendix appendix-clean
