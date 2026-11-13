import nbformat
from nbconvert import HTMLExporter, NotebookExporter

PREPROCESSORS = ["jupyterlab_fold_all_code_extension.RemoveFoldedCodePreprocessor"]


def _notebook():
    folded = nbformat.v4.new_code_cell("FOLDED_CODE = 1")
    folded.metadata["jupyter"] = {"source_hidden": True}
    folded.outputs = [nbformat.v4.new_output("stream", text="FOLDED_OUTPUT\n")]
    nb = nbformat.v4.new_notebook()
    nb.cells = [folded, nbformat.v4.new_code_cell("VISIBLE_CODE = 2")]
    return nb


def test_html_export_hides_folded_code_and_its_input_box():
    body, _ = HTMLExporter(preprocessors=PREPROCESSORS).from_notebook_node(_notebook())
    assert "FOLDED_CODE" not in body
    assert "FOLDED_OUTPUT" in body
    assert "VISIBLE_CODE" in body
    # one input box: the visible cell's
    assert body.count('class="jp-InputArea jp-Cell-inputArea"') == 1


def test_notebook_export_keeps_folded_code():
    body, _ = NotebookExporter(preprocessors=PREPROCESSORS).from_notebook_node(_notebook())
    assert "FOLDED_CODE" in body


def test_server_extension_adds_preprocessor_to_every_exporter(jp_serverapp):
    names = [type(p).__name__ for p in HTMLExporter()._preprocessors]
    assert "RemoveFoldedCodePreprocessor" in names
