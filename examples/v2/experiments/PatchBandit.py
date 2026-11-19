"""
Update bandit returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType
from datadog_api_client.v2.model.experiments_bandit_variant_input_v2 import ExperimentsBanditVariantInputV2
from datadog_api_client.v2.model.experiments_patch_bandit_v2_request import ExperimentsPatchBanditV2Request
from datadog_api_client.v2.model.experiments_patch_bandit_v2_request_data import ExperimentsPatchBanditV2RequestData
from datadog_api_client.v2.model.experiments_patch_bandit_v2_request_data_attributes import (
    ExperimentsPatchBanditV2RequestDataAttributes,
)

# there is a valid "bandit" in the system
BANDIT_DATA_ID = environ["BANDIT_DATA_ID"]

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID"]
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID"]

body = ExperimentsPatchBanditV2Request(
    data=ExperimentsPatchBanditV2RequestData(
        type=ExperimentsBanditV2DTODataType.BANDITS,
        id=BANDIT_DATA_ID,
        attributes=ExperimentsPatchBanditV2RequestDataAttributes(
            name="bandit-14bb9543f523edde-renamed",
            variants=[
                ExperimentsBanditVariantInputV2(
                    feature_flag_variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID,
                ),
                ExperimentsBanditVariantInputV2(
                    feature_flag_variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID,
                    is_fallback=True,
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_bandit"] = True
configuration.unstable_operations["patch_bandit"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.patch_bandit(bandit_id=BANDIT_DATA_ID, body=body)

    print(response)
