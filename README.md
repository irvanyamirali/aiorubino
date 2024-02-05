# Myrino
### Myrino is an api-based library for Rubino messengers


## Examples

```python
from myrino import Client 
from asyncio import run

client = Client('YOUR-AUTH')
async def main():
    results = await client.get_my_profile_info()
    print(results)


if __name__ == '__main__':
    run(main())
```
### and
```python
from myrino import Client 
from asyncio import run

client = Client('YOUR-AUTH')
async def main():
    results = await client.follow('follow_id')
    print(results)


if __name__ == '__main__':
    run(main())
```
### and
```python
from myrino import Client
from asyncio import run

client = Client('your-auth')
async def main():
    result = await client.get_post_by_share_link('post-link')
    print(result)


if __name__ == '__main__':
    run(main()) 
```

# Install
```bash
pip install -U myrino
```
