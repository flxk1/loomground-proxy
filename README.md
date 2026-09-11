<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-proxy

**Does this measurement still stand for what it claims?**

Tests whether a proxy measurement still represents its declared target.

## Problem

A metric keeps moving after it stopped meaning anything. Tests whether the proxy still stands for its target.

## Install

```
pip install loomground-proxy
```

## Usage

```python
from loomground_proxy import Movement, Proxy, check_proxies
subs = check_proxies([Proxy("tickets_closed", "customer_problems_solved", ref="okr#2")],
                     {"tickets_closed": Movement.IMPROVED, "customer_problems_solved": Movement.WORSENED})
subs[0]
```

## Example

```
in : tickets_closed IMPROVED while customer_problems_solved WORSENED
out: Substitution(kind='gamed', metric='tickets_closed', stands_for='customer_problems_solved', why='tickets_closed improved while customer_problems_solved, which it is declared to stand for, got worse (okr#2)')
```

## Interface

- inputs: `Proxy(metric, stands_for, ref)` · readings `{subject: Movement}`: `IMPROVED` · `UNCHANGED` · `WORSENED` · `UNMEASURED`
- output: `Substitution(kind, metric, stands_for, why)`; `KINDS`: `gamed` · `misleading` · `unchecked` · `tracking`
- `chain(metric, proxies)` · `fold_substitutions(substitutions) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `issue_aggregation.aggregate_issues`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5–0.6; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-proxy`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 26 tests · Python >=3.10 · solver 0.5–0.6

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
