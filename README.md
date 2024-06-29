# AIORubino
aiorubino is asynchronous Rubino API library in Python

### Install and update
```bash
pip install -U aiorubino
```

### Start
```python
from aiorubino import Client

client = Client("auth")

async def main():
    result = await client.get_my_profile_info()
    print(result.name)
    

client.run(main())
```

### Contributors
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### License
aiorubino is released under the MIT License. See the bundled [LICENSE](https://github.com/irvanyamirali/aiorubino/blob/main/LICENSE) file for details.
