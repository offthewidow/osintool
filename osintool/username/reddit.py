from aiohttp import ClientSession


async def find(session: ClientSession, username: str) -> str | None:
  profile_url = f"https://www.reddit.com/user/{username}"
  async with session.get(f"{profile_url}/about.json") as res:
    return profile_url if res.status == 200 else None
