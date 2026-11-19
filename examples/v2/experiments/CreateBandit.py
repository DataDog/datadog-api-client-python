"""
Create bandit returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_bandit_flag_configuration_input_v2 import (
    ExperimentsBanditFlagConfigurationInputV2,
)
from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType
from datadog_api_client.v2.model.experiments_bandit_variant_input_v2 import ExperimentsBanditVariantInputV2
from datadog_api_client.v2.model.experiments_create_bandit_v2_request import ExperimentsCreateBanditV2Request
from datadog_api_client.v2.model.experiments_create_bandit_v2_request_data import ExperimentsCreateBanditV2RequestData
from datadog_api_client.v2.model.experiments_create_bandit_v2_request_data_attributes import (
    ExperimentsCreateBanditV2RequestDataAttributes,
)

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID"]
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID"]
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

# there is a valid "experiment_subject_type" in the system
EXPERIMENT_SUBJECT_TYPE_DATA_ID = environ["EXPERIMENT_SUBJECT_TYPE_DATA_ID"]

body = ExperimentsCreateBanditV2Request(
    data=ExperimentsCreateBanditV2RequestData(
        type=ExperimentsBanditV2DTODataType.BANDITS,
        attributes=ExperimentsCreateBanditV2RequestDataAttributes(
            name="bandit-14bb9543f523edde",
            datadog_flag_configuration=ExperimentsBanditFlagConfigurationInputV2(
                feature_flag_id=FEATURE_FLAG_DATA_ID,
                environment_id=ENVIRONMENT_DATA_ID,
                targeting_rules=[],
            ),
            variants=[
                ExperimentsBanditVariantInputV2(
                    feature_flag_variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID,
                    is_fallback=True,
                ),
                ExperimentsBanditVariantInputV2(
                    feature_flag_variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_1_ID,
                ),
            ],
            subject_type_id=EXPERIMENT_SUBJECT_TYPE_DATA_ID,
            tags=[
                "bdd",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_bandit"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_bandit(body=body)

    print(response)
