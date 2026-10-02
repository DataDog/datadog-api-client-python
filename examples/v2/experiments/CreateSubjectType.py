"""
Create subject type returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_subject_type_v2_request import ExperimentsCreateSubjectTypeV2Request
from datadog_api_client.v2.model.experiments_create_subject_type_v2_request_data import (
    ExperimentsCreateSubjectTypeV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_subject_type_v2_request_data_attributes import (
    ExperimentsCreateSubjectTypeV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import ExperimentsSubjectTypeV2DTODataType

body = ExperimentsCreateSubjectTypeV2Request(
    data=ExperimentsCreateSubjectTypeV2RequestData(
        type=ExperimentsSubjectTypeV2DTODataType.SUBJECT_TYPES,
        attributes=ExperimentsCreateSubjectTypeV2RequestDataAttributes(
            name="ex-14bb9543f523edde",
            product_analytics_attribute="@account.id",
            warehouse_column_names=[
                "account_id",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_subject_type(body=body)

    print(response)
