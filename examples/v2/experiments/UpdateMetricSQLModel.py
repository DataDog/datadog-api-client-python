"""
Update metric SQL model returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
)
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
)
from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request import (
    ExperimentsCreateMetricSQLModelV2Request,
)
from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request_data import (
    ExperimentsCreateMetricSQLModelV2RequestData,
)
from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request_data_attributes_measures_items import (
    ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems,
)
from datadog_api_client.v2.model.experiments_metric_sql_model_property_input import (
    ExperimentsMetricSQLModelPropertyInput,
)
from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_attributes import (
    ExperimentsUpdateMetricSQLModelV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_type import (
    ExperimentsUpdateMetricSQLModelV2RequestDataType,
)
from uuid import UUID

body = ExperimentsCreateMetricSQLModelV2Request(
    data=ExperimentsCreateMetricSQLModelV2RequestData(
        attributes=ExperimentsUpdateMetricSQLModelV2RequestDataAttributes(
            date_partition_column=None,
            description=None,
            measures=[
                ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems(
                    column_name="revenue",
                    column_type=ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.FLOAT,
                    description=None,
                    name=None,
                ),
            ],
            name="Order facts",
            properties=[
                ExperimentsMetricSQLModelPropertyInput(
                    column_name="item_type",
                    column_type=ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.STRING,
                    description=None,
                    name="item_type",
                ),
            ],
            sql="SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders",
            subject_types=[
                ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems(
                    column_name="user_id",
                    subject_type_id="550e8400-e29b-41d4-a716-446655440010",
                ),
            ],
            timestamp_column="created_at",
        ),
        type=ExperimentsUpdateMetricSQLModelV2RequestDataType.METRIC_SQL_MODELS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.update_metric_sql_model(
        metric_sql_model_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body
    )

    print(response)
