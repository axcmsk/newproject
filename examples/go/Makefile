.PHONY: check format lint test reformat tools

TOOLS_DIR ?= $(HOME)/go/bin
GOLANGCI_LINT := $(TOOLS_DIR)/golangci-lint
GOLANGCI_LINT_VERSION := v2.15.0

check: format lint test

format: tools
	@tmp=$$(mktemp) || exit $$?; trap 'rm -f "$$tmp"' EXIT HUP INT TERM; \
	status=0; "$(GOLANGCI_LINT)" fmt --diff > "$$tmp" || status=$$?; \
	cat "$$tmp"; [ "$$status" -eq 0 ] || exit "$$status"; test ! -s "$$tmp"

lint: tools
	"$(GOLANGCI_LINT)" run

test:
	go test ./...

reformat: tools
	"$(GOLANGCI_LINT)" fmt

tools:
	@if [ ! -x "$(GOLANGCI_LINT)" ]; then \
		mkdir -p "$(TOOLS_DIR)" || exit $$?; \
		tmp=$$(mktemp) || exit $$?; trap 'rm -f "$$tmp"' EXIT HUP INT TERM; \
		curl -sSfL https://golangci-lint.run/install.sh -o "$$tmp" || exit $$?; \
		sh "$$tmp" -b "$(TOOLS_DIR)" "$(GOLANGCI_LINT_VERSION)" || exit $$?; \
		test -x "$(GOLANGCI_LINT)" || { echo 'golangci-lint installation did not produce an executable' >&2; exit 1; }; \
	fi
