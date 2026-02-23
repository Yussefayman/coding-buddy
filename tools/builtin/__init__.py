from tools.builtin.edit_file import EditFileTool
from tools.builtin.read_file import ReadFileTool
from tools.builtin.write_file import WriteFileTool

_all__ = ['ReadFileTool']

def get_all_builtin_tools() -> list[type]:
    return [
        ReadFileTool,
        WriteFileTool,
        EditFileTool,
    ]