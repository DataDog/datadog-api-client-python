"""
Create exposure SQL model returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request import (
    ExperimentsCreateExposureSQLModelV2Request,
)
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data import (
    ExperimentsCreateExposureSQLModelV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
)
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
)
from datadog_api_client.v2.model.experiments_sql_model_property_input import ExperimentsSQLModelPropertyInput
from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_attributes import (
    ExperimentsUpdateExposureSQLModelV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_type import (
    ExperimentsUpdateExposureSQLModelV2RequestDataType,
)

body = ExperimentsCreateExposureSQLModelV2Request(
    data=ExperimentsCreateExposureSQLModelV2RequestData(
        attributes=ExperimentsUpdateExposureSQLModelV2RequestDataAttributes(
            date_partition_column=None,
            experiment_column="experiment_id",
            name="Exposure events",
            properties=[
                ExperimentsSQLModelPropertyInput(
                    column_name="country",
                    column_type=ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.STRING,
                    description=None,
                    name="country",
                ),
            ],
            sql="SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures",
            subject_types=[
                ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems(
                    column_name="user_id",
                    subject_type_id="550e8400-e29b-41d4-a716-446655440010",
                ),
            ],
            timestamp_column="exposed_at",
            variant_column="variant",
        ),
        type=ExperimentsUpdateExposureSQLModelV2RequestDataType.EXPOSURE_SQL_MODELS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_exposure_sql_model(body=body)

    print(response)
