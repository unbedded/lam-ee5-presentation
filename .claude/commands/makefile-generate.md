Generate language-appropriate Makefile with standardized quality and testing targets: $ARGUMENTS

**Usage:** `/makefile-generate [--language <lang>] [--force]`

**Options:**
- `--language <lang>` - Target language: `python`, `cpp`, `mixed`, `auto` (default: auto-detect)
- `--force` - Overwrite existing Makefile without confirmation

**Examples:**
- `/makefile-generate` → Auto-detect project language and generate appropriate Makefile
- `/makefile-generate --language python` → Generate Python Makefile (ruff + mypy + pytest)
- `/makefile-generate --language cpp` → Generate C++ Makefile (CMake + GTest + clang-format)
- `/makefile-generate --force` → Overwrite existing Makefile without confirmation

## Simplified Language Detection

### **Automatic Detection Logic:**
```bash
# Simple, reliable detection
if [ -f "CMakeLists.txt" ]; then
    LANGUAGE="cpp"
elif [ -f "pyproject.toml" ] || [ -f "setup.py" ] || [ -d "src" -a -n "$(find src -name '*.py')" ]; then
    LANGUAGE="python"
elif [ -n "$(find . -maxdepth 2 -name '*.cpp' -o -name '*.hpp')" ]; then
    LANGUAGE="cpp"
elif [ -n "$(find . -maxdepth 2 -name '*.py')" ]; then
    LANGUAGE="python"
else
    LANGUAGE="python"  # Default for new projects
fi
```

### **Hardcoded Technology Stacks:**

#### **Python Stack (Standardized):**
- **Formatter**: ruff format
- **Linter**: ruff check
- **Type Checker**: mypy
- **Test Runner**: pytest
- **Coverage**: pytest-cov

#### **C++ Stack (Standardized):**
- **Build System**: CMake (required)
- **Test Framework**: Google Test (GTest)
- **Formatter**: clang-format
- **Static Analyzer**: clang-tidy
- **Compiler**: Any (CMake handles detection)

## Generated Makefile Templates

### **Python Makefile:**
```makefile
# Python Project Makefile

.PHONY: help quality test test-full format lint typecheck clean install

# Default target
help: ## Show this help message
	@echo "Available targets:"
	@echo "  quality     - Run complete quality pipeline (format + lint + typecheck)"
	@echo "  test        - Run test suite (quick)"
	@echo "  test-full   - Run tests with coverage report"
	@echo "  format      - Format code with ruff"
	@echo "  lint        - Lint code with ruff"
	@echo "  typecheck   - Type check with mypy"
	@echo "  clean       - Clean build artifacts and cache"
	@echo "  install     - Install project in development mode"

# Quality pipeline (used by git-flow commands)
quality: format lint typecheck ## Run complete quality pipeline

format: ## Format code with ruff
	ruff format .

lint: ## Lint code with ruff
	ruff check .

typecheck: ## Type check with mypy
	mypy .

# Testing (used by git-flow commands)
test: ## Run test suite quickly
	pytest -q

test-full: ## Run tests with coverage
	pytest --cov=src --cov-report=html --cov-report=term

# Development
install: ## Install project dependencies
	pip install -e .
	@if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	@if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/
	rm -rf htmlcov/ .coverage .pytest_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Version management
version-show: ## Display current version
	@cat VERSION 2>/dev/null || echo "No VERSION file found"

version-sync: ## Sync VERSION file to Python project files
	@if [ -f VERSION ]; then \
		VERSION=$$(cat VERSION) && \
		if [ -f pyproject.toml ]; then \
			sed -i.bak 's/version = ".*"/version = "'$$VERSION'"/' pyproject.toml && rm pyproject.toml.bak; \
		fi && \
		find src -name "__init__.py" -exec sed -i.bak 's/__version__ = ".*"/__version__ = "'$$VERSION'"/' {} \; -exec rm {}.bak \; 2>/dev/null || true; \
		echo "Synced version $$VERSION to Python project files"; \
	else \
		echo "No VERSION file found"; \
	fi

version-check: ## Validate version consistency
	@if [ -f VERSION ]; then \
		VERSION=$$(cat VERSION) && \
		echo "Checking version consistency for $$VERSION..." && \
		if [ -f pyproject.toml ]; then \
			grep -q "version = \"$$VERSION\"" pyproject.toml || echo "⚠️  pyproject.toml version mismatch"; \
		fi && \
		echo "✅ Version consistency check complete"; \
	else \
		echo "❌ No VERSION file found"; \
	fi
```

### **C++ Makefile:**
```makefile
# C++ Project Makefile
# Assumes: CMake + GTest + clang-format + clang-tidy

BUILD_DIR := build
CMAKE_BUILD_TYPE ?= Debug
SRC_DIR := src
TESTS_DIR := tests

.PHONY: help quality test test-full format lint build clean install configure

# Default target
help: ## Show this help message
	@echo "Available targets:"
	@echo "  quality     - Run complete quality pipeline (format + lint + build)"
	@echo "  test        - Run test suite with GTest"
	@echo "  test-full   - Run tests with verbose output"
	@echo "  format      - Format code with clang-format"
	@echo "  lint        - Static analysis with clang-tidy"
	@echo "  build       - Build project with CMake"
	@echo "  configure   - Configure CMake build"
	@echo "  clean       - Clean build directory"
	@echo "  install     - Build and install project"

# Quality pipeline (used by git-flow commands)
quality: format lint build ## Run complete quality pipeline

format: ## Format code with clang-format
	@find $(SRC_DIR) $(TESTS_DIR) -name "*.cpp" -o -name "*.hpp" -o -name "*.cc" -o -name "*.h" | \
		xargs clang-format -i
	@echo "✅ Code formatted with clang-format"

lint: ## Static analysis with clang-tidy
	@if [ -d "$(BUILD_DIR)" ]; then \
		find $(SRC_DIR) -name "*.cpp" | xargs clang-tidy -p $(BUILD_DIR); \
	else \
		echo "⚠️  Build directory not found. Run 'make configure' first."; \
	fi

build: configure ## Build project with CMake
	cmake --build $(BUILD_DIR)

# Testing (used by git-flow commands)
test: build ## Run GTest test suite
	cd $(BUILD_DIR) && ctest --output-on-failure -j$$(nproc)

test-full: build ## Run tests with verbose output
	cd $(BUILD_DIR) && ctest --output-on-failure --verbose

# Development
configure: ## Configure CMake build
	cmake -B $(BUILD_DIR) -DCMAKE_BUILD_TYPE=$(CMAKE_BUILD_TYPE) \
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON

install: build ## Build and install project
	cmake --build $(BUILD_DIR) --target install

clean: ## Clean build directory
	rm -rf $(BUILD_DIR)

# Version management
version-show: ## Display current version
	@cat VERSION 2>/dev/null || echo "No VERSION file found"

version-sync: ## Sync VERSION file to C++ project files
	@if [ -f VERSION ]; then \
		VERSION=$$(cat VERSION) && \
		if [ -f CMakeLists.txt ]; then \
			sed -i.bak 's/VERSION [0-9.]\+/VERSION '$$VERSION'/' CMakeLists.txt && rm CMakeLists.txt.bak; \
		fi && \
		if [ ! -d include ]; then mkdir -p include; fi && \
		echo "#pragma once" > include/version.hpp && \
		echo "#define PROJECT_VERSION \"$$VERSION\"" >> include/version.hpp && \
		echo "#define PROJECT_VERSION_MAJOR $$(echo $$VERSION | cut -d. -f1)" >> include/version.hpp && \
		echo "#define PROJECT_VERSION_MINOR $$(echo $$VERSION | cut -d. -f2)" >> include/version.hpp && \
		echo "#define PROJECT_VERSION_PATCH $$(echo $$VERSION | cut -d. -f3)" >> include/version.hpp && \
		echo "Synced version $$VERSION to C++ project files"; \
	else \
		echo "No VERSION file found"; \
	fi

version-check: ## Validate version consistency
	@if [ -f VERSION ]; then \
		VERSION=$$(cat VERSION) && \
		echo "Checking version consistency for $$VERSION..." && \
		if [ -f CMakeLists.txt ]; then \
			grep -q "VERSION $$VERSION" CMakeLists.txt || echo "⚠️  CMakeLists.txt version mismatch"; \
		fi && \
		echo "✅ Version consistency check complete"; \
	else \
		echo "❌ No VERSION file found"; \
	fi

# Project setup helpers
setup-gtest: ## Setup Google Test (if not already configured)
	@echo "Ensuring Google Test is configured in CMakeLists.txt..."
	@if ! grep -q "find_package(GTest" CMakeLists.txt; then \
		echo "⚠️  Add Google Test to your CMakeLists.txt:"; \
		echo "   find_package(GTest REQUIRED)"; \
		echo "   enable_testing()"; \
	fi
```

### **Mixed Language Makefile:**
```makefile
# Mixed Python/C++ Project Makefile

# Language detection
PYTHON_FILES := $(shell find . -name "*.py" 2>/dev/null | wc -l)
CPP_FILES := $(shell find . -name "*.cpp" -o -name "*.hpp" 2>/dev/null | wc -l)
HAS_CMAKE := $(shell [ -f CMakeLists.txt ] && echo 1 || echo 0)
HAS_PYTHON := $(shell [ -f pyproject.toml ] || [ $(PYTHON_FILES) -gt 0 ] && echo 1 || echo 0)

.PHONY: help quality test test-full clean install

help: ## Show this help message
	@echo "Mixed Language Project (Python + C++)"
	@echo "Available targets:"
	@echo "  quality     - Run quality pipeline for all languages"
	@echo "  test        - Run test suites for all languages"
	@echo "  test-full   - Run comprehensive tests for all languages"
	@echo "  clean       - Clean all build artifacts"
	@echo "  install     - Install dependencies for all languages"

# Universal targets that delegate to language-specific implementations
quality: ## Run quality pipeline for all detected languages
	@echo "🔍 Running quality checks for detected languages..."
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) quality-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) quality-cpp; fi

test: ## Run tests for all detected languages
	@echo "🧪 Running tests for detected languages..."
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) test-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) test-cpp; fi

test-full: ## Run comprehensive tests for all detected languages
	@echo "🧪 Running comprehensive tests for detected languages..."
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) test-full-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) test-full-cpp; fi

clean: ## Clean all build artifacts
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) clean-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) clean-cpp; fi

install: ## Install dependencies for all languages
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) install-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) install-cpp; fi

# Include language-specific makefiles (auto-generated)
-include Makefile.python
-include Makefile.cpp

# Generate language-specific makefiles if they don't exist
Makefile.python:
	@if [ $(HAS_PYTHON) -eq 1 ]; then \
		echo "Generating Python makefile..."; \
		$(MAKE) -f /dev/null generate-python-makefile; \
	fi

Makefile.cpp:
	@if [ $(HAS_CMAKE) -eq 1 ]; then \
		echo "Generating C++ makefile..."; \
		$(MAKE) -f /dev/null generate-cpp-makefile; \
	fi

version-sync: ## Sync VERSION file to all project files
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) version-sync-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) version-sync-cpp; fi

version-check: ## Validate version consistency across all languages
	@if [ $(HAS_PYTHON) -eq 1 ]; then $(MAKE) version-check-python; fi
	@if [ $(HAS_CMAKE) -eq 1 ]; then $(MAKE) version-check-cpp; fi
```

## Integration with Git-Flow Commands

### **Quality Gates Now Use Makefile:**
- **Before**: `/check-code` command with Python-specific logic
- **After**: `make quality` command that works for any language

### **Test Execution Now Uses Makefile:**
- **Before**: `/run-tests` command with Python-specific logic
- **After**: `make test` command that works for any language

### **Version Management Now Uses Makefile:**
- **Before**: Direct file editing in commands
- **After**: `make version-sync` and `make version-check` that handle language differences

This creates a clean separation: **git-flow commands handle git logic**, **Makefile handles language-specific build/test logic**.