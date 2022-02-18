"""
Config values for pyweb.
"""

PYODIDE_JS_URL = 'https://cdn.jsdelivr.net/pyodide/v0.19.0/full/pyodide.js'
PYODIDE_URL = 'https://cdn.jsdelivr.net/pyodide/v0.19.0/full/'

GET_PYODIDE_FUNC = """
var pyodide;
async function getPyodide(url) {
    pyodide = await loadPyodide({ indexURL : url });
}
"""

PYODIDE_IMPORT_FUNC = """
async function importPyweb(b64) {
    let buffer = b64ToBytes(b64);
    await pyodide.unpackArchive(buffer, 'gztar');
}
"""

B64_TO_BYTES_FUNC = """
b64ToBytes = (b64) => {return Uint8Array.from(atob(b64), c => c.charCodeAt(0))};
"""

WAIT_FOR_GLOBAL_FUNC = """
var waitForGlobal = function(key, callback) {
  if (window[key]) {
    callback();
  } else {
    setTimeout(function() {
      waitForGlobal(key, callback);
    }, 100);
  }
};
"""

