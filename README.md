# Myrino
### Myrino is an api-based library for Rubino messengers

## Documents 
Documents will be added soon.


## Examples
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
