"""
Mute a host returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.model.host_mute_settings import HostMuteSettings

body = HostMuteSettings(
    end=1579098130,
    message="Muting this host for a test!",
    override=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.mute_host(host_name="host_name", body=body)

    print(response)
