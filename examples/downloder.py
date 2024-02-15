from myrino import Client
import asyncio

post_link = ''
client = Client('rnd', 10)
async def main():
    result = await client.get_post_by_share_link(post_link)
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
