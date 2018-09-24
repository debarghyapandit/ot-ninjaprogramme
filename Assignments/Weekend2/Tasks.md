# Weekend Summary Saturday

* Git
```
                  What is it?
                  Why we required it?
                  Centralised v/s distrubuted
                  Git user areas:
                                    Workspace Area
                                    Staging Area
                                    Local Repo
                                    Remote(Centralized) Repo
                  Git commands:
                                    git init
                                    Do some work
                                    git add
                                    git commit
                                    git push
                                    git config (local and global config): Use of config
                                    git clone
                                    git pull
                                    git remote add origin git@github.com:username/new_repo
                   Git Branching:
                                    Why we require Branching ?, Need for branching
                                    Types of ENV : Dev ENV, QA ENV, UAT/PrePROD ENV, PROD ENV
                                    Branching Types: master
                                                     Release
                                                     feature
                                                     Bug fix branch
                                    When to use Taging and when to use Branching ?
                   Git Merge:
                                    No Merge
                                    Fast Forward Merge
                                    Merge without conflict
                                    Merge with conflict
```                                    

# Weekend Summary Sunday

* Maven
```
            Build Tool:
                              Why we need it?
                              What is it?
            Maven Build Tool:
                              mvn Build Life cycle
                              mvn clean
                              mvn compile
                              mvn test
                              mvn package
                              POM.xml file
            Maven repo:       
                              Local repository ~/.m2
                              Central/Remote repository
            Other build Tools:
                              Gradle      
                              
```

* Explain your understanding what is the difference between Jenkins SCM option or checking out code using git clone command?
```
     In git clone command:
            * it's just like normal shell command executed using execute shell option  in Jenkins.
            * Can not see the changes
            * No revision number is maintained.
      In Jenkins SCM Option:
            * We can use various other features and opions available in SCM plugin.
            * We can see the changes, and can use vaious git functionalities
            * Each build via scm generates a Revision Number; we can rollback to perevious build if the build fails.
            * can configure SCM Polling and webhook trigers.
```

* Get code as soon as someone commits his/her code in repository
```
      solution one -- via scm polling
      solution two -- via webhook triger
```

* Create a Jenkins job that will take a Git URL & a branch name as an input and clone the code and print the name of file having maximum size
```
##Approach
cd $WORKSPACE
git checkout $Branch
- command 1
  du -a $WORKSPACE | sort -n -r | head -n 1 ##Will include hidden files also
- command 2
  find . -type f -printf "%s %p\n" | sort -nr | head -1|numfmt --to=si ##will include hidden files also
- command 3
  find . -type f -not -path '*/\.*' -printf "%s %p\n" | sort -nr | head -1|numfmt --to=si
  output : 94K ./EmployeeAutomation/test-output/jquery-1.7.1.min.js
```

* Create a Jenkins job that will checkout the code from: https://github.com/OpsTree/ContinuousIntegration, If there is a new change it should invoke other jenkins job that will compile the code. If code compilation is successful next job should get triggered that will generate the artefact. Finally a mail should be sent to you with the name of artefact
```
##Approach
    job 1 -- for git checkout
    job 2 -- for compile the code
    job 3 -- for artifact generation(packaging) and sending mail
Note: all the 3 jobs should have same workspace using external worksapce feature in jenkins

- Also can we have a visualisation of same?
  # Visualization can be done by using Build pipline plugin of jenkins.
```
  
* Create a jenkins job that will take username & password and a SQl file as an input. Then it should execute that SQL file in the database.
```
     - Create a parameterized job that Will accept:
                    username
                    password
                    and a sql file as input
        then execute the SQL file in database : mysql -u $username -p$password < filename.sql
        
```

* 6. There is a company which has multiple projects, and they are very strict about there daily syncup meetings. They have introduced a fine system where if a person/person(s) get's late in joining the meeting they have to treat everyone with a cup of coffee. The contribution of people will vary depending on by how much time they were late. Please come with a solution for same.

