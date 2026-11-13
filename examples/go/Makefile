.PHONY: check format lint test test-coverage reformat tools

TOOLS_DIR ?= $(HOME)/go/bin
GOLANGCI_LINT_VERSION := v2.15.0
GOLANGCI_LINT := $(TOOLS_DIR)/golangci-lint-$(GOLANGCI_LINT_VERSION)

check: format lint test

format: $(GOLANGCI_LINT)
	@tmp=$$(mktemp) || exit $$?; trap 'rm -f "$$tmp"' EXIT HUP INT TERM; \
	status=0; "$(GOLANGCI_LINT)" fmt --diff > "$$tmp" || status=$$?; \
	cat "$$tmp"; [ "$$status" -eq 0 ] || exit "$$status"; test ! -s "$$tmp"

lint: $(GOLANGCI_LINT)
	"$(GOLANGCI_LINT)" run

test:
	go test ./...

test-coverage:
	mkdir -p coverage
	rm -f coverage/coverage.out coverage/functions.txt coverage/index.html
	go test -coverprofile=coverage/coverage.out ./...
	go tool cover -func=coverage/coverage.out > coverage/functions.txt
	cat coverage/functions.txt
	go tool cover -html=coverage/coverage.out -o coverage/index.html

reformat: $(GOLANGCI_LINT)
	"$(GOLANGCI_LINT)" fmt

tools: $(GOLANGCI_LINT)

$(GOLANGCI_LINT):
	@mkdir -p "$(TOOLS_DIR)" || exit $$?; \
	stage=$$(mktemp -d "$(TOOLS_DIR)/.golangci-lint.XXXXXX") || exit $$?; \
	trap 'rm -rf "$$stage"' EXIT HUP INT TERM; \
	curl -sSfL https://golangci-lint.run/install.sh -o "$$stage/install.sh" || exit $$?; \
	sh "$$stage/install.sh" -b "$$stage" "$(GOLANGCI_LINT_VERSION)" || exit $$?; \
	test -x "$$stage/golangci-lint" || { echo 'golangci-lint installation did not produce an executable' >&2; exit 1; }; \
	mv "$$stage/golangci-lint" "$(GOLANGCI_LINT)"
