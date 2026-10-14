"""
List feature flags combines exact keys tags search types creators and IDs
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.value_type import ValueType

# there is a valid "feature_flag_list_a" in the system
FEATURE_FLAG_LIST_A_DATA_ATTRIBUTES_CREATED_BY = environ["FEATURE_FLAG_LIST_A_DATA_ATTRIBUTES_CREATED_BY"]
FEATURE_FLAG_LIST_A_DATA_ID = environ["FEATURE_FLAG_LIST_A_DATA_ID"]

# there is a valid "feature_flag_list_b" in the system
FEATURE_FLAG_LIST_B_DATA_ID = environ["FEATURE_FLAG_LIST_B_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        key="list-a-example-feature-flag",
        is_archived=False,
        tags=[
            "list-test:example-feature-flag",
            "color:blue",
        ],
        search="LIST-A-example-feature-flag",
        value_type=[
            ValueType.BOOLEAN,
            ValueType.STRING,
        ],
        created_by=[
            FEATURE_FLAG_LIST_A_DATA_ATTRIBUTES_CREATED_BY,
        ],
        flag_ids=[
            FEATURE_FLAG_LIST_A_DATA_ID,
            FEATURE_FLAG_LIST_B_DATA_ID,
        ],
    )

    print(response)
