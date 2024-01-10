# Discord Media Forwarder

## What is it?
The Discord Media Forwarder is a Python script designed to selectively forward images, videos, or both from a source Discord channel to a destination channel. It interacts with the Discord API to automate the process of sharing media content.

## Why I Made This?
I got tired of copying and pasting the same memes to different channels. With this script, I post in one server, and it magically appears in all the other servers I've added. ;-;''

## How to Use:

### Finding AUTH-ID:
   1. Open your browser's developer tools (`F12` or `Ctrl+Shift+I`).
   2. Go to the Discord web application.
   3. In the developer tools, navigate to the `Network` tab and filter by `Fetch/XHR`.
   4. Send a message in the chat (preferably the destination channel).
   5. In the network tab, a new entry will appear. Click on it.
   6. Go to the `Headers` section, and copy the numeric value between `https://discord.com/api/v9/channels/` and `/messages`. This is your `DESTINATION_CHANNEL_ID`.
   7. Scroll down in the `Headers` section to find the "Authorization" header. Copy its value; this is your `AUTH-ID`.

### Finding #SOURCE_CHANNEL_ID:
   - To find the `SOURCE_CHANNEL_ID`, right-click on the source channel in Discord.
   - Select "Copy Channel ID."
   - Replace `#SOURCE_CHANNEL_ID` in the script with the copied ID.

**Note:** If you can't see the "Copy Channel ID" option, enable developer mode in Discord settings (`Settings > Advanced > Developer Mode`).

## Script Configuration:
1. Set the obtained AUTH-ID as the `Authorization` header in the script.
2. Replace `#SOURCE_CHANNEL_ID` and `#DESTINATION_CHANNEL_ID` with the appropriate channel IDs.
3. Run the script and follow the prompts to choose the type of media to forward.

Note: Be cautious with your AUTH-ID and channel IDs; keep them confidential to maintain security.

---

**Disclaimer:** 

This script is meant for educational purposes and personal use. Use it responsibly and in compliance with Discord's [Terms of Service](https://discord.com/terms) and [Developer Terms](https://discord.com/developers/docs/legal).


Happy meme sharing! 🚀
