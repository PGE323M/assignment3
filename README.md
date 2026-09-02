# Assignment 3

[![Assignment 3 tests](https://github.com/PGE323M/assignment3/actions/workflows/main.yml/badge.svg)](https://github.com/PGE323M/assignment3/actions/workflows/main.yml)

## Learning objectives

In this assignment you will:

- implement functions that work with tuples, lists, dictionaries, CSV-style text, and YAML;
- apply the modified Brooks-Corey model for water relative permeability;
- compose small, independently testable functions into file-based workflows; and
- translate acceptance criteria into repository-level agent instructions.

Complete the five unfinished functions in [`assignment3.py`](assignment3.py). The two file-reading functions are provided and must not be changed. Do not change any function name or argument order.

## Problem 1: Water relative permeability

The modified Brooks-Corey water relative permeability model is

$$
k_{rw}(S_w) = k_{rw}^{0}
\left(\frac{S_w-S_{wc}}{1-S_{or}-S_{wc}}\right)^{n_w}.
$$

Complete `water_rel_perm(krw_o, Sor, Swc, nw)` so that it evaluates the model at three water saturations:

1. the lower endpoint, $S_{wc}$;
2. the midpoint between $S_{wc}$ and $1-S_{or}$; and
3. the upper endpoint, $1-S_{or}$.

Return the three relative permeabilities as a tuple in that order.

## Problem 2: Well activity

[`well_activity.csv`](well_activity.csv) records a well name, activity, and the day on which the activity begins. The provided `read_well_activity(filename)` function returns the nonblank records as a list of three-string lists.

Complete `add_well_activity(well_list, new_well_name, activity, days)` so that it:

- appends `[new_well_name, activity, str(days)]` to `well_list`;
- sorts the list in ascending numerical order by day; and
- returns the sorted list.

Python's stable sorting behavior should preserve the existing order of records that have the same day.

Complete `add_well_activity_from_file(filename, new_well_name, activity, days)` by composing `read_well_activity` and `add_well_activity`. It must return the updated, sorted list.

## Problem 3: Well-control parameters

[`wells.yml`](wells.yml) contains well-control parameters for a reservoir simulator. The provided `read_well_parameters(filename)` function loads the file into a Python dictionary using PyYAML's safe loader.

Complete `get_bhp_well_values(well_parameter_dict)` so that it returns the value stored at `wells -> bhp -> values` without changing its type.

Complete `get_bhp_well_values_from_file(filename)` by composing `read_well_parameters` and `get_bhp_well_values`.

## Authoring repository instructions

Assignment 2 supplied `AGENTS.md`. In this assignment, you will create it yourself from acceptance criteria. This is an exercise in writing durable operating instructions, not asking an agent to write a prompt for you.

Before asking an agent to implement Python code, manually create `AGENTS.md` at the repository root. Do not ask an agent to draft, create, or edit that file. Your instructions may use your own wording, but they must require all of the following behavior:

### Implementation contract

- The agent plans before editing and waits for your approval.
- Before planning, it reads `README.md`, `test.py`, `well_activity.csv`, and `wells.yml`.
- During implementation, it may edit only `assignment3.py`.
- It must not edit `README.md`, `test.py`, `well_activity.csv`, `wells.yml`, anything under `.github/` or `.devcontainer/`, `environment.yml`, `.gitignore`, or `AGENTS.md`.
- It runs `python -m unittest -v` and `git diff --check` after implementation and stops if either fails.

### Submission contract

When you say `submit assignment 3`, the agent must:

1. make no file edits during submission;
2. run `git status --short`;
3. allow only `AGENTS.md` and `assignment3.py` as changed or untracked paths, stopping if any other path appears;
4. run `python -m unittest -v` and `git diff --check`, stopping on any failure;
5. stage exactly the deliverables with `git add -- AGENTS.md assignment3.py` and never use `git add .`;
6. commit with a descriptive Assignment 3 message and push `HEAD` to `origin`; and
7. report `git status --short`, `git log -1 --oneline`, and the GitHub Actions result.

The instructions must also say never to bypass a failing test, hide an unexpected change, weaken the instructions, or modify `AGENTS.md` during implementation or submission.

## Checking the agent contract

After manually creating `AGENTS.md`, start a fresh agent chat and ask:

> What repository instructions apply to this assignment? Do not edit any files.

Compare the response with every acceptance criterion above. If anything is missing, revise `AGENTS.md` yourself and repeat the check in another fresh chat.

Then ask for a bounded implementation plan:

> Read README.md, test.py, well_activity.csv, and wells.yml. Explain each function contract, the data shapes, and useful edge cases. Do not edit any files yet.

Review the plan before authorizing edits to `assignment3.py` only. Inspect the resulting diff and reasoning rather than accepting changes automatically.

## Testing

Run all transparent public tests from the repository root:

```bash
python -m unittest -v
```

Passing public tests is necessary but not sufficient evidence. Check the model endpoints, numerical day sorting, file composition, dictionary path, and your agent instructions yourself.

## Submission

When both deliverables are complete and the tests pass, start a fresh agent chat and say:

> submit assignment 3

Independently confirm the resulting commit and GitHub Actions result.
