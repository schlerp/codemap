# CODEMAP

You've found `CodeMap`! It's a modern tool for maintaining codesets. It provides a simple rest interface for creating, reading, updating and deleting codes and codesets.

## Data structures

The basic data sctructure is a `Code`, this contains a key and a value, along with data types for each. This allows smart serialisation into the backend database, and the ability to use both strings, numbers and binary objects as keys and values.

Another thing you should to know is that `Code` objects belong to `CodeSet` objects. A `Codeset` is essentially a name/grouper for referring to collections of `Code` objects. This essentially provides a high level object for getting groups of codes and creating extracts for use in applications.

# Dynamic use

You can also look up a `Code.value` directly using the REST endpoints. You will need to know the codeset name and the key.

```bash
# get a code value for the key foo, in the codeset baz
curl http://codesetapi/baz/foo

{
    name: "foo",
    name_datatype: "str",
    value: "bar",
    value_datatype: "str"
}
```
