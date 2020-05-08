import os


def find_files(suffix, path):
    if suffix == "":
        return []

    matching_paths = []

    if os.path.isdir(path):

        for subdir in os.listdir(path):
            match = find_files(suffix, path + "/" + subdir)
            matching_paths = matching_paths + match

    else:
        if path.endswith(suffix):
            return [path]

    return matching_paths


# Test case 1
print(find_files('.c', "testdir"))
# expected output
# ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

# Test case 2
print(find_files('.h', "testdir"))
# expected output
# ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h']

# Test case 3 Edge Case
print(find_files('.pdf', "testdir"))
# expected output
# []

# Test case 4 Edge Case
print(find_files('', "testdir"))
# expected output
# []
