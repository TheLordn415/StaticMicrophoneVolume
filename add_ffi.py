from typing import List
from PyInstaller.utils.win32 import versioninfo


class FFICreator:
    """Class to generate and apply Windows FFI (file version info)."""

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

    def apply_to_executable(
        self, exe_path: str, ffi_path: str = "file_version_info.ffi"
    ) -> None:
        """Apply FFI to an existing executable."""
        vs_info = versioninfo.load_version_info_from_text_file(ffi_path)
        versioninfo.write_version_info_to_executable(exe_path, vs_info)


def main() -> None:
    """CLI for generating or applying FFI."""
    import sys

    version = "1.1.0"
    ffi_creator = FFICreator(version)

    if len(sys.argv) > 1:
        if sys.argv[1] == "create":
            ffi_creator.generate()
            print("FFI file created.")
        elif sys.argv[1] == "apply" and len(sys.argv) > 2:
            exe_path = sys.argv[2]
            ffi_creator.apply_to_executable(exe_path)
            print(f"FFI applied to {exe_path}.")
        else:
            print("Usage:")
            print("  python add_ffi.py create        # generate .ffi file")
            print("  python add_ffi.py apply app.exe # apply ffi to exe")
    else:
        print("⚠️ No arguments provided. Use 'create' or 'apply'.")


if __name__ == "__main__":
    main()
