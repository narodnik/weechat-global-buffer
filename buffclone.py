# Drop this in .weechat/python/autoload/
import weechat

weechat.register("buffclone", "narodnik", "1.0", "GPL3",
                 "Clones messages from channel list into a single buffer",
                 "", "")
weechat.prnt("", "Hello, from python script!")

buff = weechat.buffer_new("darkfi-all", "", "", "", "")
weechat.buffer_set(buff, "title", "darkfi-all")
weechat.buffer_set(buff, "localvar_set_no_log", "1")

weechat.hook_print("", "", "", 0, "on_print", "")

def on_print(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Get channel
    channel = weechat.buffer_get_string(buffer, "name")
    if channel.startswith("darkfi."):
        channel = channel.removeprefix("darkfi.")

    # Get nick
    tags = tags.split(",")
    nicks = [tag for tag in tags if tag.startswith("nick_")]
    assert len(nicks) == 1
    nick = nicks[0].removeprefix("nick_")

    weechat.prnt(buff, f"{channel} <{nick}> {message}")
    return weechat.WEECHAT_RC_OK
