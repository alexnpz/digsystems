#!/bin/bash
# We wil need to add this command later on console chmod u+x singlefile2git.sh
echo Script to update a single file to Github
echo We will show you the files untrack, from one of those, copy completely and push it to Git
git status
echo Introduce the filename:
read varstring
git add ${varstring}
git commit -m "Updating ${varstring}"
git push
read -p "Press any key to close..."