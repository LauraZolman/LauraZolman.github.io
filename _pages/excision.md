---
permalink: /excision/
title: "Excision"
---

{% include figure image_path="/assets/images/excision.png" alt="Excision" caption="" %}

I don't remember where the idea for Excision came from. But it was at least partially inspired by [the hardest riddle available on the internet](http://notpron.org/notpron/). What I wanted to do was build a game where I hid things on the internet and people would have to find them. Hopefully they would learn something about computers and biology while they were playing. I came up with a few puzzles, then built a pretty extensive story around that skeleton. If you really want to do a deep dive for some reason, [here's a gist](https://gist.github.com/Jessime/5fbf76e9437fdaa5d182) of all the text and a lot of the puzzles that I saved after the game. I don't recommend spending much time trying to parse what's going on in that gist.

The game was set up as a competition. As a small promotion, I offered $50 dollars to the first person who could email me the final clue. Here's how I described the structure of the game at the time:

1. Read the story. It provides important context for the stage, and it's entertaining!
2. Work through the puzzle at that stage.
3. Uncover the password necessary to unlock the next stage/clue.
4. Find the location of the next stage/clue.
5. Repeat.

Sadly, I made the first level (finding a comment in the source code of some html) a little too hard for my audience, and a lot of people gave up on the first level. That was a great learning experience for me, because I had previously been pretty confident that I was doing a good job judging the difficulty level of the game. In an unexpected twist, it was a random high school student, Ankur Sundara from New Jersey, who ended up winning the game.

I'd intentionally set things up so that players would have to hit spots that I could monitor approximately every 3rd level, so I could keep an eye on the progress of the competition. How it actually played out was that only a handful of people made it past the second level, and were taking their sweet time on the third and fourth levels. All of those people were friends of mine. Then all of the sudden somebody is on level five. I don't remember the exact timeline of events, but I do distinctly remember waking up one morning and realizing that Ankur had clearly spent a majority of the night playing Excision. I think he might have literally pulled an all nighter. He ended up getting his prize a day or two later.

For my own entertainment (because I don't remember many of the levels) I'm going to summarize them here:

## Base Camp
1. The players get the rules and I introduce the idea that they're playing as an Agent.
2. The first clue was at the bottom of the of the introductory blog post. It was some underlined keywords and misplaced capitalization they had to piece together. There are also a bunch of encrypted links at the bottom, but those have to be ignored (they're for later).
3. There wasn't a password for this stage
4. The clue pointed users to the source code of another blog post.

## Source code of A Prelude (Part 1)¶
1. Agent is about to graduate from the Academy, but need to pass one last Biology exam.
2. I provide a link to the stem cell wikipedia page, and the player has to "link hop" from one wikipedia page to the next based on some flashcard style questions.
3. The answer to the last card is "chromatin", which is the password to the next level.
4. The last clue is also a play-on-words with another post on the blog that only contains a single sentence. It's also an encrypted link; clicking it prompts for the "chromatin" password.

## Encryptions Post
1. Agent graduates and starts working for someone nicknamed The Congressman. Agent also meets another employee Anita, who needs you to analyze some cell images and email her the results.
2. Players have to do some busy work to get a clue to mess with the brightness and contrast of the image data.
3. DANGEROUS is embedded in the image.
4. Players don't really have anywhere to go at this point, other than to fallback to the links at the bottom of the Base Camp post. One of them asks, "What is he?" (and decrypts to a message).

## Base Camp- What is he?
1. Agent is worried about Anita's message, but has to help someone at the Justice Center with some sequencing data.
2. The message includes a Google Drive link, but the word "WRONG" has been inserted in. Players have to remove that word.
3. No password here.
4. Just go to the Drive folder.

## Justice Center
1. Agent has to help someone with a corrupted file, and then is told to check out a nearby bookstore.
2. The file is a fasta string with some incorrect characters. Players just have to remove those characters in order.
3. The incorrect characters are "ZIP.FILE.FLIP.FLOP.PIE.OIL". The words "PIE OIL" are the password (the other letters are used figure out the correct "book" in the bookstore).
4. The bookstore is another Drive folder that contains a ton of randomly named zip files, most of which are filled with random strings. The one named FLIP FLOP.zip is the next location.

## Bookstore
1. Agent gets a call that a murder has occurred on a flight The Congressman is on. Anita has DNA from the scene and DNA samples from some suspects.
2. "Analyzing" the DNA is just finding which suspect sample the DNA fragment is in, then matching the sample to the suspect name. Players are encouraged to slightly modify and use a pre-written python script, but any notepad app will also work.
3. The password is "Herman", the suspect whose
3. There's no location for this level. Players should go back to Base Camp and click "Who was it?"


## Base Camp- Who was it?
1. Agent realizes they know Herman, and they were buddies at the Academy, until Herman dropped out. Agent decides to keep investigating to prove Herman's innocence.
2. Players have to track down a specific comment on a genomics video.
3. There's no password here.
4. The comment includes a link to another Drive folder.


## Herman's House
1. Agent finds a distressed note from Herman indicating there's more to this murder. There's also an encoded message.
2. The encoded string is a nucleotide sequence that needs to be converted to a protein sequence.
3. The decoded protein sequence explicitly says that the password is NEWCANDY
4. There's another locked zip folder called WorkRoom.zip within the Drive folder.

## Work Room
1. There are a bunch of humanoid robots sitting around the work room. Agent tries to interrogate them.
2. The player is given some python code, most of which is a HermanBot_v2 class. The class has some simple parameters the player has to fiddle with (like set `bot.on=True`), then they can ask the bot any question that includes the words "Herman" and "where".
3. The bots will return the string "hermanisincanadastreetpierre".
4. Again, there's no location, so the play heads back to Base Camp and click "What COUNTRY \*space\* STREET ?" and enter CANADA PIERRE

## Canada, Pierre
1. Agent ends up at a deserted summer cabin in rural Canada, and finds a trap door leading to a secret basement. After breaking the locks on a steel door in the basement, Agent discovers a high-tech, underground bunker. Agent makes their way past a receptionist and sneaks around a number of laboratories trying to find an alternative way out. While wondering around, Agent has to "defeat" a couple of workers in the lab, and learns about a company called "Gene Corp.". Eventually Agent stumbles their way into a room called "Experimental Travel", and has to run some software to program an autonomous pod to take them back to The Congressman. There's no sign of Herman.
2. This level is pretty long and includes a bunch of sub-puzzles. Most of them follow a similar theme of giving players a probability question and some pre-written python code to calculate the answer. In each case, while individual lines are correct, the lines are out of order for some reason. Players have to arrange the code into the correct answer.
3. Each script prints a probability, which is the password to the next sub-puzzle. The final sub-puzzle gives some story and basically tells the player the next password is GENE CORPORATION.
4. Each of the sub-puzzles are locked zip folders within Drive folders. At the end, the player goes to a coffee shop (for which the location is hidden in a comment containing a short-link on another blogpost)

## Coffee Shop
This is more of an interlude than a level. There's a bit of narration where The Congressman says he'll monitor the situation.

## Months later
1. Agent is now Special Agent, but still hasn't found Herman (only another lab run by him). Special Agent is spending time investigating a GENE CORP subsidiary called Life/Better LLC who is testing a protein used as a prenatal brain supplement. Anita realizes that the protein is tied to Herman's other lab, and asks for help following up.
2. Players have to dig into the EXIF metadata of an image to get a geolocation.
3. The password is coordinates "43.621965 13.508345"
4. Players go back to Base Camp one last time and click "Where? xx.xxxxxx \*space\* xx.xxxxxx"

## Base Camp- Where? xx.xxxxxx *space* xx.xxxxxx?
Another "interlude". Agent, Anita, and The Congressman decide to send Agent to the coordinates, located in Ancona, Italy. Herman is certainly there.

## Ancona, Italy
1. Like the Canada level, this is a large, multi-part set of puzzles, since it's the final level. Over the course of the level, Agent finds a supercomputer and a way to have a conversation with it. The supercomputer is running an AI named Arius, who reveals that "Herman" was in fact an android. Herman is normally one of the embodiments of Arius. Arius was using Herman to investigate Gene Corp, and suspects that Herman was discovered and hacked. Thus, it was likely Gene Corp who attempted to murder The Congressman. At the end of the conversation, Arius encourages Agent to continue investigate Gene Corp on its behalf and declares that it's objective has been satisfied and it is going to self-terminate.
2. Again, there are multiple puzzles on this level. The primary one is downloading and running the "Arius" program, then navigating though the "reveal" conversation. Players need to "connect" to Arius first which requires them to enter in specs for their computers (Note: this is program is running locally on their computers and not doing any weird data collection). Players then have to ask enough relevant question to Arius to trigger the end of the conversation and the final reveals.
3. There's no password for this level
4. Arius gives the final "location" after its termination.

## Conclusion
1. Agent returns home to find that their friend The Congressman has been murdered, and that The Congressman has appointed Agent to replace him. Later that same evening, Agent gets a call from the vet saying that Agent's Golden Retriever is going to have puppies.
2. Players have to send me an email solving a Punnett square problem about the likelihood of different phenotypes for the puppies.
3. The final email should be:

> Wavy and golden: 9/16
> Wavy and blond: 3/16
> Straight and golden: 3/16
> Straight and blond: 1/16

jqhwvan/moc.lruynit//:ptth

😉
