# Decisions

What was chosen, what was rejected, and why, for the program
repository itself. Each repository in the program keeps its own
record; this one governs the umbrella.

## D-001: The program is named control-plane

The name states the subject: the human is the control plane, directing
the workloads without doing the work packet by packet, through
architecture, standards, and gates. The rejected candidates and their
reasons: names built on the evidence the method produces (paper-trail,
receipts, show-your-work) described the symptoms rather than the
system; governor and the-score carried the control idea but needed
explaining; plane-control inverted a term of art and would read as
unfamiliarity to exactly the audience that knows the term. Taking the
canonical term straight and letting the twist live in the tagline won.

## D-002: Identity is scoped to what it works on

The signing key and the installed-app identity that serve the
application repository serve only it. This repository and future
program repositories get their own: a control-plane signing key and a
control-plane agent app, created under the same recorded pattern as
every identity here, need, request, approval. One boundary stated
plainly: this repository's first commit predates this decision and is
signed by the application repository's key; it stays as it is, because
rewriting published history to repair a label would destroy the record
the signatures exist to protect.
