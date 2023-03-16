import asyncio

from aiohttp import ClientSession
from colorama import Fore

from . import reddit, twitter


async def __await_and_print(website_name, coroutine):
  profile_url = await coroutine
  if profile_url:
    print(f"[{Fore.GREEN}+{Fore.RESET}] {website_name}: {profile_url}")

async def find_and_print_all(session: ClientSession, username: str):
  print(f"[{Fore.YELLOW}*{Fore.RESET}] Searching for username {Fore.YELLOW}{username}{Fore.RESET}")
  await asyncio.gather(
    __await_and_print("Reddit", reddit.find(session, username)),
    __await_and_print("Twitter", twitter.find(session, username)),
  )
