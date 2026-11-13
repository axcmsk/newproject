# Go starter

The Makefile and .golangci.yml are starting defaults. Choose your Go module
name, add code and tests, and adapt paths and rules to the project before use.
Generation does not run go mod init or install any dependencies.

Requires Go and GNU Make; the first linter installation also requires curl
and network access on macOS/Linux. Run from the module root:

```sh
make check
make reformat
make test-coverage
```

The default target checks formatting, runs lint and `go test ./...`. Individual
targets are format, lint and test. Reformat applies gofmt and goimports only;
follow it with make check. Use make -C /path/to/project when outside the root.

Formatting and lint install a missing pinned golangci-lint into ~/go/bin with
its version in the filename. Make tools installs it explicitly. Changing
GOLANGCI_LINT_VERSION selects a new file; older versions are preserved.
Installation uses a temporary staging directory. Tool directory paths must not
contain spaces. Existing destination files are reused; a non-executable file
must be repaired or removed explicitly. Test and test-coverage do not install
the linter. Normal Go commands may download dependencies and write caches.

Coverage is optional and excluded from check. One test run produces
coverage/coverage.out, coverage/functions.txt and coverage/index.html; these
outputs are ignored by Git. Each run clears those three files first. Supply
the measured source version, function summary and native profile for review;
HTML is supplementary for browsing source. There is no coverage threshold.
