"""
The MIT License (MIT)

Copyright (c) 2023-present shiüo

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import os.path
import pathlib
import subprocess
import time

from tools import clear


def build(
    withconsole,
    path,
    file_dict,
    companyname,
    product_version,
    icon,
    plugin_dict,
    include_package_dict,
):
    try:
        # Formatting the code and creating requirements.txt file
        clear.code_format_and_make_requirements_txt(path=os.path.dirname(path))

        # Define build file name and output directory name
        buildfile_name = path
        Output_dir_name = os.path.join(
            os.path.dirname(path), f"{pathlib.Path(path).stem}_build"
        )

        # Creating a list to store files that should be included
        should_include = []

        # Check if file_dict is not None
        if file_dict is not None:
            # Iterate over the file_dict and append the full file path to should_include list
            for i in range(0, len(file_dict)):
                should_include.append(os.path.join(os.path.dirname(path), file_dict[i]))

        # Construct the command for nuitka
        command = (
            f"python -m nuitka --clang --show-modules --follow-imports "
            f"--windows-company-name={companyname} --windows-product-version={product_version} "
            f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads --onefile "
        )

        # Append include-data-dir options to the command
        for i in range(0, len(should_include)):
            command += f"--include-data-dir={should_include[i]}={file_dict[i]} "

        # Append enable-plugin options to the command
        for i in range(0, len(plugin_dict)):
            command += f"--enable-plugin={plugin_dict[i]} "

        # Check if include_package_dict is not None
        if include_package_dict is not None:
            # Append include-package options to the command
            for i in range(0, len(include_package_dict)):
                command += f"--include-package={include_package_dict[i]} "

        # Check if withconsole is True
        if withconsole:
            # Check if icon is None
            if icon is None:
                command = command + f"{buildfile_name}"
            else:
                command = (
                    command + f"--windows-icon-from-ico={icon} " + f"{buildfile_name}"
                )
        else:
            # Check if icon is None
            if icon is None:
                command = command + f"--windows-disable-console " + f"{buildfile_name}"
            else:
                command = (
                    command
                    + f"--windows-disable-console "
                    + f"--windows-icon-from-ico={icon} "
                ) + f"{buildfile_name}"

        # Measure the time taken for the build process
        start = time.time()
        subprocess.run(command, shell=True, check=True)
        end = time.time()

        # Print the time taken and the command used
        print(f"{end - start}s elapsed")
        print(command)
    except Exception as e:
        print(e)
