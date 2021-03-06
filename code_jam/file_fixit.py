"""
Given a list of paths of existing directories on a Unix system and a list of paths of new directories, output the minimal number of mkdir commands required to create the new directories.

For example, given:

    Existing:
            /chicken
            /chicken/egg
            /chicken/egg/spam
    New:
            /chicken
            /chicken/egg/ham/spam
            /chicken/spam

the answer should be 3, because the required commands are:

	mkdir chicken/egg/ham
	mkdir chicken/egg/ham/spam
	mkdir chicken/spam
"""

import os

def split_path(path):
    return list(filter(None, path.strip().split(os.sep)))

with open('input', 'r') as infile, open('output', 'w') as out:
    num_testcases = int(next(infile))
    for testcase in range(num_testcases):
        header = tuple(int(i) for i in next(infile).split())
        n_existing, n_new = header 
        dirs = set()
        for i in range(n_existing):
            existing = split_path(next(infile))
            for j in range(len(existing)):
                dirs.add(os.path.join(*existing[:j+1]))
        before =  len(dirs)
        for i in range(n_new):
            new = split_path(next(infile))
            for j in range(len(new)):
                dirs.add(os.path.join(*new[:j+1]))
        after = len(dirs)
        out.write("Case #{0}: {1}\n".format(testcase+1, after-before))
