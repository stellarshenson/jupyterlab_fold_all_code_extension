"""
Preprocessor to remove folded (hidden) code cells during notebook export.

This preprocessor checks for the `jupyter.source_hidden` metadata on cells
and removes the source code from those cells during export to HTML, PDF, etc.
"""

from nbconvert.exporters import NotebookExporter
from nbconvert.preprocessors import Preprocessor


class RemoveFoldedCodePreprocessor(Preprocessor):
    """
    Preprocessor that removes source code from cells marked as hidden.

    When a code cell has metadata `jupyter.source_hidden = true`, the cell's
    source code will be cleared during export, effectively hiding it from
    the exported document.
    """

    def preprocess(self, nb, resources):
        # a notebook written as a notebook keeps its code: `nbconvert --to notebook --inplace` would destroy it
        if isinstance(self.parent, NotebookExporter):
            return nb, resources
        return super().preprocess(nb, resources)

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Process each cell and remove source if marked as hidden.

        Parameters
        ----------
        cell : NotebookNode
            The cell to preprocess
        resources : dict
            Additional resources used in preprocessing
        cell_index : int
            Index of the cell being processed

        Returns
        -------
        cell : NotebookNode
            The processed cell (with source removed if hidden)
        resources : dict
            The resources dict
        """
        # Check if this is a code cell with hidden source
        if cell.cell_type == 'code':
            jupyter_metadata = cell.metadata.get('jupyter', {})
            if jupyter_metadata.get('source_hidden', False):
                # Clear the source code - cell remains but code is hidden
                cell.source = ''
                # nbconvert's own mark (TagRemovePreprocessor): the templates then render no input box
                cell.metadata['transient'] = {'remove_source': True}

        return cell, resources
