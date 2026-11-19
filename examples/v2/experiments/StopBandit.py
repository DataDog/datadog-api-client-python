"""
Stop bandit returns "The bandit is stopped and serves the chosen variant." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_stop_bandit_v2_request import ExperimentsStopBanditV2Request
from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data import ExperimentsStopBanditV2RequestData
from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_attributes import (
    ExperimentsStopBanditV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_stop_bandit_v2_request_data_type import (
    ExperimentsStopBanditV2RequestDataType,
)
from uuid import UUID

body = ExperimentsStopBanditV2Request(
    data=ExperimentsStopBanditV2RequestData(
        attributes=ExperimentsStopBanditV2RequestDataAttributes(
            served_variant_key="green",
        ),
        type=ExperimentsStopBanditV2RequestDataType.STOP_BANDIT_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["stop_bandit"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.stop_bandit(bandit_id=UUID("4b1f3c2e-8d5a-4f6b-9c7e-1a2b3c4d5e6f"), body=body)
