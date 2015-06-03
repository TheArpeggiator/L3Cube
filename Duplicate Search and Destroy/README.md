Search and Destroy all Duplucates
=================================

Simple shell script which uses fdupes command to search recursively for duplicates in path passed as command line parameter.
Assumes fdupes is preinstalled in system. If not use "apt-get install fdupes".

Content based checking (includes md5 checks), will avoid checking all empty files. Will not detect duplicates if file names are the same since it uses content based checking schemes.