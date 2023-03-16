import argparse
import asyncio

from aiohttp import ClientSession, ClientTimeout

import username


async def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("name")
  args = parser.parse_args()

  async with ClientSession(timeout=ClientTimeout(15)) as session:
    await username.find_and_print_all(session, args.name)


if __name__ == "__main__":
  asyncio.run(main())
