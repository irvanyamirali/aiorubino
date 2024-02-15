# Myrino
### Myrino is an api-based library for Rubino messengers


# Install
```bash
pip install -U myrino
```

## Start
```python
from myrino import Client
import asyncio

client = Client('rnd', 10)
async def main():
    result = await client.get_my_profile_info()
    print(result)
    

if __name__ == '__main__':
    asyncio.run(main())
```


## Examples
- [Go to the examples directory](https://github.com/metect/myrino/tree/main/docs)

