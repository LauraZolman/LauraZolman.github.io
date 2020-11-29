---
title: "ChuckSort"
last_modified_at: 2020-09-27
categories:
  - Blog
tags:
  - Programming
  - Education
---

> The internet is pretty cool; right now I'm watching some Harvard lectures on advanced algorithms. This one's about sorting.

\- Me

> What's an algorithm?

\- Mom and Dad

I'm hanging out with my parents for the week. Anytime I'm home I try to spend a little time giving my parents a better sense of what I do. Neither have much background in science or engineering, but they always indulge me and ask to hear about what I'm working on.

Clearly explaining complicated things to people who don't have a background is an invaluable skill. Anytime there's a chance to practice, take advantage of it.

We ended up on the topic of algorithms, so I decided to play a game. I asked Dad how to describe the steps needed to sort a list of randomly generated integers from smallest to largest. That didn't get much of a response besides "Well, study the numbers, then put them in order."

I decided we needed a visual aid. We cut up and numbered some paper square and manually went through the process of creating a random array and then sorting it.

<figure>
	<a href="https://i.imgur.com/f3FobQr.png"><img src="https://i.imgur.com/f3FobQr.png"></a>
</figure>

The first couple iterations of sorting the numbers didn't make much progress towards describing any sort of algorithm. It sort of just _happened_. There were some vague mutterings about "this goes over here" and "then the 6 can move here..." and the like.

Eventually, I took over and said he had to tell me what to do instead. I would write down the instructions as we went along. That also didn't go perfectly. After a couple of tries, a lot of clarifying questions, and a hint or two, however, I was able to write down the following steps:

1. Find min.
1. Find max.
1. Decide bin size.
1. Move min to far left.
1. Look right (within bin) for num not in bin.
1. Move num to correct bin.
1. Within bin, find number just smaller than num, place num in from of smaller number.
1. If any num shouldn't be in bin, put it in the right bin. (Repeat previous 3 steps).
1. If all nums in bin are in valid bin, quickly sort "nearby".
1. If nearby is sorted, record max value.
1. Do comparison to the right, until you find unsorted num.
1. Check for nums in wrong bin.
1. Either go back to putting nums in right bin, or go back to quickly sorting "nearby".
1. Check if array is sorted.

By this point, both parents were sufficiently through with the conversation. But I had to take it one step further and turn this algorithm into working code.

After a few quick sessions ChuckSort was born. You can check out the source code on GitHub for more details.

[https://github.com/Jessime/ChuckSort](https://github.com/Jessime/ChuckSort)

You'll notice that the algorithm in `chuck_sort.py` isn't exactly the same as what's above. It morphed a bit over the 3-4 short sessions it took me to write it up. I'm fine with that. The essence of what happened with those little paper squares is still captured in this repo. The fun bit is that the code actually works. Here's the algorithm sorting 1 through 100:

<figure>
	<a href="https://i.imgur.com/jcf92Mo.gif"><img src="https://i.imgur.com/jcf92Mo.gif"></a>
</figure>

This exercise reminded me of two things.

1. Learning to think algorithmically is difficult and not something humans do intuitively. In some sense, this is great news for beginner programmers who often feel a lot of frustration about the difficulty of programming and their lack of progress. It's normal! Becoming a good programmer is so much more than learning the syntax of a language. It's about expression. It's about taking hold of thoughts in your head and clarifying those thoughts until they can ultimately be expressed in binary. When you're programming in the context of something like bioinformatics, it's also about capturing real-world phenomena in some accurate way.
2. Even if _you're_ used to thinking programmatically, it's hard to capture what someone's doing to process some task. Even when the process is as simple as sorting 20 numbers, I was never able to fully capture what Dad was doing to sort the numbers. I'm no psychologist, but it feels like this observation has interesting implications for assuming the intent or rationale of other humans. Given the political climate (there's been a lot of politics this week), I find it entertaining how often we say things like, "He obviously did this because he wanted to...", or "All of those people think that...". It's absurd. I can't even tell you why my own father sorted 20 numbers the way he did. How are you going to assert the intentions of some random person you've never met on some complex political topic? I digress...

tl;dr: Formalizing the world into code is _tricky_, but fun!
