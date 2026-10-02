# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data import ExperimentsMetricSQLModelV2DTOData


class ExperimentsMetricSQLModelV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data import (
            ExperimentsMetricSQLModelV2DTOData,
        )

        return {
            "data": (ExperimentsMetricSQLModelV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsMetricSQLModelV2DTOData, **kwargs):
        """
        Response containing the metric SQL model.

        :param data: JSON:API resource containing the metric SQL model identity and fields.
        :type data: ExperimentsMetricSQLModelV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data
