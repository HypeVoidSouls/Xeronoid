from Ӽɛʀօռօɨɖ import *
from pyrogram.types import Message
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from Importing import *

@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
& filters.command(
"off",
prefixes=DYNO_COMMAND))                   
async def leave_voice_chat(_, ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    ʜᴀᴅᴇ.playlist.clear()
    voice_chatting.input_filename = ''
    await voice_chatting.stop()
    await ryui.delete()    