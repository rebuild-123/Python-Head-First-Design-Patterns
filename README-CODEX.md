# Codex Workflow Usage

This repository is wired to run Codex workflows from issue comments. The entrypoint workflow is:
`.github/workflows/codex-issue.yml`

## One-time setup
1. Add `OPENAI_API_KEY` in `Settings > Secrets and variables > Actions`.
2. Ensure Actions are enabled for the repo.
3. If you want review runs to open a draft PR, enable:
   `Settings > Actions > General > Allow GitHub Actions to create and approve pull requests`.

## Branch requirements
The branch must already exist on the remote and start with one of:
- `codex/`
- `feature/`
- `bugfix/`
- `hotfix/`

## Commands
Run these commands as a comment on an issue (not on a PR):

```text
/codex plan branch=codex/example
/codex implement branch=codex/example
/codex review branch=codex/example
/codex autopilot branch=codex/example max_rounds=3
```

Only `OWNER`, `MEMBER`, or `COLLABORATOR` comments trigger the workflow.

## Expected flow
1. `/codex plan ...` creates a trusted plan comment.
2. `/codex implement ...` uses the trusted plan and writes changes.
3. `/codex review ...` reviews the implementation and may open a draft PR when passing.

`/codex autopilot ...` runs `plan -> implement -> review`, and repeats up to `max_rounds` only when the latest review is blocked.

## Validation
Implementation runs require a unittest entrypoint:
`PYTHONPATH=. python -m unittest discover -s tests -p 'test*.py' -t .`

## Troubleshooting
- `Branch does not exist`: push the target branch first.
- `No trusted latest plan was found`: run the plan command for the same issue and branch.
- Review passes but no PR: confirm the repo allows Actions to create PRs and that the branch has a diff vs base.
