pngbot
========
pngbot is a bot designed to combine two png images so that they appear differently when expanded.  this is a "quirk" which surfaces due to the fact that most image viewers change the background color between thumbnail and fullsize view states. I've observed that it works on twitter, tumblr, and also on iphones!</br>
examples:</br>
<ul>
   <li>http://twitter.com/pngbot</li>
   <li>http://pngbot.tumblr.com</li>
</ul>
I first discovered this via twitter user @taki_bump - ex: https://twitter.com/taki_bump/status/376313959969599488/photo/1
I only got this bot working after lots of trial and error with photoshop layers and many different imagemagick options..

<b>Operation:</b> </br>
<ul>
	<li>first it will check for new mentions and download the image attachments to the working directory as png0.png and png1.png.</li>
	<li>next it will call a shell script to do the imagemagick conversion and composite commands. if the mention provides only one image, it uses default.png as the 1st image.</li>
	<li>mentions are logged to a file called mentionlog.txt in the working directory.</li> 
</ul>

<b>APIs/ Prerequisites:</b> </br>
	* Twitter (tweepy) https://github.com/tweepy/tweepy
	* Tumblr (pytumblr) https://github.com/tumblr/pytumblr (optional)
	* Python - Tested with version: 2.7.5
	* ImageMagick - Tested with version: 6.7.8.9-10
</br>

<b>Scheduling via Cron:</b> </br>
        */5 * * * * * your-username python /path-to-your-script/pngbot.py >> /path-to-your-script/pngbot.log 2>&1
<b> To Do:</b>
<ul>
	<li> get conversion and composite commands working with wand or some other imagemagick python wrapper so I don't need to use a shell script.  :)</li>
</ul>
