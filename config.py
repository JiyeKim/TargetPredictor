from pathlib import Path


BASE_DIR = Path("__file__").resolve().parent.parent

PATH_CONFIG = {
    'TREAP_SCRIPT': f'{BASE_DIR}/rscripts/run_treap.R',
}
