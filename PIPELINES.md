# Pipelines and infrastructure as code, the program view

Every repository in the program is gated the same way in spirit and
per its layer in substance: nothing lands without passing checks,
every tool arrives from its canonical release and is checksum-verified
before it runs, and what a gate may block on is decided and recorded,
because an alarm that is always red teaches the eye to skip it.

## The shared method

- Changes travel branches and pull requests; the mainline refuses
  direct pushes, force pushes, and deletion.
- The coding agent proposes under its own installed-app identity with
  named permissions; a human approving review is required, and the
  approve button lives past the diff, so the diff gets read.
- Commits and release tags are signed; releases carry build
  provenance attestations verifiable against the platform's
  transparency log.
- Writing rules, status-truth gates, and secret scans run at commit
  time and again in the pipeline.
- Weekly scheduled runs cover what changes while the code does not: a
  base image fix shipping, a new advisory against a pinned tree.

## Per repository

| Repository | The gates, beyond the shared set |
|---|---|
| The application | Tests with a coverage floor, strict typing, a mutation check that breaks one control at a time and requires the tests to notice, migration drift against a real database, dependency audits, container lint, base image scan, manifest schema and posture checks, and a documented route surface asserted against the live route table |
| The guidelines | The writing rules enforced on the documents that define the writing rules |
| The platform (arrives at Phase 3) | Format and validation, IaC misconfiguration scanning with the already-vetted scanner's config mode, a cost delta stated on every pull request, drift detection on the weekly clock, and the cloud's own reviewers (Config, Security Hub, Access Analyzer) checking what actually exists independently of what any plan claimed |

## Infrastructure as code, the posture

Terraform as the primary tool, state in versioned S3 with native
locking, no account identifiers in shipped modules (identity is
discovered from credentials; environment specifics live in a thin live
layer), and no stored cloud credential anywhere: humans authenticate
through short-lived Identity Center sessions, pipelines federate
through OIDC into scoped roles. A plan is a claim about intent, so the
cloud's own configuration record is the independent reviewer of what
exists, the same relationship the application's tests have to its
controls.
