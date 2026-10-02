"""
Patch subject type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request import ExperimentsPatchSubjectTypeV2Request
from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data import (
    ExperimentsPatchSubjectTypeV2RequestData,
)
from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data_attributes import (
    ExperimentsPatchSubjectTypeV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import ExperimentsSubjectTypeV2DTODataType

# there is a valid "experiment_subject_type" in the system
EXPERIMENT_SUBJECT_TYPE_DATA_ID = environ["EXPERIMENT_SUBJECT_TYPE_DATA_ID"]

body = ExperimentsPatchSubjectTypeV2Request(
    data=ExperimentsPatchSubjectTypeV2RequestData(
        type=ExperimentsSubjectTypeV2DTODataType.SUBJECT_TYPES,
        attributes=ExperimentsPatchSubjectTypeV2RequestDataAttributes(
            name="ex-14bb9543f523edde updated",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.patch_subject_type(subject_type_id=EXPERIMENT_SUBJECT_TYPE_DATA_ID, body=body)

    print(response)
