from http_async_client import async_client_factory
import asyncio

key = "sid=@GV5dqupT5P@"

#url1 = "192.168.1.11/config/xmlapi/statechange.cgi?ise_id=1269&new_value=false&sid=@GV5dqupT5P@"
#url1 = "192.168.1.11"
#url1=
url1 = "192.168.1.11/pages/index.htm?" + key
#url1 =   "192.168.1.11/addons/xmlapi/state.cgi?datapoint_id=1645&" + key
print(url1)
client = async_client_factory(host=url1, protocol="http")

async def get_my_resource():
    response = await client().get()
    print(response.text)

asyncio.run(get_my_resource())