"""
Update host tags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags

body = HostTags(
    host="test.host",
    tags=[
        "environment:production",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    response = api_instance.update_host_tags(host_name="host_name", body=body)

    print(response)
