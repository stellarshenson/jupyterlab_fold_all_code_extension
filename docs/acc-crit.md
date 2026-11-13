# Acceptance criteria

What the JupyterLab fold all code extension must do, one criterion per feature the README states.

## Authors

- `@kj` Konrad Jelen

## Export `EXPORT`

Folded code in exported documents

- log: 2026-11-13T06:49:42Z @kj category created

- [x] `ACC-EXPORT-1-HIDE-CODE` **Export hides folded code** - HIGH; a code cell with `jupyter.source_hidden` true exports to HTML and PDF with no code and no input box; its output and every unfolded cell stay
  - evidence: build_test.py 1.0.43: pytest 3 passed, test_html_export_hides_folded_code_and_its_input_box
  - test: pytest test_html_export_hides_folded_code_and_its_input_box
  - test-tags: UNIT
  - log: 2026-11-13T06:49:42Z @kj added
  - log: 2026-11-13T06:51:42Z @kj closed
- [x] `ACC-EXPORT-2-LAB-EXPORT` **JupyterLab export menu uses the preprocessor** - HIGH; the server extension adds `RemoveFoldedCodePreprocessor` to every nbconvert exporter, so Save and Export Notebook As hides folded code
  - evidence: build_test.py 1.0.43: pytest 3 passed, test_server_extension_adds_preprocessor_to_every_exporter
  - test: pytest test_server_extension_adds_preprocessor_to_every_exporter
  - test-tags: UNIT
  - log: 2026-11-13T06:49:42Z @kj added
  - log: 2026-11-13T06:51:42Z @kj closed
- [x] `ACC-EXPORT-3-KEEP-NOTEBOOK` **Notebook export keeps the code** - CRITICAL; an export to `.ipynb` keeps the source of folded cells, so `jupyter nbconvert --to notebook --inplace` never removes code
  - evidence: build_test.py 1.0.43: pytest 3 passed, test_notebook_export_keeps_folded_code
  - test: pytest test_notebook_export_keeps_folded_code
  - test-tags: UNIT
  - log: 2026-11-13T06:49:42Z @kj added
  - log: 2026-11-13T06:51:42Z @kj closed

## Folding `FOLD`

Folding and expanding all code cells

- log: 2026-11-13T06:49:42Z @kj category created

- [ ] `ACC-FOLD-4-FOLD-ALL` **Fold and expand all code cells** - MEDIUM; View menu `Collapse All Code` and `Expand All Code`, and the commands `jupyterlab_fold_all_code_extension:fold-all` and `:expand-all`, hide or show every code cell and set or remove `jupyter.source_hidden`
  - test: Galata: run fold-all on a 2-cell notebook, save, read jupyter.source_hidden from the file
  - test-tags: E2E
  - log: 2026-11-13T06:49:42Z @kj added
