from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.pebi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Pebi Olla🤗`")
    sleep(3)
    await typew.edit("16 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Yogyakarta, Salam Kenal Ya NGENTOT!!!`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.piki(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Kalo Piki itu Ganteng Banget:)`")
    sleep(1)
    await typew.edit("`Love U Mwaaa😚`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "pebi":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pebi`\
    \n↳ : Perkenalan Diri"
    "piki":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.piki`\
    \n↳ : Perkenalan Diri"
    "semangat":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
    \n↳ : gabutan aja ye"
    }
)
