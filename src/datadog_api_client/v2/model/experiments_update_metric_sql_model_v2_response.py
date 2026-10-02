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
    from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data import ExperimentsMetricSQLModelV2DTOData
    from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_response_meta import (
        ExperimentsUpdateMetricSQLModelV2ResponseMeta,
    )


class ExperimentsUpdateMetricSQLModelV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data import (
            ExperimentsMetricSQLModelV2DTOData,
        )
        from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_response_meta import (
            ExperimentsUpdateMetricSQLModelV2ResponseMeta,
        )

        return {
            "data": (ExperimentsMetricSQLModelV2DTOData,),
            "meta": (ExperimentsUpdateMetricSQLModelV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: ExperimentsMetricSQLModelV2DTOData,
        meta: Union[ExperimentsUpdateMetricSQLModelV2ResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated metric SQL model and its removed entries.

        :param data: JSON:API resource containing the metric SQL model identity and fields.
        :type data: ExperimentsMetricSQLModelV2DTOData

        :param meta: Model entries removed by the update. Empty arrays mean no entries were removed.
        :type meta: ExperimentsUpdateMetricSQLModelV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
