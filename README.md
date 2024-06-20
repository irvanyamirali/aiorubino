# AIORubino
aiorubino is asynchronous Rubino API framework in Python

# Install
```bash
pip install -U aiorubino
```

# Start
```python
from aiorubino import Client
import asyncio

client = Client("auth")

async def main():
    result = await client.get_my_profile_info()
    print(result)
    

if __name__ == '__main__':
    asyncio.run(main())
```

## Examples
- [Go to the examples directory](https://github.com/irvanyamirali/myrino/tree/main/examples)
