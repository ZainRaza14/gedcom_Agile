# GEDCOM Agile — A Genealogy File Parser & Validation Engine

[![Build Status](https://travis-ci.org/ZainRaza14/gedcom_Agile.svg?branch=master)](https://travis-ci.org/ZainRaza14/gedcom_Agile)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-unittest-green.svg)](#-testing)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](#-license)

> A Python engine that parses **GEDCOM** genealogy files, models individuals and families as first-class objects, renders human-readable summary tables, and runs a suite of **30+ data-integrity validations** — built incrementally across four agile sprints (SSW-555, *Agile Methods for Software Development*).

---

## 📖 Table of Contents

- [What is this?](#-what-is-this)
- [Why it exists](#-why-it-exists)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Validation Rules (User Stories)](#-validation-rules-user-stories)
- [Testing](#-testing)
- [Continuous Integration](#-continuous-integration)
- [Development Workflow](#-development-workflow)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧬 What is this?

**GEDCOM** (GEnealogical Data COMmunication) is the de-facto standard text format for
exchanging family-tree data between genealogy programs. A `.ged` file is a flat,
line-oriented, level-numbered record set describing **individuals** (`INDI`) and the
**families** (`FAM`) that link them together.

This project reads a GEDCOM file and:

1. **Parses** each line into structured `Individual` and `Family` objects.
2. **Derives** computed attributes such as age and living/deceased status.
3. **Presents** the data as clean, aligned ASCII tables.
4. **Validates** the tree against a catalog of genealogical sanity checks — flagging
   impossible dates, illegal marriages, duplicate records, and more.

Every anomaly is reported as a structured, greppable error string, e.g.:

```
ERROR: INDIVIDUAL: US01: I01: Birthday 2020-07-15 is after todays date
ERROR: FAMILY: US19: The two first cousins @I12@ and @I15@ cannot be married together
```

---

## 💡 Why it exists

Genealogical data is notoriously error-prone: hand-entered dates, merged trees, and
decades of copy-paste introduce contradictions (a child born before their parents, a
divorce recorded after a death, duplicate IDs, and so on). This engine acts as a
**linter for family trees**, surfacing those inconsistencies automatically so they can
be corrected before the data is trusted.

The codebase was developed **sprint-by-sprint** as a teaching exercise in agile software
engineering — each sprint adds a batch of user stories, each user story ships with its
own targeted GEDCOM fixture and unit test.

---

## ✨ Features

- **Streaming GEDCOM parser** — reads level `0/1/2` records for `INDI`, `FAM`, `NAME`,
  `SEX`, `BIRT`, `DEAT`, `MARR`, `DIV`, `HUSB`, `WIFE`, `CHIL`, `FAMC`, `FAMS`.
- **Object model** — `indClass` and `famClass` encapsulate individuals and families with
  getters/setters and a `details()` view used for tabular output.
- **Date normalization** — GEDCOM dates (`15 JUL 1990`) are converted to ISO `YYYY-MM-DD`.
- **Derived fields** — automatic **age** computation and **alive/deceased** flags.
- **Pretty tabular reports** — individual and family summaries rendered with
  [`PrettyTable`](https://pypi.org/project/prettytable/).
- **30+ validation rules** — organized as independent "user story" functions returning
  lists of error strings (see [full catalog](#-validation-rules-user-stories)).
- **Per-story fixtures & tests** — every rule has a dedicated `.ged` test file and a
  `unittest` case with expected error output.
- **Sprint runners** — one entry point per sprint that parses a master file, runs all
  that sprint's checks, and writes a combined report to `sprintNoutput.txt`.

---

## 🏗 Architecture

```
                ┌──────────────────┐
   .ged file ──▶│  ParserModule.py │  parse_main()
                └────────┬─────────┘
                         │ builds
              ┌──────────▼───────────┐
              │  OrderedDict of      │      indClass  (individuals)
              │  Individuals & Families ────┤
              │  + errorList (dup IDs)│      famClass  (families)
              └──────────┬───────────┘
                         │
        ┌────────────────┼─────────────────────┐
        │                │                      │
 ┌──────▼──────┐  ┌──────▼───────┐      ┌───────▼────────┐
 │ print_main  │  │ userstories/ │      │    utils.py    │
 │ PrettyTable │  │ usNN_* checks│◀─────│ date helpers   │
 │  reports    │  │ → error list │      │ age / diffs    │
 └─────────────┘  └──────┬───────┘      └────────────────┘
                         │
                  ┌──────▼───────┐
                  │  us_test/    │  unittest cases per story
                  │  sprintN_*   │
                  └──────────────┘
```

**Data flow:** `parse_main(file)` returns `(indDict, famDict, errorList)`. The print
layer turns those dicts into tables; each user-story function re-parses (or consumes) the
dicts and returns a list of human-readable error strings; the sprint runners aggregate
everything and persist a report.

---

## 📂 Project Structure

```
gedcom_Agile/
├── ParserModule.py          # Core GEDCOM parser → Individual/Family dicts + derived fields
├── indClass.py              # Individual object model (name, sex, birth, death, age, alive…)
├── famClass.py              # Family object model (husband, wife, children, marriage, divorce)
├── print_main.py            # PrettyTable rendering of individuals & families
├── utils.py                 # Date utilities (ISO compare, age, day/month diffs, name parsing)
│
├── sprint_1.py … sprint_4.py        # Per-sprint runners (parse + run all checks + write report)
├── sprint1_alltests.py … sprint4_alltests.py   # Per-sprint unittest aggregators
├── sprintNoutput.txt        # Generated tabular + anomaly reports
│
├── userstories/             # Validation rules, one module per user story
│   ├── sprint01_us/userStory01.py … userStory08.py
│   ├── sprint02_us/userStory09.py … userStory16.py
│   ├── sprint03_us/userStory17.py … userStory24.py
│   └── sprint04_us/userStory27.py … userStory36.py
│
├── us_test/                 # Unit tests mirroring the user stories
│   ├── sprint01_tests/test01.py … test08.py
│   ├── sprint02_tests/…  sprint03_tests/…  sprint04_tests/…
│
├── gedfilestest/            # GEDCOM fixtures
│   ├── sprintNN-testdata.ged           # Master files per sprint
│   └── sprintNN_ged/usNNtestdata.ged   # One focused fixture per user story
│
└── .travis.yml              # CI: install deps + run all four sprint test suites
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+**
- Dependencies:
  - [`PrettyTable`](https://pypi.org/project/prettytable/) — tabular output
  - [`python-dateutil`](https://pypi.org/project/python-dateutil/) — relative date math

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ZainRaza14/gedcom_Agile.git
cd gedcom_Agile

# 2. (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install PrettyTable python-dateutil
```

---

## 🖥 Usage

### Print the family & individual tables

```bash
python print_main.py
```

Renders the individual and family summary tables for the default fixture
(`gedfilestest/sprint01-testdata_1.ged`). Example output:

```
Individuals Information----------------------->

+-----+----------------+--------+------------+-----+-------+------------+-------+--------+
| ID  |      Name      | Gender |  Birthday  | Age | Alive |   Death    | Child | Spouse |
+-----+----------------+--------+------------+-----+-------+------------+-------+--------+
| I01 |  John /Smith/  |   M    | 1980-05-12 |  45 |  True |     NA     |   NA  |  F23   |
| ... |      ...       |  ...   |    ...     | ... |  ...  |    ...     |  ...  |  ...   |
+-----+----------------+--------+------------+-----+-------+------------+-------+--------+
```

### Run a full sprint (tables + all validations + report file)

```bash
python sprint_4.py    # parses sprint04 master file, runs US01–US36, writes sprint4output.txt
```

Each `sprint_N.py` prints the tables and every detected anomaly to the console **and**
writes a combined report to `sprintNoutput.txt`.

### Use the parser programmatically

```python
from ParserModule import parse_main
from userstories.sprint01_us.userStory01 import us01_dates_b4_curr_date

indDict, famDict, dupIds = parse_main("gedfilestest/sprint01-testdata.ged")

# Inspect an individual
john = indDict["@I01@"]
print(john.nameGet(), john.ageGet(), john.aliveGet())

# Run a single validation
for err in us01_dates_b4_curr_date("gedfilestest/sprint01-testdata.ged"):
    print(err)
```

---

## ✅ Validation Rules (User Stories)

Each rule is an independent function that returns a list of error strings. Anomalies are
tagged `ERROR: <SCOPE>: USNN: …` so they can be filtered by ID or rule.

### Sprint 1 — Dates & basic ordering

| ID | Rule | Description |
|----|------|-------------|
| **US01** | Dates before current date | Birth, death, marriage, and divorce dates must not be in the future. |
| **US02** | Birth before marriage | An individual's birth date must precede their marriage date. |
| **US03** | Birth before death | Birth date must precede death date. |
| **US04** | Marriage before divorce | Marriage must occur before divorce. |
| **US05** | Marriage before death | Marriage must occur before either spouse's death. |
| **US06** | Divorce before death | Divorce must occur before either spouse's death. |
| **US07** | Less than 150 years old | No individual is older than 150 years (living or at death). |
| **US08** | Birth before marriage of parents | A child is born after the parents' marriage (and before divorce + 9 months). |

### Sprint 2 — Life-stage & structural limits

| ID | Rule | Description |
|----|------|-------------|
| **US09** | Birth before death of parents | A child is born before the mother's death and within 9 months of the father's death. |
| **US10** | Marriage after 14 | Neither spouse marries before age 14. |
| **US11** | No bigamy | No individual is married to two people at the same time. |
| **US12** | Parents not too old | Mother < 60 years and father < 80 years older than their children. |
| **US13** | Siblings spacing | Siblings are born more than 8 months apart, or less than 2 days (twins). |
| **US14** | Multiple births ≤ 5 | No more than five siblings are born at the same time. |
| **US15** | Fewer than 15 siblings | A family has fewer than 15 children. |
| **US16** | Male last names | All males in a family share the same last name. |

### Sprint 3 — Relationship legality & uniqueness

| ID | Rule | Description |
|----|------|-------------|
| **US17** | No marriages to descendants | Parents must not marry their own descendants. |
| **US18** | Siblings should not marry | Siblings must not marry one another. |
| **US19** | First cousins should not marry | First cousins must not marry one another. |
| **US20** | Aunts and uncles | Aunts/uncles must not marry their nieces/nephews. |
| **US21** | Correct gender for role | Husband is male; wife is female. |
| **US22** | Unique IDs | All individual and family IDs are unique. |
| **US23** | Unique name and birth date | No two individuals share the same name **and** birth date. |
| **US24** | Unique families by spouses | No two families share the same spouse names and marriage date. |

### Sprint 4 — Reporting & list utilities

| ID | Rule | Description |
|----|------|-------------|
| **US27** | Include individual ages | Report the current (or at-death) age of each individual. |
| **US28** | Order siblings by age | List a family's children ordered from oldest to youngest. |
| **US29** | List deceased | List all individuals who have died. |
| **US30** | List living married | List all living, currently married individuals. |
| **US31** | List living single | List all living individuals over 30 who have never married. |
| **US32** | List multiple births | List individuals born as part of a multiple birth. |
| **US35** | List recent births | List individuals born within the last 30 days. |
| **US36** | List recent deaths | List individuals who died within the last 30 days. |

> **Note:** US25–US26 and US33–US34 are intentionally out of scope for this project.

---

## 🧪 Testing

Every user story ships with a dedicated `unittest` case in `us_test/`, backed by a focused
GEDCOM fixture in `gedfilestest/`. Tests assert the **exact** list of expected error
strings for their fixture.

Run all tests for a single sprint:

```bash
python -m unittest sprint1_alltests.py
python -m unittest sprint2_alltests.py
python -m unittest sprint3_alltests.py
python -m unittest sprint4_alltests.py
```

Run one story's test directly:

```bash
python -m unittest us_test.sprint01_tests.test01
```

Discover and run everything:

```bash
python -m unittest discover -s us_test -p "test*.py"
```

> ⚠️ **Time-sensitive checks:** Some rules (US01, US07, US27, US29–US36) compare against
> **today's date**. Fixtures and expected values were authored during the course; a few
> age- or "recent"-based assertions may drift over time. Run tests with this in mind.

---

## 🔄 Continuous Integration

CI is configured via [`.travis.yml`](.travis.yml) and runs on **Python 3.6**:

```yaml
install:
  - pip install PrettyTable
  - pip install python-dateutil
  - sudo apt-get install -y r-base
script:
  - python -m unittest sprint1_alltests.py
  - python -m unittest sprint2_alltests.py
  - python -m unittest sprint3_alltests.py
  - python -m unittest sprint4_alltests.py
```

Every push runs all four sprint test suites, gating regressions across the full rule set.

---

## 🛠 Development Workflow

This project follows an **agile, sprint-based** cadence. Each sprint adds a batch of user
stories following the same repeatable pattern:

1. **Write a fixture** — craft `gedfilestest/sprintNN_ged/usNNtestdata.ged` that
   deliberately contains the anomaly (and valid records as controls).
2. **Implement the rule** — add `userstories/sprintNN_us/userStoryNN.py` exposing a
   `usNN_*(file) -> list[str]` function that returns error strings.
3. **Write the test** — add `us_test/sprintNN_tests/testNN.py` asserting the exact
   expected output for the fixture.
4. **Wire it up** — register the story in `sprint_N.py` (runner) and
   `sprintN_alltests.py` (test aggregator).

### Conventions

- **Error format:** `ERROR: <INDIVIDUAL|FAMILY>: USNN: <id/context>: <message>`
- **Dates:** stored internally as ISO `YYYY-MM-DD`; use helpers in `utils.py` for
  comparisons and diffs rather than re-implementing date math.
- **IDs:** GEDCOM cross-reference pointers (e.g. `@I01@`); `details()` strips `@` for
  display.

---

## 🗺 Roadmap

Potential next steps for anyone extending the project:

- [ ] Implement the remaining GEDCOM user stories (US25, US26, US33, US34).
- [ ] Replace duplicated `dateFormating` helpers (in `ParserModule`, `indClass`,
      `famClass`) with a single shared utility.
- [ ] Parse each file **once** and pass the dicts into checks (rather than re-parsing per
      story) for large-file performance.
- [ ] Package as an installable CLI (`gedcom-lint <file.ged>`) with a `requirements.txt`.
- [ ] Migrate CI from Travis to GitHub Actions and modern Python versions.
- [ ] Make time-sensitive tests deterministic by freezing "today" in fixtures.

---

## 🤝 Contributing

1. Fork the repository and create a feature branch.
2. Follow the [development workflow](#-development-workflow) above — fixture → rule →
   test → wire-up.
3. Ensure all four sprint test suites pass locally.
4. Open a pull request describing the user story or fix.

---

## 📄 License

Released under the **MIT License**. This project was developed for the **SSW-555 Agile
Methods for Software Development** course.

---

<div align="center">
<sub>Built with Python • Parsed with care • Linted like a family tree deserves 🌳</sub>
</div>
