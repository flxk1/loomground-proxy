<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-proxy

**Does this measurement still stand for what it claims?**

Tests whether a proxy measurement still represents its declared target.

## Install

```
pip install loomground-proxy
```

## Usage

```python
from loomground_proxy import Movement, Proxy, check_proxies
subs = check_proxies([Proxy("response_time", "client_was_served", ref="policy#3")],
                     {"response_time": Movement.IMPROVED, "client_was_served": Movement.WORSENED})
subs[0].kind
```

## Interface

- inputs: `Proxy(metric, stands_for, ref)` · readings `{subject: Movement}`: `IMPROVED` · `UNCHANGED` · `WORSENED` · `UNMEASURED`
- output: `Substitution(kind, metric, stands_for, why)`; `KINDS`: `gamed` · `misleading` · `unchecked` · `tracking`
- `chain(metric, proxies)` · `fold_substitutions(substitutions) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `issue_aggregation.aggregate_issues`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-proxy`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 26 tests · Python >=3.10 · solver 0.5

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
