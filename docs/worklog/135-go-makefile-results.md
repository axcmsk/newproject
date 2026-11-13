# Go Makefile implementation evidence

Specification: `docs/worklog/133-go-makefile-task.md` at
`6f8a19b8566bd170eddf56fb392059dd38c7b3a1`. Implementation inputs are the
Makefile, configuration and test file in the same commit as this evidence.

- `make check`: passed, 67 tests, exit 0; complete output is saved at
  `/tmp/newproject-135-make-check.log`. Seven new tests use isolated fake tools
  and cover the default and explicit targets, ordering, parallel installation,
  reuse, installer failures, read-only formatting and failure propagation,
  reformatting, lint/test failures, and `make -C`.
- Real tool: Go 1.26.2, GNU Make 3.81, golangci-lint v2.15.0 on darwin/arm64.
  `make -C /tmp/newproject-go-real/module TOOLS_DIR=/tmp/newproject-go-real/tools-official tools`
  installed the pinned release into the temporary directory using the official
  installer and its checksum verification. The installer was run with network
  access; no tool was installed in the user's home.
- `golangci-lint config verify --config /tmp/newproject-go-real/module/.golangci.yml`
  passed. In the temporary Go module, `format` on deliberately unformatted
  source returned 2 and printed the diff; `cmp` confirmed the file unchanged.
  `reformat` changed the source; `check` subsequently passed with `0 issues.`
  and `go test ./...` successful. Cache locations were set to temporary paths
  via `GOLANGCI_LINT_CACHE` and `GOCACHE`.
- The first attempt used the repository's raw master installer URL and failed
  checksum verification: its unanchored checksum lookup matched both the
  archive and the release's `.sbom.json`. The official documented endpoint
  `https://golangci-lint.run/install.sh` uses a suffix-anchored lookup and
  succeeded without disabling verification. The real formatter also returned
  nonzero for a dirty diff, prompting the implementation to print the captured
  diff before propagating its status. A fixture initially failed revive's
  default `package-comments` rule; adding the package comment made it pass.

The real end-to-end run covers this host architecture; other supported platforms
are represented by the upstream installer and mock tests, not separately run.
