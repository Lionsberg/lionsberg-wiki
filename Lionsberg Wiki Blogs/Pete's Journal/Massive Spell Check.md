# Massive Spell Check

_a post in [[Pete's Journal]]_

by [[Peter Kaminski]], 2022-07-26

In a bit of productive procrastination, I experimented with some bulk spell correction.

Thanks to our prolific contributor [[Jordan Nicholas Sukut]], we have a lot of text, with an attendant number of typos that can be found and fixed.

Today, I tried using `aspell` and some not-really-automation to fix about 30 typos in as many files.  (On a Mac, `aspell` can be installed with Homebrew.)

I hope this helps prototype something that might ultimately be packaged more nicely and productively.

## Methodology

First, grab all the potential misspellings with `aspell`:

```shell
(find . -name '*.md' -exec cat "{}" \;) | aspell list | sort -dfu >/tmp/tmp.txt
```

Second, create a "fix" file, with a typo and then the corrected word, per line.  I only did the "A" words, and only words that seemed like they would surely want to be fixed, nothing that needed further manual inspection.

After trying a couple of things, what I did was to use Emacs to create two words per line (both were the original word), then loaded the file in TextEdit, where it was easier (not quite easy) to correct the right-hand word.  Interestingly, some of the typo'ed words did not get flagged by the Mac spell correction.

This part was a little manually intensive, but I'm not sure of a great way around it.  (Also to note, `aspell` is usually use in interactive mode, one file at a time.  That would have been another way to do it, but not automated enough for my taste.)

Here's the result:

```
aboslute absolute
abraction abstraction
abstarction abstraction
abudnance abundance
abyssmal abysmal
accomodate accommodate
accompish accomplish
Acquition Acquisition
Actioin Action
activites activities
adapated adapted
addresing addressing
adminsitering administering
Adminsitration Administration
Adminsitrative Administrative
advanding advancing
aggree agree
Agrement Agreement
alignement alignment
appartent apparent
apporach approach
approachs approaches
architypical archetypical
ariticulated articulated
artciulate articulate
assigments assignments
assoiated associated
attemtping attempting
Attendence Attendance
audaceous audacious
autonmous autonomous
autonomouosly autonomously
avaiable available
```

I then transformed the text file into the following shell script. We could write something that handles this much better, but as a hack:

```shell
find . -name '*.md' -exec perl -p -i -e 's/aboslute/absolute/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/abraction/abstraction/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/abstarction/abstraction/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/abudnance/abundance/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/abyssmal/abysmal/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/accomodate/accommodate/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/accompish/accomplish/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Acquition/Acquisition/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Actioin/Action/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/activites/activities/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/adapated/adapted/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/addresing/addressing/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/adminsitering/administering/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Adminsitration/Administration/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Adminsitrative/Administrative/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/advanding/advancing/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/aggree/agree/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Agrement/Agreement/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/alignement/alignment/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/appartent/apparent/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/apporach/approach/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/approachs/approaches/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/architypical/archetypical/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/ariticulated/articulated/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/artciulate/articulate/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/assigments/assignments/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/assoiated/associated/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/attemtping/attempting/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/Attendence/Attendance/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/audaceous/audacious/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/autonmous/autonomous/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/autonomouosly/autonomously/g' "{}" \;
find . -name '*.md' -exec perl -p -i -e 's/avaiable/available/g' "{}" \;
```

You might observe that this is massively inefficient, and indeed, even on my MacBook M1, it took forever to run, and I'm sure several of the internal hamsters-on-wheels went to a better place before it was finished.  Anywho...

After skimming through the changes with `git diff`, it all looked good.  I noted the Perl one-liner had the effect of removing whitespace at the end of lines; I think that was okay, so I didn't do anything to handle that.

Here is the resulting commit: [semi-automated spelling correction experiment](https://github.com/Lionsberg/lionsberg-wiki/commit/795c0484f441791dd73b7647b9b41a9de01922dd).

### Conclusion

I believe we can adapt the work above to create a workflow that helps automate some of the work of spelling correction, perhaps as an Obsidian plugin, perhaps as a Python script, etc.

Questions/observations:

- would it make sense to keep and update a script such as the above (with fairly unambiguous corrections), and run it regularly?  or regenerate it one-off once in a while?
- somewhere, we have some [[lorem ipsum]] in the pages, which generated noise as I was trying to find which words to correct.
- it would be nice to generate a whitelist dictionary, of known good words, e.g., "Netlify".
