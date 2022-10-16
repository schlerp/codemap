# CODEMAP

You've found CodeMap! It's a modern tool for maintaining codesets. It provides a simple rest interface for creating, reading, updating and deleting codes and codesets.

## Data structures

The basic data sctructure is a code, this contains a key and a value, along with data types for each. This allows smart serialisation into the backend database, and the ability to use both strings, numbers and binary objects as keys and values.

Another thing you should to know is that `Code` objects belong to codesets. A codeset is essentially a name/grouper for dealing iwth sets of codes. This allows a high level object for getting groups of codes and creating extracts for use in applications.

# Dynamic use

You can also look up code values directly using the REST endpoints if you know the codeset name and the key.
