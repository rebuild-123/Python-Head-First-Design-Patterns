# Implementation rules

## Source of truth
The approved `.codex/codex-plan.md` state is the source of truth.
If `.codex/codex-review.md` exists, treat its blocking findings as mandatory.

## Execution
- Follow plan milestones in order.
- Do not expand scope.
- Stop and report if the trusted plan is contradicted by repository reality.

## Validation
- Keep `tests/` importable and ensure at least one `test*.py` exists.
- Run `PYTHONPATH=. python -m unittest discover -s tests -p 'test*.py' -t .`.
- Fix validation failures before continuing.
