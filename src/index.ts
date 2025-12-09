import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the jupyterlab_fold_all_code_extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_fold_all_code_extension:plugin',
  description: 'Jupyterlab extension to fold and expand all code cells, to help create nice notebook to share with non-technical audience',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyterlab_fold_all_code_extension is activated!');
  }
};

export default plugin;
