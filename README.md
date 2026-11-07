<div align="center">

# Apple Health CLI

A command-line tool for editing Apple Health exports.<br>
Keep only the data and date ranges you need, and remove personal information.

![Status](https://img.shields.io/badge/status-planning-lightgrey?style=flat-square)
![Stage 1](https://img.shields.io/badge/stage%201-0%2F36-lightgrey?style=flat-square)
![Python](https://img.shields.io/badge/python-3-3776AB?style=flat-square&logo=python&logoColor=white)

</div>

---

## How it works

The workflow is inspired by Git. You mount the export, select the data you want, review what you've staged, and export the new file.

```mermaid
flowchart LR
    mount([mount]) --> add([add]) -.-> review([status · edit · remove]) -.-> export([export])

    classDef core fill:#0969da,stroke:#0969da,color:#ffffff
    classDef optional fill:transparent,stroke:#8c959f,stroke-dasharray:4 3,color:#8c959f
    class mount,add,export core
    class review optional
```

Here, **staging data** means saving it as part of your export selection, along with any date ranges. For example, you could stage a full year of steps and one month of heart-rate readings. The CLI remembers these choices between commands and writes the matching records when you run `export`.

### Commands

| Command  | Options                                  | Description                                                                                            |
| :------- | :--------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| `mount`  |                                          | Accept a `.zip`, a directory, or a file, as long as it contains a valid Apple Health export.            |
| `add`    | `-a, -all`<br>`-s, -start`<br>`-e, -end` | Stage one or more categories, optionally with start and end dates. You can also select all categories. |
| `status` |                                          | Review staged categories and their date ranges, and see which categories are still available.          |
| `edit`   | `-a, -all`<br>`-s, -start`<br>`-e, -end` | Edit the date ranges of all or selected staged categories.                                             |
| `remove` | `-a, -all`                               | Remove all or selected categories from staging.                                                        |
| `export` |                                          | Write the selected records to a new XML file.                                                          |

---

## How to use
Work in progress...

## Roadmap

```text
●  finished stage   ◐  current stage   ○  later stage   [x] done   [ ] to do

●  STAGE 0 · Groundwork
│  ████████████████████  3/3
│
├── [x] Learn about XML data
├── [x] Figure Apple Health export.xml data structure and schema
│       using the Linux CLI
├── [x] Set up the project repo with a README
│
◐  STAGE 1 · Basic functionality (MVP)
│  ░░░░░░░░░░░░░░░░░░░░  0/36
│
├── [ ] Implement the mount command
│   ├── [ ] Find export.xml in a .zip, directory, or file by checking
│   │       for the HealthData root, not the filename
│   ├── [ ] Handle permission errors, missing paths, corrupt .zip files,
│   │       non-Health XML, and zero or multiple candidates
│   ├── [ ] Define what a category is (record types, workouts, activity
│   │       summaries) and how users refer to them
│   └── [ ] Stream-parse the file and record each category's count,
│           date range, and estimated size
├── [ ] Save state between commands
│   ├── [ ] Keep one active source in an app data folder, independent
│   │       of the current directory
│   ├── [ ] Save the source path, inventory, and staged categories
│   ├── [ ] Reset staged categories when a new source is mounted
│   └── [ ] Detect when the mounted source has changed, moved, or
│           been deleted
├── [ ] Implement the status command
│   ├── [ ] Show each category's name, start/end date, count, and
│   │       estimated size
│   ├── [ ] Show staged categories and their date ranges
│   └── [ ] Handle nothing mounted and nothing staged
├── [ ] Implement the add command
│   ├── [ ] -start and -end date ranges for all or selected categories
│   ├── [ ] Validate dates (format, start before end, time zones) and
│   │       document whether boundaries are inclusive
│   ├── [ ] Handle incorrect category names
│   └── [ ] Handle categories that are already staged
├── [ ] Implement the edit command
│   ├── [ ] Change date ranges for all or selected staged categories
│   ├── [ ] Handle incorrect category names
│   └── [ ] Handle categories that aren't staged
├── [ ] Implement the remove command
│   ├── [ ] Remove all or selected categories from staging
│   └── [ ] Handle incorrect or unstaged category names
├── [ ] Implement the export command
│   ├── [ ] Stream the staged records into a new XML file that keeps
│   │       the Apple Health export schema intact
│   ├── [ ] Export to the current directory by default, or accept a
│   │       custom export path
│   ├── [ ] Never modify the mounted source
│   ├── [ ] Handle an empty selection and an existing output file
│   └── [ ] Handle path permission, bad path, and failed export errors
├── [ ] Release the MVP
│   ├── [ ] Test every command on small synthetic exports
│   ├── [ ] Measure time and peak memory on a full export
│   └── [ ] Document installation, usage, and known limitations
│
○  STAGE 2 · Formats, sources, and privacy
│  ░░░░░░░░░░░░░░░░░░░░  0/9
│
├── [ ] Export to different formats
│   ├── [ ] JSON
│   ├── [ ] CSV
│   ├── [ ] Relational database
│   └── [ ] Document database
├── [ ] Edit sources per data category
├── [ ] Remove personal information
│   ├── [ ] Strip the <Me> element (date of birth, sex, blood type)
│   └── [ ] Anonymise device and source names
│
○  STAGE 3 · Advanced data aggregation
│  ░░░░░░░░░░░░░░░░░░░░  0/4
│
├── [ ] Convert raw data records to daily, weekly, monthly, and
│   │   yearly aggregates
│   ├── [ ] Choose a calculation for each metric (for example, sum
│   │       steps and average heart rate)
│   └── [ ] Handle different data sources for some categories
├── [ ] Compare the results with Apple Health
│
○  STAGE 4 · Final touches
│  ░░░░░░░░░░░░░░░░░░░░  0/2
│
├── [ ] Import and export reusable selection presets
└── [ ] Stylized CLI output
```
