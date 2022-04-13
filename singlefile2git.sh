#!/bin/bash
# We wil need to add this command later on console chmod u+x deploy.sh
echo Script to update a single file to Github
echo We will show you the files untrack
git status
echo Introduce the filename:
read varstring
git add ${varstring}
git commit -m "Updating ${varstring}"
git push
read -p "Press any key to close..."