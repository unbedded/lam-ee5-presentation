Finish GitFlow branch workflow: $ARGUMENTS

Required arguments:
- `<branch_type>` - Branch type: `feature`, `release`, `hotfix`, `bugfix`
- `<branch_name>` - Name of the branch to finish

Options:
- `--keep-branch` - Keep the branch after merging (don't delete) - **DEFAULT for this project**
- `--no-ff` - Force no fast-forward merge
- `--delete-branch` - Delete branch after merging (override default keep behavior)

Examples:
- `/gitflow-finish feature user-authentication` - Finish and KEEP feature branch (for evaluation)
- `/gitflow-finish release 1.2.0` - Finish release, merge to main and develop, KEEP branch
- `/gitflow-finish hotfix critical-fix --delete-branch` - Finish and DELETE branch

**Project Policy: KEEP ALL BRANCHES by default**
- Assignment evaluation requires visible development progression
- Remote branches show workflow and version control maturity
- Delete only local branches for cleanup (remote branches preserved)

Merge behavior:
- `feature/*` - Merges to `develop`, **keeps remote branch** (deletes local only)
- `release/*` - Merges to both `main` and `develop`, creates version tag, **keeps remote branch**
- `hotfix/*` - Merges to both `main` and `develop`, creates version tag, **keeps remote branch**
- `bugfix/*` - Merges to `develop`, **keeps remote branch**

For releases/hotfixes: Automatically creates git tag using VERSION file content.
Implementation: Manual git merge --no-ff (preserves branch history for evaluation)