# Git Hub Walk-Through

1. Configuring git with my personal GitHub account username and email,

    ```bash
    $ git config --global user.name "Dibyajyoti-08"
    $ git config --global user.email "eng.djena075@gmail.com"
    ```

2. Create a Git folder,

    ```bash
    $ mkdir myproject
    $ cd myproject
    ```

3. Initialize the Git,

    ```bash
    $ git init
    Initialized empty Git repository in /home/phytec/Documents/gitProject/myproject/.git/
    ```

4. Create a simple C code,

    ```bash
    $ nano test.c
    ```

5. Check the status,

    ```bash
    $ git status
    On branch master

    No commits yet

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
        test.c

    nothing added to commit but untracked files present (use "git add" to track)
    ```

6. Do the git staging environment,

    ```bash
    $ git add test.c
    $ git status
    On branch master

    No commits yet

    Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
        new file:   test.c
    ```

7. We can add all the files in one go,

    ```bash
    $ git add --all
    ```

8. Let's perform git commit now,

    ```bash
    $ git commit -m "first release of test.c"
    [master (root-commit) 68cbddb] first release of test.c
    1 file changed, 5 insertions(+)
    create mode 100644 test.c
    ```

9. It is possible to commit changes directly, skipping the staging environment using the `-a` option,

    ```bash
    $ nano test.c
    -> make some changes

    $ git status --sort
    M test.c

    $ git commit -a -m "Updated test.c with a newline."
    [master eaaf6ce] Updated test.c with a new line.
    1 file changed, 1 insertion(+)
    ```

10. To view the history of commits for the repository,

    ```bash
    $ git log
    commit eaaf6ce9c861694e4a8861c6982e62d5222b8bd4 (HEAD -> master)
    Author: Dibyajyoti-08 <eng.djena075@gmail.com>
    Date:   Tue Aug 27 12:17:20 2024 +0530

        Updated test.c with a new line.

    commit 68cbddba4ee33563f1f4ae33438fda1eaab288e9
    Author: Dibyajyoti-08 <eng.djena075@gmail.com>
    Date:   Tue Aug 27 12:09:54 2024 +0530

        first release of test.c
    ```

11. Create a new git branch,

    ```bash
    $ git branch Git_test_v0.1
    ```

12. If we see there will be two branches, one is the default one, and another is the one you have created,

    ```bash
    $ git branch
      Git_test_v0.1
    * master
    ```

13. Let's switch to the branch that we have created,

    ```bash
    $ git checkout Git_test_v0.1
    Switched to branch 'Git_test_v0.1'
    ```

14. Now our git branch has been changed. Then I have made some changes in the test.c and also added a new file as `new.c`. If we check the status,

    ```bash
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
    ```

15. Now we will add all the changes and commit them,

    ```bash
    $ git add --all

    $ git status
    On branch Git_test_v0.1
    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
        new file:   new.c
        modified:   test.c

    $ git commit -m "Added a new file in the source"
    [Git_test_v0.1 077fe3d] Added a new file in the source.
    2 files changed, 8 insertions(+), 1 deletion(-)
    create mode 100644 new.c

    $ git status 
    On branch Git_test_v0.1
    nothing to commit, working tree clean
    ```

16. If we switch between the branches and check out the master branch, we can see that in the master branch, there is no such file as `new.c`.

    ```bash
    $ ls
    new.c  test.c
    $ git checkout master
    $ ls
    test.c
    ```

17. Let's suppose I want to fix something, but I don't want to mess with the master branch or `Git_test_v0.1`. Then we will create a new branch called `emergency-fix`. 

    ```bash
    $ git branch emergency-fix
    $ git checkout emergency-fix
    ```

    Or we can make a new branch and checkout at the same time,

    ```bash
    $ git checkout -b emergency-fix
    $ nano test.c 
    ```

    -> Change something in that file

    ```bash
    $ git status
    On branch emergency-fix
    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   test.c

    no changes added to commit (use "git add" and/or "git commit -a")

    $ git add test.c

    $ git commit -m "updated test.c for a small bug fix"
    ```

18. Now we can merge the branches

    ```bash
    $ git checkout master
    ```

19. Now merge the current branch with the `emergency-fix` branch

    ```bash
    $ git merge emergency-fix
    Updating eaaf6ce..42734d3
    Fast-forward
     test.c | 3 ++-
     1 file changed, 2 insertions(+), 1 deletion(-)
    ```

20. As the master and `emergency-fix` branches are the same, we can now delete the `emergency-fix` branch

    ```bash
    $ git branch -d emergency-fix
    Deleted branch emergency-fix (was 42734d3).
    ```

21. For the Merge Conflict concept, we will switch to the `Git_test_v0.1` and make changes in the `test.c`, then we will add and commit it,

    ```bash
    $ git checkout Git_test_v0.1

    $ git add --all

    $ git commit -m "added a new print line in the test.c"
    ```

22. Now we will check out the master branch and merge `Git_test_v0.1`, but what will happen to the recent change that we made in the master branch? The merge will fail as there is a conflict between the versions for `test.c`. We can check the same in the status as well,

    ```bash
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
    ```

23. Now it is confirmed that there is a conflict between the versions of the `test.c` file. Open the file and make changes to resolve the conflict of the versions, then we will add the file and check the status,

    ```bash
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

    $ git add

 --all

    $ git status
    On branch master
    All conflicts fixed but you are still merging.
    (use "git commit" to conclude merge)

    Changes to be committed:
        new file:   new.c
        modified:   test.c

    $ git commit -m "Fixed the test.c conflicts"
    ```

