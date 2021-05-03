# TAMU Problems 2021
All of our problems in one place!

## Contributing Guidelines for TAMUctf-probs

### Repository Setup

Your repository should have two remotes.  The particular name of either doesn't matter but I like leaving your team repository as origin (and default) and adding the main repository as a secondary remote so there is a little more barrier and you don't accidentally push something you don't intend.  

```text
git@github.tamu.edu:tamuctf-blue/tamuctf-probs-2021.git
cd tamuctf-probs-2021
git remote add tamuctf-dev git@github.tamu.edu:tamuctf-dev/tamuctf-probs-2021.git
```

### Creating a Challenge

Each challenge should be on its own branch.  Each challenge should also have a readme, example provided below. 

```text
# challenge name

## Description

List description as the challenger should see it and mention any provided files

## Solution

Writeup to be written by whoever solves/reviews it

```
At this stage of challenge development you should only push it to your team repository.  

### Submitting a Challenge

You can't make a pull request on the main repository without a branch to merge in -- since we will not be pushing challenge code until after it has been reviewed I think the easiest thing to do is just make an issue and mention that its ready for review.  This issue should provide everything a challenger needs to solve the challenge and also only stuff that the contestant is supposed to have.  

Example:
```
# leaky

## Description

Attack this binary and get the flag!

```nc 34.123.3.89 8374```

[leaky.zip](https://github.tamu.edu/tamuctf-dev/tamuctf-probs-2021/files/934/leaky.zip)
```
