# Git Hub Walk-Through

1.Configuring git with my personal git hub account username and email,

'''bash
$ git config --global user.name "Dibyajyoti-08"
$ git config --global user.email "eng.djena075@gmail.com"

2.Create a Git folder,

$ mkdir myproject
$ cd myproject

3.Initialize the Git,

$ git init
Initialized empty Git repository in /home/phytec/Documents/gitProject/myproject/.git/

4.Create a simple c code,

$ nano test.c

5.Check the status,

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	test.c

nothing added to commit but untracked files present (use "git add" to track)


6.Do the git staging environment,

$ git add test.c
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   test.c

7.We can add all the files in one go,

$ git add --all

8.Lets perform git commit now,

$ git commit -m “first release of test.c”
[master (root-commit) 68cbddb] first release of test.c
 1 file changed, 5 insertions(+)
 create mode 100644 test.c

9.It is possible to commit changes directly, skipping the staging environment using -a option,

$ nano test.c
-> make some changes

$ git status --sort
M test.c

$ git commit -a -m “Updated test.c with a newline.”
[master eaaf6ce] Updated test.c with a new line.
 1 file changed, 1 insertion(+)

10.To view history of commits for the repository,

$ git log
commit eaaf6ce9c861694e4a8861c6982e62d5222b8bd4 (HEAD -> master)
Author: Dibyajyoti-08 <eng.djena075@gmail.com>
Date:   Tue Aug 27 12:17:20 2024 +0530

    Updated test.c with a new line.

commit 68cbddba4ee33563f1f4ae33438fda1eaab288e9
Author: Dibyajyoti-08 <eng.djena075@gmail.com>
Date:   Tue Aug 27 12:09:54 2024 +0530

    first release of test.c

11.Create a new git branch,

$ git branch Git_test_v0.1

12.If we see there will be 2 branches one is the defualt one and another is the one you have created,

$ git branch
  Git_test_v0.1
* master

13.Lets switch to the branch that we have created,

$ git checkout Git_test_v0.1
Switched to branch 'Git_test_v0.1'

14.Now our git branch has been changed, then i have made some changes in the test.c and also added a new file as new.c, if we check the status,

$ git status
On branch Git_test_v0.1
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   test.c

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	new.c

no changes added to commit (use "git add" and/or "git commit -a")



15.Now we will add all the changes and commit it,

$ git add --all

$ git status
On branch Git_test_v0.1
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   new.c
	modified:   test.c

$ git commit -m “Added a new file in the source”
[Git_test_v0.1 077fe3d] Added a new file in the source.
 2 files changed, 8 insertions(+), 1 deletion(-)
 create mode 100644 new.c

$ git status 
On branch Git_test_v0.1
nothing to commit, working tree clean

16.If we switch between the branches and checkout the master branch we can see that in the master branch there is no such file as new.c

$ ls
new.c  test.c
$ git checkout master
$ ls
test.c










17.Let suppose i want to fix something but i dont want to mess with the master branch or Git_test_v0.1, then we will create a new branch called emergency-fix. 

$ git branch emergency-fix

$ git checkout emergency-fix

or we can make a new branch and checkout at the same time,

$ git checkout -b emergency-fix
$ nano test.c 

-> change something in that file

$ git status
On branch emergency-fix
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   test.c

no changes added to commit (use "git add" and/or "git commit -a")

$ git add test.c

$ git commit -m “updated test.c for a small bug fix”

18.Now we can merge the branches

$ git checkout master

19.Now merge the current branch with the emergency-fix branch

$ git merge emergency-fix
Updating eaaf6ce..42734d3
Fast-forward
 test.c | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)


20.As master and emergency-fix branch is same we can now delete the emergency-fix branch

$ git branch -d emergency-fix
Deleted branch emergency-fix (was 42734d3).

21.For Merge Conflict concept we will switch to the Git_test_v0.1 and do the changes in the test.c, then we will add and commit it,

$ git checkout Git_test_v0.1

$ git add --all

$ git commit -m "added a new print line in the test.c"

22.Now we will checkout to the master branch and merge the Git_test_v0.1, but what will happen to the recent change that we made in the master branch? The merge will get failed, as there is conflict between the versions for the test.c, we can check the same in the status as well,

$ git checkout master

$ git merge Git_test_v0.1
Auto-merging test.c
CONFLICT (content): Merge conflict in test.c
Automatic merge failed; fix conflicts and then commit the result.

$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	new file:   new.c

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   test.c

23.Now it is confirmed that there is conflict between the versions of the test.c file now open the file and make changes to resolve the conflict of the versions, then we will add the file and check the status,

$ nano test.c
# include<stdio.h>
int main() {
	printf("This is the Git test.");
<<<<<<< HEAD
	print("Small change occured");
	print("Bug fix");
=======
	printf("Small change occured!");
	printf("new change.");
	printf("Added a new line.");
>>>>>>> Git_test_v0.1
	return 0;
}
-> Make the changes and add the file
# include<stdio.h>
int main() {
	printf("This is the Git test.");
	print("Small change occured");
	print("Bug fix");
	printf("Small change occured!");
	printf("new change.");
	printf("Added a new line.");
	return 0;
}

$ git add test.c
$ git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
	new file:   new.c
	modified:   test.c
-> now commit the changes in the master branch

$ git commit -m "Merged the new branch Git_test_v0.1"



24.Create a repository in git hub,




25.Since we have already set up a local git  repo, we are going to push it to the git hub.

$ git remote add origin https://github.com/Dibyajyoti-08/git_repo.git
-> this implies that we are adding a remote repository, with the specified URL, as an origin to the local git repo

26.Now we can push our master branch to the origin url and set it as a default remote branch

$ git push --set-upstream origin master 
-> it will ask for your username and password, for the password i am using token,
Username for 'https://github.com': Dibyajyoti-08
Password for 'https://Dibyajyoti-08@github.com': 
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 4 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (19/19), 1.72 KiB | 878.00 KiB/s, done.
Total 19 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/Dibyajyoti-08/git_repo.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

27.You can now see your file in the git hub repository,


28.So i changed readme manually now i will pull the updated repo, but first we will fetch and see what happens, as fetch gets all the change history of a tracked branch/repo 

$ git fetch origin
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 1.98 KiB | 404.00 KiB/s, done.
From https://github.com/Dibyajyoti-08/git_repo
   181afe1..7778827  master     -> origin/master







29.Now we have our recent changes, we can check our status,

$ git status
On branch master
Your branch is behind 'origin/master' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

30.As we can see we have 1 commit in our branch, to check we can get the log,

$ git log origin/master
commit 7778827316f84efa95e0be8e678f3e10ca71d2b2 (origin/master)
Author: djena <114151571+Dibyajyoti-08@users.noreply.github.com>
Date:   Tue Aug 27 14:38:01 2024 +0530

    Update README.md

commit fe56d0f8b26b1f49eba558b9ec3b273c10bbeac4
Author: djena <114151571+Dibyajyoti-08@users.noreply.github.com>
Date:   Tue Aug 27 14:37:13 2024 +0530

    Create README.md

commit 181afe1885747d15c41406bebdac1cba1c41a098 (HEAD -> master)
Merge: 42734d3 259a143
Author: Dibyajyoti-08 <eng.djena075@gmail.com>
Date:   Tue Aug 27 13:12:59 2024 +0530

    Merged the new branch Git_test_v0.1
...

31.We can also check the differences as,

$ git diff origin/master
diff --git a/README.md b/README.md
deleted file mode 100644
index f46da1b..0000000
--- a/README.md
+++ /dev/null
@@ -1,2 +0,0 @@
-# Git Hub Walk-Through
-This is a git hub test to know how git hub works.

32.Now we will merge the current branch with the specified branch,

$ git merge origin/master
Updating 181afe1..7778827
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 README.md


33.But what if you just want to update your local repo without going through all the changes, as pull is the combination of fetch and merge, instead of this step you can just pull the changes from the remote repository to the branch you are working on.
 
$ git pull origin 
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1.02 KiB | 1.02 MiB/s, done.
From https://github.com/Dibyajyoti-08/git_repo
   7778827..b126183  master     -> origin/master
Updating 7778827..b126183
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

34.For push the changes to the git hub let us make some changes in the file and push it to the git hub,

$ nano new.c

-> Either you can add and commit or you can do the both in one line,

$ git commit -a -m “Updated a new line in new.c”
[master bdf4823] updated a new line in new.c
 1 file changed, 1 insertion(+)

$ git push origin
Username for 'https://github.com': Dibyajyoti-08
Password for 'https://Dibyajyoti-08@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 404 bytes | 404.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Dibyajyoti-08/git_repo.git
   b126183..bdf4823  master -> master










35.So i created a new branch in the git hub and made some changes in the new.c, now we will see how we can pull the branch from the git hub

$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1.02 KiB | 1.02 MiB/s, done.
From https://github.com/Dibyajyoti-08/git_repo
 * [new branch]      git_test-v0.1 -> origin/git_test-v0.1
Already up to date.

$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

$ git branch
  Git_test_v0.1
* master

-> as we cannot see our remote branch in local git but with -a option we can see both the loca and remote git repo,

$ git branch -a
  Git_test_v0.1
* master
  remotes/origin/git_test-v0.1
  remotes/origin/master

36.Now we will switch to our newly created branch,

$ git checkout git_test-v0.1

$ git branch
  Git_test_v0.1
* git_test-v0.1
  master

37.Check if this is all upto date

$ git pull
Already up to date.

38.As you can see i have already one local new branch Git_test_v0.1, lets try to push it to git hub,

$ git checkout Git_test_v0.1




39.So i added a readme file and lets push this branch with this changes,

$ git status
On branch Git_test_v0.1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)

$ git add README.md

$ git commit -m "update readme file in this branch"
[Git_test_v0.1 60ed1d4] update readme file in this branch
 1 file changed, 2 insertions(+)
 create mode 100644 README.md

40.Now lets push our branch from local git repo to the git hub

$ git push origin Git_test_v0.1
Username for 'https://github.com': Dibyajyoti-08
Password for 'https://Dibyajyoti-08@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 379 bytes | 379.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'Git_test_v0.1' on GitHub by visiting:
remote:      https://github.com/Dibyajyoti-08/git_repo/pull/new/Git_test_v0.1
remote: 
To https://github.com/Dibyajyoti-08/git_repo.git
 * [new branch]      Git_test_v0.1 -> Git_test_v0.1


41. We can now create a pull request in order to merge this branch.



42.Click on the request you got and if it looks good you can merge it,




