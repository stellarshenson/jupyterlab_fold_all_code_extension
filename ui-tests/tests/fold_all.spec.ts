import { expect, test } from '@jupyterlab/galata';

const NOTEBOOK = 'fold_all.ipynb';

test('fold-all and expand-all set and remove jupyter.source_hidden in the saved file', async ({
  page,
  tmpPath
}) => {
  const path = `${tmpPath}/${NOTEBOOK}`;

  // Runs a command, saves, and reads source_hidden of every cell from the file
  const runAndRead = async (command: string) => {
    await page.evaluate(
      id => (window as any).jupyterapp.commands.execute(id),
      command
    );
    await page.notebook.save();
    return page.evaluate(async p => {
      const model = await (
        window as any
      ).jupyterapp.serviceManager.contents.get(p);
      return model.content.cells.map((c: any) => [
        c.cell_type,
        c.metadata?.jupyter?.source_hidden ?? null
      ]);
    }, path);
  };

  await page.notebook.createNew(NOTEBOOK);
  await page.notebook.setCell(0, 'code', '1 + 1');
  await page.notebook.addCell('code', '2 + 2');
  await page.notebook.addCell('markdown', 'text');

  expect(
    await runAndRead('jupyterlab_fold_all_code_extension:fold-all')
  ).toEqual([
    ['code', true],
    ['code', true],
    ['markdown', null]
  ]);
  await expect(page.locator('.jp-Notebook .jp-InputCollapser')).toHaveCount(3);
  await expect(
    page.locator('.jp-Notebook .jp-CodeCell .jp-InputArea-editor:visible')
  ).toHaveCount(0);

  expect(
    await runAndRead('jupyterlab_fold_all_code_extension:expand-all')
  ).toEqual([
    ['code', null],
    ['code', null],
    ['markdown', null]
  ]);
  await expect(
    page.locator('.jp-Notebook .jp-CodeCell .jp-InputArea-editor:visible')
  ).toHaveCount(2);
});
