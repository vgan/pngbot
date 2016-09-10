pngbot
========
pngbot is a bot designed to combine two png images in one so that they appear as each of the original images in certain situations.  This is possible due to the fact that image viewers usually change the background color between white (or some shade of white) for thumbnail to black in fullsize view states. I've observed that it works on twitter, tumblr, and also on iPhones!</br>
examples:</br>
<ul>
   <li>http://twitter.com/pngbot</li>
   <li>http://pngbot.tumblr.com</li>
</ul>
I first encountered this effect via twitter user <a href="http://twitter.com/taki_bump">@taki_bump</a></br>
ex:</br>
<a href="https://twitter.com/taki_bump/status/376313959969599488/photo/1" target="_new"><img title="taki_bump example" src="https://pbs.twimg.com/media/BTjvjYRCMAAXOYV.png:small" width="250"> </a></br>

<b>Operation:</b> </br>
<ul>
	<li>First it checks for new mentions and downloads the image attachments to the working directory as png0.png and png1.png.</li>
	<li>Next it will call the shell script to do the imagemagick conversion and composite commands. If the mention provides only one image, it uses default.png as the 1st image.</li>
	<li>Mentions are logged to a file called mentionlog.txt in the working directory.</li> 
</ul>

<b>APIs/ Prerequisites:</b> </br>
<ul>
	<li>Twitter (tweepy) https://github.com/tweepy/tweepy</li>
	<li>Tumblr (pytumblr) https://github.com/tumblr/pytumblr (if you're posting to Tumblr)</li> 
	<li>Python - Tested with version: 2.7.5</li>
	<li>ImageMagick - Tested with version: 6.7.8.9-10</li>
</ul>
