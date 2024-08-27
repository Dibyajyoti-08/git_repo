# Git Walk-Through

This guide provides a step-by-step process for using Git, from configuring Git with your personal account to creating branches, committing changes, and managing remote repositories.

### 1. Configuring Git with Personal GitHub Account
```bash
$ git config --global user.name "Dibyajyoti-08"
$ git config --global user.email "eng.djena075@gmail.com"
```

### 2. Creating a Git Folder
```bash
$ mkdir myproject
$ cd myproject
```

### 3. Initializing Git
```bash
$ git init
Initialized empty Git repository in /home/phytec/Documents/gitProject/myproject/.git/
```

### 4. Creating a Simple C Code
```bash
$ nano test.c
```

### 5. Checking the Git Status
```bash
$ git status
```

### 6. Staging Files for Commit
```bash
$ git add test.c
$ git status
```

### 7. Adding All Files at Once
```bash
$ git add --all
```

### 8. Performing Git Commit
```bash
$ git commit -m “first release of test.c”
```

### 9. Committing Changes Directly Without Staging
```bash
$ nano test.c
# Make some changes
$ git commit -a -m “Updated test.c with a new line.”
```

### 10. Viewing the Commit History
```bash
$ git log
```

### 11. Creating a New Git Branch
```bash
$ git branch Git_test_v0.1
```

### 12. Viewing Available Branches
```bash
$ git branch
```

### 13. Switching to a New Branch
```bash
$ git checkout Git_test_v0.1
```

### 14. Modifying Files in a Branch
```bash
$ nano test.c
$ nano new.c
$ git status
```

### 15. Staging and Committing Changes in a Branch
```bash
$ git add --all
$ git commit -m “Added a new file in the source”
```

### 16. Switching Between Branches
```bash
$ git checkout master
$ ls
```

### 17. Creating and Switching to an Emergency Fix Branch
```bash
$ git branch emergency-fix
$ git checkout emergency-fix
# or
$ git checkout -b emergency-fix
```

### 18. Merging Branches
```bash
$ git checkout master
$ git merge emergency-fix
```

### 19. Deleting a Branch After Merge
```bash
$ git branch -d emergency-fix
```

### 20. Handling Merge Conflicts
```bash
$ git checkout Git_test_v0.1
$ git add --all
$ git commit -m "added a new print line in the test.c"
$ git checkout master
$ git merge Git_test_v0.1
# Resolve conflicts in the file
$ git add test.c
$ git commit -m "Merged the new branch Git_test_v0.1"
```

### 21. Creating a Repository on GitHub
Follow GitHub's interface to create a new repository.
![img 1](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2014-12-47.png)
![img 2](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2014-12-54.png)
![img 3](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2014-13-08.png)

### 22. Pushing Local Repository to GitHub
```bash
$ git remote add origin https://github.com/Dibyajyoti-08/git_repo.git
$ git push --set-upstream origin master
```
![img 4](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2014-32-10.png)

### 23. Fetching Updates from Remote Repository
```bash
$ git fetch origin
```

### 24. Checking the Status After Fetch
```bash
$ git status
```

### 25. Viewing the Log for the Remote Branch
```bash
$ git log origin/master
```

### 26. Checking Differences Between Local and Remote
```bash
$ git diff origin/master
```

### 27. Merging Remote Updates to Local Branch
```bash
$ git merge origin/master
```

### 28. Fetching Updates from Remote Repository

I manually updated the README file, and now I'm ready to pull the updated repository. Before pulling, I'll fetch the changes to see what has been updated in the remote repository. Fetching gets all the change history of a tracked branch/repository.

```bash
$ git fetch origin
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 1.98 KiB | 404.00 KiB/s, done.
From https://github.com/Dibyajyoti-08/git_repo
   181afe1..7778827  master -> origin/master
```

### 29. Checking the Status of the Local Branch

Now that we have fetched the recent changes, we can check the status of our local branch.

```bash
$ git status
On branch master
Your branch is behind 'origin/master' by 2 commits and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

### 30. Viewing the Commit Log

We have one commit in our branch. To see the recent commits, we can view the log.

```bash
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
```

### 31. Checking Differences Between Local and Remote Branch

To see what has changed between the local and remote branches, we can use the `git diff` command.

```bash
$ git diff origin/master
diff --git a/README.md b/README.md
deleted file mode 100644
index f46da1b..0000000
--- a/README.md
+++ /dev/null
@@ -1,2 +0,0 @@
-# Git Hub Walk-Through
-This is a git hub test to know how git hub works.
```

### 32. Merging the Local Branch with the Remote Branch

Now, we'll merge the changes from the remote branch into our local branch.

```bash
$ git merge origin/master
Updating 181afe1..7778827
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

### 33. Pulling Changes Directly

If you want to update your local repository without fetching and merging separately, you can use the `git pull` command. This command is a combination of fetch and merge.

```bash
$ git pull origin
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 1.02 KiB | 1.02 MiB/s, done.
From https://github.com/Dibyajyoti-08/git_repo
   7778827..b126183  master -> origin/master
Updating 7778827..b126183
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 34. Pushing Changes to GitHub

Let's make some changes in the `new.c` file and push them to GitHub. You can add and commit changes separately, or you can do both in a single command.

```bash
$ nano new.c

$ git commit -a -m "Updated a new line in new.c"
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
```
![img 5](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-04-23.png)

### 35. Pulling a Branch from GitHub

After creating a new branch in GitHub and making changes in `new.c`, we can pull the branch from GitHub.

```bash
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
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
```

We cannot see the remote branch in the local Git by default, but we can use the `-a` option to list all branches, including remote branches.

```bash
$ git branch -a
  Git_test_v0.1
* master
  remotes/origin/git_test-v0.1
  remotes/origin/master
```

### 36. Switching to the New Branch

Let's switch to the newly created branch.

```bash
$ git checkout git_test-v0.1

$ git branch
  Git_test_v0.1
* git_test-v0.1
  master
```

### 37. Checking If the Branch Is Up to Date

Now, we'll check if the branch is up to date.

```bash
$ git pull
Already up to date.
```

### 38. Pushing a Local Branch to GitHub

If you already have a local branch (`Git_test_v0.1`), you can push it to GitHub.

```bash
$ git checkout Git_test_v0.1
```

### 39. Adding and Committing Changes

After adding a README file, we can push the changes to the branch.

```bash
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
```

### 40. Pushing the Branch to GitHub

Finally, push the branch from the local Git repository to GitHub.

```bash
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
To https://github.com

/Dibyajyoti-08/git_repo.git
 * [new branch]      Git_test_v0.1 -> Git_test_v0.1
```
![img 6](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-26-07.png)


### 41. We can now create a pull request in order to merge this branch.
![img 7](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-28-19.png)
![img 8](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-28-40.png)



### 42. Click on the request you got and if it looks good you can merge it
![img 9](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-29-04.png)
![img 10](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-30-15.png)
![img 11](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-30-35.png)
![img 12](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-30-51.png)
![img 13](https://github.com/Dibyajyoti-08/git_repo/blob/94070c0709f47a2138d4350b113866373d2f34ad/images/Screenshot%20from%202024-08-27%2015-30-59.png)

