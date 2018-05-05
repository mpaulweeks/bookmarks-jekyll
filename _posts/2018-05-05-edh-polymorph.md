---
layout: post_mtg_building
title: EDH | Building Polymorph
type: post
category: mtg
isLive: true
permalink: /edh-polymorph
---

Building a deck around <auto-card>Polymorph</auto-card> has always appealed to me. When built correctly, it turns a bad removal spell into <auto-card>Tinker</auto-card>.

<div class="center">
  <auto-card-image>Tinker</auto-card-image>
  <auto-card-image>Polymorph</auto-card-image>
</div>

The basic idea is this: you run a deck where the only creatures are expensive and powerful. Then, you use cards that generate tokens or "animate" themselves to get a Polymorph target.

<div class="center">
  <auto-card-image>Chatter of the Squirrel</auto-card-image>
  <auto-card-image>Guardian Idol</auto-card-image>
  <auto-card-image>Spawning Pool</auto-card-image>
</div>

This way, you guarantee turning a cheap creature into an expensive one! This general strategy has appeared in Standard from <a href="https://mtg.gamepedia.com/Standard_Polymorph_deck">time to time</a>.

<auto-card-list
  preview
  name="Polymorph - Tim Sussino - Pro Tour San Diego 2010"
  src="decks/20180505_polymorph_standard.dec"
></auto-card-list>

## Bringing it to EDH

When I'm trying to bring a "combo" strategy to EDH, my number one priority is redundancy. You need to line up two effects, in this case Polymorph and a "creature". This can be difficult in a 100 card, singleton format.

In other decks, I often use the Commander as a reliable source of one of those effect. In my MaroSpeaker deck, I need two things: "hand-size matters" creatures + draw spells that check power. Together, they double my hand size! Given the larger number of <auto-card>Maro</auto-card> cards printed vs just a few <auto-card>Soul's Majesty</auto-card> clones, it makes sense to rely on <auto-card>Prime Speaker Zegana</auto-card>.

<div class="center">
  <auto-card-image>Prime Speaker Zegana</auto-card-image>
  <auto-card-image>Maro</auto-card-image>
</div>

Okay, so what Commander can give us a reliable Polymorph? Why <auto-card name="Jalira, Master Polymorphist">Jalira</auto-card> of course!

<div class="center">
  <auto-card-image>Jalira, Master Polymorphist</auto-card-image>
</div>

Except no, she's awful. Jalira has a ton of problems:

1. She restricts you to mono blue
2. Token options aren't great in mono blue, so you have to work harder to get stuff to Polymorph
3. She can never cheat in Legendary Creatures, which represent a lot of the big bombs
4. Unlike an ETB effect, Jalira is not a guaranteed Polymorph, so your hoping she'll survive until the next turn. Solving this would require Haste, which is hard to get in mono blue
5. She's expensive. Polymorph effects costs between 4-6 mana, but she's a minimum of 7 (to play and activate), and will only get more expensive

We need to flip our assumption. Rather than using the Commander for a reliable Polymorph, what if instead it was a reliable target?

## Polymorph Redundancy

First we need to make sure we can reliable get a Polymorph effect out of the 99. As far as the straightforward "kill a creature, get a bigger creature" card, we have a decent array of Polymorph options just in Blue.

<div class="center">
  <auto-card-image>Polymorph</auto-card-image>
  <auto-card-image>Mass Polymorph</auto-card-image>
  <auto-card-image>Synthetic Destiny</auto-card-image>
  <auto-card-image>Reweave</auto-card-image>
  <auto-card-image>Proteus Staff</auto-card-image>
</div>

Fun little note: if you activate Proteus Staff and there are no creatues left in your deck, it will put the target on the bottom, flip the whole deck, and put in back in play. But then, because you "put the rest on the bottom in any order" instead of shuffling, you can stack your entire deck. This can lead to <a href="https://tappedout.net/mtg-decks/melek-madiq/">instantly game winning combos</a> with <auto-card>Melek, Izzet Paragon</auto-card>.

If we add Green, we gain access to a few "flip untip you hit a creature" spells, which are basically Polymorph with fewer steps!

<div class="center">
  <auto-card-image>Natural Order</auto-card-image>
  <auto-card-image>Oath of Druids</auto-card-image>
  <auto-card-image>Selvala's Stampede</auto-card-image>
  <div class="img-comment">Natural Order - literally Tinker for creatures</div>
</div>

Polymorph decks often get a few big guys stuck in their hand, so <auto-card>Selvala's Stampede</auto-card> ends up does double-duty.

Even Red has a few oddballs.

<div class="center">
  <auto-card-image>Divergent Transformations</auto-card-image>
  <auto-card-image>Shifting Shadow</auto-card-image>
  <auto-card-image>Indomitable Creativity</auto-card-image>
</div>

Divergent Transformations is really strong, but the others have serious downsides.

Shifting Shadow is hurt by waiting for upkeep, as well as killing your shiny new creature after a turn.

Indomitable Creativity would require building a deck without mana rocks, which is doable with Green, but a constraint nonetheless.

So where do we go from here?

## The Traditional Route

My first EDH Polymorph deck (not counting the Melek combo mentioned above) did the most sensible thing: maximize Polymorph spells and maximize cheap targets. My solution?

<div class="center">
  <auto-card-image>Derevi, Empyrial Tactician</auto-card-image>
  <div class="img-comment">you just have to convince the table you're not running Winter Orb</div>
</div>

Derevi gives us the colors for most of the Polymorph spells, as well as some really big threats. He's an always available Polymorph target for 4 mana at instant speed. His passive ability can give our big creatures Vigilance by untapped them after combat. And if our Plan B is to go wide with tokens, he's great for that too.

<auto-card-list
  preview
  name="Bant Polymorph Overrun"
  src="decks/20180505_polymorph_derevi.dec"
></auto-card-list>

You see the cards mentioned above, as well draw, removal, cards that generate lots of tokens, and a few ways to get the big guys out of my hand.

You can find the current list on my <a href="https://tappedout.net/mtg-decks/bant-polymorph-overrun/">TappedOut</a>.

## The Single Target Route

What else is left to say? Well, last year, Polymorph was showing up in online competetive EDH with the commander Baral. The basic idea is that Baral is cheap enough, and cycles your deck enough, that you get sufficient ahead via control, then end the game by Polymorphing your commander into the only creature in your deck: Emrakul, the Aeons Torn.

<div class="center">
  <auto-card-image>Baral, Chief of Compliance</auto-card-image>
  <auto-card-image>Emrakul, the Aeons Torn</auto-card-image>
  <div class="img-comment">old Emrakul has long been banned in Paper, but was legal at the time on MTGO</div>
</div>

You read more about it on <a href="https://www.mtggoldfish.com/articles/instant-deck-tech-baral-polymorph-commander">MTGGoldfish</a>. Slimming your deck down to one creature makes the strategy very consistent, and makes perfect sense when framed as making a bunch of 4-6 mana spells into viable win-cons.

## Enter Teferi

I wanted to do a similar spin, but a bit more open ended. No grabbing a giant weapon like Emrakul. No, I want a card that will put me far enough ahead to win, but feel different everytime.

Also, the problem with Baral in multiplayer is that he becomes a huge target. If everyone knows they just have to kill Baral to keep me off my win-con, I can't counterspell 3 kill spells in one turn. I needed a Commander my opponents couldn't snipe.

Thus, a match made in heaven:

<div class="center">
  <auto-card-image>Teferi, Mage of Zhalfir</auto-card-image>
  <auto-card-image>Jin-Gitaxias, Core Augur</auto-card-image>
</div>

If you flash out Teferi during the end step before your turn, then untap and immediately Polymorph, your opponent will be unable to prevent it. The only possible answers are activated abilities like <auto-card>Avatar of Woe</auto-card> and <auto-card>Crystal Shard</auto-card>, but you will see those coming a mile away.

Thus, if you are patient and wait until you have a Polymorph in hand and a safe board, you can guarantee cheating out a Jin-Gitaxias and refilling your hand with as little as 5 mana.

Added bonus for the competetive player: Teferi has a built in "one-card combo" with <auto-card>Knowledge Pool</auto-card>. With both of those cards out, your opponents will be unable to play spells from their hand (<a href="https://www.mtgsalvation.com/forums/magic-fundamentals/magic-rulings/magic-rulings-archives/289690-teferi-knowledge-pool">more details here</a>). Teferi has the same effect with <auto-card>Possiblity Storm</auto-card>, but it's out of our colors.

<div class="center">
  <auto-card-image>Knowledge Pool</auto-card-image>
  <auto-card-image>Possibility Storm</auto-card-image>
</div>

Granted, your opponents can still cast their Commanders, and you can still lose to whatever's on the table (note: this happened the first game I resolved the combo). But it's a pretty strong lock, and a convenient win-con for a deck pre-disposed to draw a lot of cards.

<auto-card-list
  preview
  name="Tef-Gitaxias"
  src="decks/20180505_polymorph_teferi.dec"
></auto-card-list>

You can find the current list on my <a href="https://tappedout.net/mtg-decks/tef-gitaxias/">TappedOut</a>.

## In Conclusion

My point to all this is that even if you have a simple strategy, like Polymorph plus little guy equals big guy, there are a lot of ways to approach it when building an EDH deck.

Until next time, happy brewing!
