# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!pause"))
# async def pause_playing(_, m: Message):
#     mp.group_call.pause_playout()
#     await mp.update_start_time(reset=True)
#     reply = await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} paused",
#                                quote=False)
#     mp.msg['pause'] = reply
#     await m.delete()


# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!resume"))
# async def resume_playing(_, m: Message):
#     mp.group_call.resume_playout()
#     reply = await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} resumed",
#                                quote=False)
#     if mp.msg.get('pause') is not None:
#         await mp.msg['pause'].delete()
#     await m.delete()
#     await _delay_delete_messages((reply,), DELETE_DELAY)