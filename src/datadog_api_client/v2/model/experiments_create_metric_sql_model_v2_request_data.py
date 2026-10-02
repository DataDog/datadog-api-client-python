# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_attributes import (
        ExperimentsUpdateMetricSQLModelV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_type import (
        ExperimentsUpdateMetricSQLModelV2RequestDataType,
    )


class ExperimentsCreateMetricSQLModelV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_attributes import (
            ExperimentsUpdateMetricSQLModelV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_type import (
            ExperimentsUpdateMetricSQLModelV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsUpdateMetricSQLModelV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsUpdateMetricSQLModelV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsUpdateMetricSQLModelV2RequestDataAttributes,
        type: ExperimentsUpdateMetricSQLModelV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metric SQL model resource to create.

        :param attributes: Complete column mappings and query used to replace the metric SQL model.
        :type attributes: ExperimentsUpdateMetricSQLModelV2RequestDataAttributes

        :param id: Optional JSON:API resource identifier field.
        :type id: str, optional

        :param type: Metric SQL models resource type.
        :type type: ExperimentsUpdateMetricSQLModelV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
