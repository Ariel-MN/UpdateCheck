# Update Check

## Python Application Update Check

### Instructions:

1. Download the update package.
2. Run `CreateShortcut.vbs` to generate the program's shortcut.

### Information:
- The update process is managed by the `bin/update_check.pyw` module. It should be called as a new process, passing a version number parameter in string format 'v0.0.0', similar to GitHub's release tag format. Optionally, you can also pass the path to a Python script to restart the program. Before launching `bin/update_check.pyw`, the main program script should ensure that no other instances are running to prevent file conflicts.
- The example application intentionally maintains a version number lower than the latest release tag. To repeat the update process, you can simply modify the `__version__` variable in the `main_program.pyw` script.
- The `update_check` module compares the version number in the `__version__` variable of `main_program.pyw` to the tag of the latest release.
- When creating a new GitHub release, ensure all modified files, including the `update.json` file, are included outside of the source code zip file. Update the `update.json` file with the correct paths where these files should be placed during the installation process.

Refer to the release example provided in this repository for guidance.
