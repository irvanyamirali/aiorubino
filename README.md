# AIORubino
aiorubino is asynchronous Rubino API framework in Python

### Start
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

### Install and update
```bash
pip install -U aiorubino
```

### Examples
[Visit the Examples directory](https://github.com/irvanyamirali/aiorubino/tree/main/examples)

### Contributors
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### License
aiorubino is released under the MIT License. See the bundled [LICENSE](https://github.com/irvanyamirali/aiorubino/blob/main/LICENSE) file for details.
