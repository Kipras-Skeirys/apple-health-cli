# Sample exports

Synthetic Apple Health `export.xml` files for testing.

| File                | Size    | Record types | Records | Date range | Other elements                                                                                              |
| :------------------ | :------ | -----------: | ------: | :--------- | :---------------------------------------------------------------------------------------------------------- |
| `small_export.xml`  | 281 KB  |            8 |     602 | 1 month    | 6 workouts, 30 activity summaries                                                                           |
| `medium_export.xml` | 3.0 MB  |           34 |   5,823 | 3 years    | Blood pressure and food correlations, 120 workouts, daily activity summaries, clinical records, 1 audiogram |
| `large_export.xml`  | 14.7 MB |          106 |  28,005 | 10 years   | All of the above at larger scale, plus vision prescriptions                                                 |
| `empty_file.xml`    | 0 B     |            — |       — | —          | Empty file, for testing the "not a valid XML file" error                                                    |
| `invalid_file.xml`  | 25 B    |            — |       — | —          | Non-Health root element, for testing the "not Apple Health data" error                                      |
