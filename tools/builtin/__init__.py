from tools.builtin.read_file import ReadFileTool

_all__ = ['ReadFileTool']

def get_all_builtin_tools() -> list[type]:
    return [
        ReadFileTool,
    ]