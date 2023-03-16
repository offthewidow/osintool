from aiohttp import ClientSession


async def find(session: ClientSession, username: str) -> str | None:
  profile_url = f"https://github.com/{username}"
  async with session.get(profile_url) as res:
    return profile_url if res.status == 200 else None