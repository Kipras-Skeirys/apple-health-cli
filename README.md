<div align="center">

# Apple Health CLI

A command-line tool for editing Apple Health exports.<br>
Keep only the data and date ranges you need, and remove personal information.

![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=flat-square)
![Stage 2](https://img.shields.io/badge/stage%202-1%2F18-yellow?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)

</div>

---

## How it works

The workflow is inspired by Git. You mount the export, select the data you want, review what you've staged, and export the new file.

```mermaid
flowchart LR
    mount([mount]) --> add([add]) -.-> review([status · remove]) -.-> export([export])

    classDef core fill:#0969da,stroke:#0969da,color:#ffffff
    classDef optional fill:transparent,stroke:#8c959f,stroke-dasharray:4 3,color:#8c959f
    class mount,add,export core
    class review optional
```

Here, **staging data** means saving it as part of your export selection. For example, you could stage steps and heart-rate readings while removing everything else. The CLI remembers these choices between commands and writes the matching records when you run `export`.

### Commands

| Command  | Options     | Description                                                                                                                                                   |
| :------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `mount`  |             | Currently accepts only a valid Apple Health XML file. Planned to accept a `.zip`, a directory, or a file, as long as it contains a valid Apple Health export. |
| `add`    | `-a, --all` | Stage one or more data types. You can also select all data types.                                                                                             |
| `status` |             | Review staged data types, and see which data types are still available.                                                                                       |
| `remove` | `-a, --all` | Remove all or selected data types from staging.                                                                                                               |
| `export` |             | Write the selected records to a new XML file.                                                                                                                 |

---

## How to use

> **Note:** The project is currently at Stage 2 of development, so some commands may not work as expected. See the [roadmap](#roadmap) for current project status.

Requires Python 3.10 or newer. No other dependencies.

```bash
git clone https://github.com/kipras-skeirys/apple-health-cli.git
cd apple-health-cli
```

Try it with one of the [sample data](sample_data/) provided, or your own `export.xml`:

```bash
python3 main.py mount sample_data/small_export.xml   # load the export
python3 main.py status                               # see available data types
python3 main.py add StepCount HeartRate              # stage data types
python3 main.py remove HeartRate                     # unstage one
python3 main.py export                               # write the filtered XML
```

---

## Roadmap

```text
●  finished stage   ◐  current stage   ○  planned stage   [x] done   [ ] to do

●  STAGE 0 · Groundwork ····································· DONE
┃  ████████████████████  3/3
┃
┣━━ [x] Learn about XML data
┣━━ [x] Figure out the Apple Health export.xml data structure and
┃       schema using the Linux CLI
┣━━ [x] Set up the project repo with a README
┃
●  STAGE 1 · Basic functionality (MVP) ······················ DONE
┃  ████████████████████  13/13
┃
┣━━ [x] mount command
┃   ┣━━ [x] Accept file with valid Apple Health data
┃   ┣━━ [x] Count each data type
┃   ┗━━ [x] Show readable data type names
┣━━ [x] Save state between commands
┣━━ [x] status command
┣━━ [x] add command (one, many, or all data types)
┣━━ [x] remove command (one, many, or all data types)
┣━━ [x] export command
┃   ┣━━ [x] Write staged records to a new XML file, schema intact
┃   ┗━━ [x] Use the current directory or a custom path
┣━━ [x] Handle common errors
┣━━ [x] Usage docs and a sample export.xml
┃
◐  STAGE 2 · Core workflow and tests ················· IN PROGRESS
│  █░░░░░░░░░░░░░░░░░░░  1/18
│
├── [ ] Estimate size
│   ├── [x] Estimated size per data type
│   └── [ ] Show size change against estimated export size (old -> new)
├── [ ] Fix missing line breaks between exported elements
├── [ ] Date ranges (start and end)
├── [ ] edit command
├── [ ] Remove personal information (new command or option)
│   ├── [ ] Strip the <Me> element
│   └── [ ] Anonymize device and source names
├── [ ] Support all top-level elements, not only <Records>
├── [ ] Handle nested duplicate records
├── [ ] Tests
│   ├── [ ] Set up unittest and a tests folder
│   ├── [ ] Unit tests for pure functions
│   ├── [ ] Tests for error cases
│   ├── [ ] Isolate the state file in tests
│   ├── [ ] End-to-end CLI tests
│   └── [ ] Regression tests for fixed bugs
│
○  STAGE 3 · Data aggregation ···························· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/7
┆
┆╌╌ [ ] Daily, weekly, monthly, and yearly aggregates
┆   ┆╌╌ [ ] Choose a calculation per metric
┆   ┆╌╌ [ ] Handle overlapping data sources
┆╌╌ [ ] Edit sources(phone, watch, third-party app, etc.) per data type
┆╌╌ [ ] Data categories
┆╌╌ [ ] Compare results with Apple Health
┆╌╌ [ ] Measure time and peak memory
┆
○  STAGE 4 · Input and export formats ···················· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/17
┆
┆╌╌ [ ] Accept a .zip or directory
┆   ┆╌╌ [ ] Limit directory search depth
┆   ┆╌╌ [ ] Resist decompression bombs
┆╌╌ [ ] Harden XML parsing
┆   ┆╌╌ [ ] Billion laughs (entity expansion)
┆   ┆╌╌ [ ] Quadratic blowup
┆   ┆╌╌ [ ] External entities (XXE)
┆   ┆╌╌ [ ] External DTD retrieval
┆╌╌ [ ] Export formats
┆   ┆╌╌ [ ] JSON
┆   ┆╌╌ [ ] JSON Lines
┆   ┆╌╌ [ ] CSV
┆   ┆╌╌ [ ] SQLite database
┆   ┆╌╌ [ ] Plain text report
┆   ┆╌╌ [ ] Gzip compression
┆╌╌ [ ] Safe file writing
┆╌╌ [ ] Export to stdout (export -)
┆
○  STAGE 5 · Usability and packaging ····················· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/9
┆
┆╌╌ [ ] ignore command (unstage and lock data types or categories)
┆╌╌ [ ] hide command (hide data types or categories from status)
┆╌╌ [ ] Reusable selection presets
┆╌╌ [ ] Notify about unknown or already staged data types
┆╌╌ [ ] Confirm before overwriting an export
┆╌╌ [ ] Detect a changed (SHA-256 fingerprint) or moved source
┆╌╌ [ ] Stylized CLI output
┆╌╌ [ ] Per-platform app data folder
┆╌╌ [ ] Installable package
```
