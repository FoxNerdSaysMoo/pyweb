import base64
import tarfile
import io

from .const import (
    PYODIDE_URL,
    PYODIDE_JS_URL,
    GET_PYODIDE_FUNC,
    PYODIDE_IMPORT_FUNC,
    B64_TO_BYTES_FUNC,
    WAIT_FOR_GLOBAL_FUNC
)


def build_base():
    return f"""
<script src="{PYODIDE_JS_URL}"></script>
<script>
{GET_PYODIDE_FUNC}
{B64_TO_BYTES_FUNC}
{WAIT_FOR_GLOBAL_FUNC}
getPyodide('{PYODIDE_URL}').then(() => {{
    console.log('pyodide loaded');
}});
{PYODIDE_IMPORT_FUNC}
waitForGlobal("pyodide", async function() {{

// MODULE IMPORTS HERE //  (this is where imports and are added)

}});
</script>
    """


def module_to_b64(module):
    file = io.BytesIO()
    tar = tarfile.open(mode="w:gz", fileobj=file)
    tar.add(module, arcname=module)
    tar.close()
    return base64.b64encode(file.getvalue()).decode("utf-8")


def add_module_import(base, module_name, module_b64, entrypoints):
    indx = base.index("// MODULE IMPORTS HERE //")
    base = base[:indx] + f"""
importPyweb('{module_b64}');
pyodide.runPython(`
import js
import {module_name}
{''.join([x+'(js);' for x in entrypoints])}
`);
""" + base[indx:]
    return base


def build_js(modules):
    """`modules` is in format of {module: [entrypoints if any]} and entrypoints are absolute paths"""
    base = build_base()
    for module, entrypoints in modules.items():
        base = add_module_import(base, module, module_to_b64(module.split(".")[0]), entrypoints)
    return base
