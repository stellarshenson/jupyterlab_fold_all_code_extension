# Defects

Known defects of the JupyterLab fold all code extension, found by reading src/index.ts and the Python package.

## Authors

- `@kj` Konrad Jelen

## Export `EXPORT`

nbconvert preprocessor and its registration

- log: 2026-11-13T06:49:27Z @kj category created

- [x] `DEF-EXPORT-1-INPLACE-WIPE` **In-place notebook conversion deletes folded code** - CRITICAL; `jupyter nbconvert --to notebook --execute --inplace` writes the notebook back with empty source in every folded code cell; the shipped `jupyter_nbconvert_config.json` applies the preprocessor to the notebook exporter too; `preprocessor.py`
  - evidence: build_test.py 1.0.43: pytest 3 passed, test_notebook_export_keeps_folded_code; nbconvert --to notebook --execute --inplace run kept the source
  - root-cause: 2026-11-13T06:49:42Z @kj the preprocessor is set on the base `Exporter`, so it also runs for `NotebookExporter`, whose output overwrites the source file with --inplace
  - repro: fold a code cell, save, run jupyter nbconvert --to notebook --execute --inplace nb.ipynb, read the cell source
  - test-tags: UNIT
  - log: 2026-11-13T06:49:27Z @kj added
  - log: 2026-11-13T06:51:41Z @kj closed: preprocessor skips NotebookExporter
- [x] `DEF-EXPORT-2-EMPTY-BOX` **Folded cell leaves an empty input box in the export** - MEDIUM; HTML export shows an `In [ ]:` prompt and an empty code box for every folded cell; only the source text was cleared; `preprocessor.py`
  - evidence: build_test.py 1.0.43: pytest 3 passed, test_html_export_hides_folded_code_and_its_input_box counts 1 input box for 2 cells
  - root-cause: 2026-11-13T06:49:42Z @kj `preprocess_cell` set `cell.source = ''` only; the templates drop the input block only for `metadata.transient.remove_source`
  - repro: fold a code cell, save, export to HTML, look above the cell output
  - test-tags: UNIT
  - log: 2026-11-13T06:49:27Z @kj added
  - log: 2026-11-13T06:51:41Z @kj closed: folded cell marked transient.remove_source
- [x] `DEF-EXPORT-3-NO-TEST` **Export path has no test** - MEDIUM; no test covers the preprocessor or its registration by the server extension; pytest collected 0 tests
  - evidence: build_test.py 1.0.43: pytest 3 passed, jupyterlab_fold_all_code_extension/tests/test_preprocessor.py
  - repro: make test, read the pytest count
  - test-tags: UNIT
  - log: 2026-11-13T06:49:28Z @kj added
  - log: 2026-11-13T06:51:41Z @kj closed: 3 pytest tests added

## Documentation `DOCS`

README claims against the code

- log: 2026-11-13T06:49:28Z @kj category created

- [x] `DEF-DOCS-4-VIEW-MENU` **README names View menu commands the extension does not add** - MINOR; README says Fold/Expand All commands are in the View menu; the extension adds no menu item; the View menu items are JupyterLab's own `Collapse All Code` and `Expand All Code`; `README.md`
  - evidence: README.md Features section; JupyterLab 4.6.6 registers Collapse All Code and Expand All Code with syncCollapse on
  - root-cause: 2026-11-13T06:49:42Z @kj version 1.0.35 removed the context menu items and the README then named a View menu entry that never existed in this extension
  - repro: open the View menu, look for Fold All Code
  - test-tags: MANUAL
  - log: 2026-11-13T06:49:28Z @kj added
  - log: 2026-11-13T06:51:42Z @kj closed: README names JupyterLab's View menu items and the two command ids

## Frontend `FRONT`

Commands in src/index.ts

- log: 2026-11-13T06:49:28Z @kj category created

- [-] `DEF-FRONT-5-DUP-COMMANDS` **Fold and expand commands repeat JupyterLab's own and have no entry point** - MINOR; `fold-all` and `expand-all` do what `notebook:hide-all-cell-code` and `notebook:show-all-cell-code` do, and no menu, palette or shortcut reaches them; `setSourceHidden` repeats the metadata write that `inputHidden` already makes; `src/index.ts`
  - repro: search the command palette for Fold All Code
  - test-tags: MANUAL
  - log: 2026-11-13T06:49:28Z @kj added
  - log: 2026-11-13T06:49:42Z @kj rejected: no user is harmed; removing the commands removes public command ids a shortcut may use; owner decides whether to remove them or add them to the palette

## Packaging `PKG`

Files and metadata the package ships

- log: 2026-11-13T06:49:28Z @kj category created

- [-] `DEF-PKG-6-DEAD-CONFIG` **Unused nbconvert config file and entry point** - MINOR; `jupyter-config/jupyter_nbconvert_config.d/` is not installed and nbconvert reads no such folder; the `nbconvert.preprocessors` entry point group in `pyproject.toml` is read by nothing
  - repro: grep shared-data in pyproject.toml for jupyter_nbconvert_config.d
  - test-tags: MANUAL
  - log: 2026-11-13T06:49:28Z @kj added
  - log: 2026-11-13T06:49:42Z @kj rejected: unused file and metadata, no effect on any user; not worth a change
