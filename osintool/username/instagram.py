import json

from aiohttp import ClientSession


async def find(session: ClientSession, username: str) -> str | None:
  profile_url = f"https://www.instagram.com/{username}"

  async with session.get(profile_url) as res:
    text = await res.text()
    data = json.loads(text.split("ScheduledApplyEach,")[1].split(");")[0])

    return profile_url if "id" in data["require"][2][3][3]["rootView"]["props"] else None
