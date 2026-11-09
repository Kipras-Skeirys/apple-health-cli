<div align="center">

# Apple Health CLI

A command-line tool for editing Apple Health exports.<br>
Keep only the data and date ranges you need, and remove personal information.

![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=flat-square)
![Stage 1](https://img.shields.io/badge/stage%201-2%2F13-yellow?style=flat-square)
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

> **Note:** Stage 1 is still in progress, so not all commands work yet. See the [roadmap](#roadmap) for current progress.

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
◐  STAGE 1 · Basic functionality (MVP) ··············· IN PROGRESS
│  ███░░░░░░░░░░░░░░░░░  2/13
│
├── [ ] mount command
│   ├── [x] Accept file with valid Apple Health data
│   ├── [ ] Count each data type
│   └── [ ] Show readable data type names
├── [ ] Save state between commands
├── [ ] status command
├── [ ] add command (one, many, or all data types)
├── [ ] remove command (one, many, or all data types)
├── [ ] export command
│   ├── [ ] Write staged records to a new XML file, schema intact
│   └── [ ] Use the current directory or a custom path
├── [ ] Handle common errors
├── [x] Usage docs and a sample export.xml
│
○  STAGE 2 · Full workflow, formats, and privacy ········· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/16
┆
┆╌╌ [ ] Estimated size per data type
┆╌╌ [ ] Accept a .zip or directory
┆╌╌ [ ] Date ranges (start and end)
┆╌╌ [ ] edit command
┆╌╌ [ ] Workouts and activity summaries
┆╌╌ [ ] Detect a changed or moved source
┆╌╌ [ ] Tests
┆╌╌ [ ] Export formats
┆   ┆╌╌ [ ] JSON
┆   ┆╌╌ [ ] CSV
┆   ┆╌╌ [ ] Relational database
┆   ┆╌╌ [ ] Document database
┆╌╌ [ ] Edit sources per data type
┆╌╌ [ ] Remove personal information
┆   ┆╌╌ [ ] Strip the <Me> element
┆   ┆╌╌ [ ] Anonymize device and source names
┆
○  STAGE 3 · Advanced data aggregation ··················· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/5
┆
┆╌╌ [ ] Daily, weekly, monthly, and yearly aggregates
┆   ┆╌╌ [ ] Choose a calculation per metric
┆   ┆╌╌ [ ] Handle overlapping data sources
┆╌╌ [ ] Compare results with Apple Health
┆╌╌ [ ] Measure time and peak memory
┆
○  STAGE 4 · Final touches ······························· PLANNED
┆  ░░░░░░░░░░░░░░░░░░░░  0/5
┆
┆╌╌ [ ] Reusable selection presets
┆╌╌ [ ] Installable package
┆╌╌ [ ] Per-platform app data folder
┆╌╌ [ ] Confirm before overwriting an export
┆╌╌ [ ] Stylized CLI output
```
