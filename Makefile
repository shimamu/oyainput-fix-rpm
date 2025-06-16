# Makefile for building and installing oyainput-fix RPM locally

TOPDIR := $(CURDIR)
SPECDIR := $(TOPDIR)/SPECS
SOURCEDIR := $(TOPDIR)/SOURCES
RPMDIR := $(TOPDIR)/RPMS
SRPMDIR := $(TOPDIR)/SRPMS
BUILDDIR := $(TOPDIR)/BUILD

SPECFILE := oyainput-fix.spec
SPEC_SRC := $(TOPDIR)/$(SPECFILE)
SPEC_DST := $(SPECDIR)/$(SPECFILE)

# Parse Source0 URL or file name from the .spec file
SOURCE0_LINE := $(shell awk '/^Source0:/ {print $$2}' $(SPEC_SRC))
SOURCE_URL := $(SOURCE0_LINE)
SOURCE_FILE := $(notdir $(SOURCE0_LINE))
SOURCE_DST := $(SOURCEDIR)/$(SOURCE_FILE)

.PHONY: all clean dirs install

all: dirs $(SPEC_DST) $(SOURCE_DST)
	rpmbuild \
		--define "_topdir $(TOPDIR)" \
		--define "_sourcedir $(SOURCEDIR)" \
		--define "_specdir $(SPECDIR)" \
		--define "_builddir $(BUILDDIR)" \
		--define "_rpmdir $(RPMDIR)" \
		--define "_srcrpmdir $(SRPMDIR)" \
		-ba $(SPEC_DST)

dirs:
	mkdir -p $(BUILDDIR) $(RPMDIR) $(SRPMDIR) $(SPECDIR) $(SOURCEDIR)

$(SPEC_DST): $(SPEC_SRC) | dirs
	cp -u $(SPEC_SRC) $(SPEC_DST)

$(SOURCE_DST): | dirs
	@if [ -z "$(SOURCE_URL)" ]; then \
		echo "ERROR: Source0 not found in $(SPECFILE)"; exit 1; \
	fi
	@if echo "$(SOURCE_URL)" | grep -qE '^https?://'; then \
		echo "Downloading source from URL: $(SOURCE_URL)"; \
		curl -L -o $(SOURCE_DST) $(SOURCE_URL); \
	else \
		echo "Copying local source file: $(SOURCE_URL)"; \
		cp -u $(TOPDIR)/$(SOURCE_URL) $(SOURCE_DST); \
	fi

install:
	@RPM_FILE=$$(find $(RPMDIR)/x86_64 -type f -name "oyainput-fix-[0-9]*.rpm" ! -name "*debug*" | sort | tail -n 1); \
	if [ -z "$$RPM_FILE" ]; then \
		echo "❌ RPM file not found. Run 'make' first."; \
		exit 1; \
	fi; \
	echo "📦 Installing: $$RPM_FILE"; \
	sudo dnf install -y "$$RPM_FILE"

clean:
	rm -rf $(BUILDDIR) \
		$(RPMDIR) \
		$(SRPMDIR) \
		$(SPECDIR) \
		$(SOURCEDIR)

