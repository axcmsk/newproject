.PHONY: check format lint test reformat tools

TOOLS_DIR ?= $(HOME)/go/bin
GOLANGCI_LINT_VERSION := v2.15.0
GOLANGCI_LINT := $(TOOLS_DIR)/golangci-lint-$(GOLANGCI_LINT_VERSION)
empty :=
space := $(empty) $(empty)
TOOL_TARGET := $(subst $(space),\$(space),$(GOLANGCI_LINT))

check: format lint test

format: $(TOOL_TARGET)
	@tmp=$$(mktemp) || exit $$?; trap 'rm -f "$$tmp"' EXIT HUP INT TERM; \
	status=0; "$(GOLANGCI_LINT)" fmt --diff > "$$tmp" || status=$$?; \
	cat "$$tmp"; [ "$$status" -eq 0 ] || exit "$$status"; test ! -s "$$tmp"

lint: $(TOOL_TARGET)
	"$(GOLANGCI_LINT)" run

test:
	go test ./...

reformat: $(TOOL_TARGET)
	"$(GOLANGCI_LINT)" fmt

tools: $(TOOL_TARGET)

$(TOOL_TARGET):
	@mkdir -p "$(TOOLS_DIR)" || exit $$?; \
	stage=$$(mktemp -d "$(TOOLS_DIR)/.golangci-lint.XXXXXX") || exit $$?; \
	trap 'rm -rf "$$stage"' EXIT HUP INT TERM; \
	curl -sSfL https://golangci-lint.run/install.sh -o "$$stage/install.sh" || exit $$?; \
	sh "$$stage/install.sh" -b "$$stage" "$(GOLANGCI_LINT_VERSION)" || exit $$?; \
	test -x "$$stage/golangci-lint" || { echo 'golangci-lint installation did not produce an executable' >&2; exit 1; }; \
	mv "$$stage/golangci-lint" "$(GOLANGCI_LINT)"
