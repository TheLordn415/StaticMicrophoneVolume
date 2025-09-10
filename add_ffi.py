from typing import List


class FFICreator:
    """Class to generate a Windows FFI (file version info) file for Nuitka build."""

    def __init__(self, version: str) -> None:
        self.version = version

    def _normalize_version(self) -> List[str]:
        """Convert version string into a list of 4 numeric values."""
        ver_list = [str(digit) for digit in self.version if digit.isdigit()]
        while len(ver_list) < 4:
            ver_list.append("0")
        return ver_list[:4]

    def generate(self, output_path: str = "file_version_info.ffi") -> None:
        """Generate FFI file and write to disk."""
        ver_tuple = f"({', '.join(self._normalize_version())})"
        version_info = f"""# UTF-8
VSVersionInfo(
    ffi=FixedFileInfo(
        filevers={ver_tuple},
        prodvers={ver_tuple},
        mask=0x3f,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo(
          [
            StringTable(
                '040904b0',
                [StringStruct('ProductName', 'StaticMicrophoneVolume'),
                StringStruct('CompanyName', 'TheLordn415 GitHub'),
                StringStruct('LegalCopyright', 'Copyright TheLordn415 2025'),
                StringStruct('FileDescription', 'Static Microphone Volume'),
                StringStruct('InternalName', 'Static Microphone Volume'),
                StringStruct('FileVersion', '{self.version}'),
                StringStruct('ProductVersion', '{self.version}')])
            ]), 
            VarFileInfo([VarStruct('Translation', [1033, 1200])])
        ]
)
"""
        with open(output_path, "w", encoding="utf-8") as fs:
            fs.write(version_info)


def main() -> None:
    """Entry point to create an FFI file."""
    version = "1.1.0"
    FFICreator(version).generate()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "create":
        main()
