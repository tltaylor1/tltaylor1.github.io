# control-plane

A security engineering program, built in public, by one person and a
governed coding agent. The name is the thesis: the human is the
control plane, directing the workloads without doing the work packet
by packet, through architecture, standards, and gates the agent
cannot route around. Every claim carries its record: decisions with
their rejected alternatives, controls with their proving tests,
releases with their provenance attestations, the agent's failures
with what caught them, and the human's own account posture attested
rather than assumed.

The rendered site is this repository, served at
https://tltaylor1.github.io once public.

## The parts

| Repository | What it is, and what it proves |
|---|---|
| [role-call](https://github.com/tltaylor1/role-call) | A governance tool for non-human identities: import cloud identity snapshots, derive state from history, put owners and review campaigns on the record. The program's flagship: building in motion, with the decision record growing under load |
| [secure-expense-mvp](https://github.com/tltaylor1/secure-expense-mvp) | A small expense tool, finished and hardened: every request-path gate tied to the failure it prevents, mutation-tested, complete on purpose |
| [build-guidelines](https://github.com/tltaylor1/build-guidelines) | The doctrine: standards where every rule records the incident that produced it, the enforcement mapping, and the promotion path from human check to automated gate |
| [sample-diagrams](https://github.com/tltaylor1/sample-diagrams) | Hand-drawn systems diagrams under an editorial doctrine: a complexity budget, one accent, done when nothing can be removed |
| aws-platform | Arrives with Phase 3: generic Terraform modules for an organization, its baseline, account vending, and keyless deploy federation |

## The program documents

The concerns that span repositories live here, not buried in any one
of them:

- [PHASE-3.md](PHASE-3.md), the current phase's public plan, fixed
  before the work.
- [MONITORING.md](MONITORING.md), what is watched at each layer, its
  signal, and who hears it, with unfilled layers stating themselves.
- [BCDR.md](BCDR.md), recovery split between rebuildable-from-code and
  actual state, with drills that carry their last-run date and expire.
- [PIPELINES.md](PIPELINES.md), how every repository is gated, and the
  infrastructure-as-code posture.

## The method, in five lines

Design before code, with the plan fixed and published before building
starts. Every change through a pull request: the agent proposes under
its own installed-app identity, required checks gate, a human
approving review is required, and the merge is the review's receipt.
Every figure a document states is asserted against the running system
or gated against its source. Every incident becomes a rule, and the
second identical hand-fix becomes automation. What is deliberately
absent is recorded next to what exists, because an undocumented gap
and a considered exclusion look identical from outside.

## The arc

Eight phases: design; the application; local Kubernetes; the cloud
enclave as code; managed Kubernetes; the security-gated pipeline;
runtime detection; human-triggered remediation last, because write
access to anyone's cloud account is trust that must be earned by
everything before it. Phases one and two are complete and tagged
(v0.2.0, with verifiable build provenance); Phase 3 is in progress.
