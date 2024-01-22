# Myrino
### Myrino is an api-based library for Rubino messengers


## Examples

```python
from myrino import Client 

client = Client('YOUR-AUTH')
async def main():
    results = await client.get_my_profile_info()
    print(results)


run(main())
```

# Install
```bash
pip install myrino -U
```

### Documents on Rubika
https://rubika.ir/myrino_documents 
