from aiohttp import ClientSession


async def find(session: ClientSession, username: str) -> str | None:
  async with session.get(f"https://api.twitter.com/i/users/username_available.json?username={username}") as res:
    data = await res.json()
    return f"https://twitter.com/{username}" if data["reason"] == "taken" else None
