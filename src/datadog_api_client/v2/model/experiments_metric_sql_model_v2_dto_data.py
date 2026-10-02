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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes import (
        ExperimentsMetricSQLModelV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_type import (
        ExperimentsUpdateMetricSQLModelV2RequestDataType,
    )


class ExperimentsMetricSQLModelV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes import (
            ExperimentsMetricSQLModelV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_request_data_type import (
            ExperimentsUpdateMetricSQLModelV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsMetricSQLModelV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsUpdateMetricSQLModelV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsUpdateMetricSQLModelV2RequestDataType,
        attributes: Union[ExperimentsMetricSQLModelV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the metric SQL model identity and fields.

        :param attributes: Details of the metric SQL model.
        :type attributes: ExperimentsMetricSQLModelV2DTODataAttributes, optional

        :param id: ID of the metric SQL model.
        :type id: UUID

        :param type: Metric SQL models resource type.
        :type type: ExperimentsUpdateMetricSQLModelV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
