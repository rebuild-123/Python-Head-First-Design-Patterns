## Goal
Improve reliability in a tightly scoped area by adding meaningful type annotations, introducing minimal `unittest` coverage, and fixing one reproduced runtime bug in the vacation builder module.

## Problem Statement
The repository currently has no stable project-level test entrypoint (`tests/` + discovery command), and `builder/vacation` contains both typing inconsistencies and at least one real runtime bug:
- Reproduced on April 11, 2026 (UTC): `OutdoorsVacationBuilder.addAccommodation_1()` raises `NameError: name 'Tentl' is not defined`.

## Affected Files
Planned code/test scope (only):
1. `builder/vacation/OutdoorsVacationBuilder.py`
2. `builder/vacation/CityVacationBuilder.py`
3. `builder/vacation/VacationBuilder.py`
4. `builder/vacation/Vacation.py`
5. `builder/vacation/Accommodation.py`
6. `tests/test_vacation_builders.py` (new)
7. `tests/__init__.py` (new, minimal)

## Chosen Approach
1. Fix only reproduced bug(s) in `builder/vacation`, starting with `Tentl` typo.
2. Add targeted type annotations in the same module group only (no broad refactor), aligning declared types with actual runtime usage.
3. Add minimal `unittest` tests covering:
   - bug reproduction path (now expected to pass),
   - key builder behavior touched by type/bug edits.
4. Add a stable test entrypoint via standard unittest discovery under `tests/`.

## Milestones
1. Baseline verification
   - Re-run minimal reproduction for `addAccommodation_1()` failure (documented).
2. Implement targeted fixes
   - Correct typo bug.
   - Apply annotation updates in listed files only.
3. Add tests
   - Create `tests/` layout and focused test module for modified behavior.
4. Validate
   - Run smallest relevant tests first (new test module), then full `tests/` discovery.
5. Scope check
   - Confirm final diff contains only approved files and no unrelated refactors.

## Validation Steps
1. `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_vacation_builders`
2. `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_*.py'`
3. If any failure occurs: report exact failing test and traceback, then stop/adjust within scope.

## Risks
1. Local-import style in this repo (non-package relative imports) may require careful `sys.path` handling in tests.
2. Tightening annotations may expose latent inconsistencies; risk is mitigated by limiting changes to `builder/vacation`.
3. Behavior-preservation risk if type cleanup accidentally changes formatting/output; tests will lock expected behavior.

## Rollback Strategy
1. Revert only the specific changed files listed above if regressions appear.
2. Keep bug fix and tests atomic in commit(s) so rollback can be selective (tests only vs code+tests).

## Out-of-Scope Items
1. Refactoring other pattern examples outside `builder/vacation`.
2. Introducing third-party test/type tooling dependencies.
3. Repository-wide typing modernization.
4. Bug fixes not evidenced by reproduction or directly touched tests/files.
