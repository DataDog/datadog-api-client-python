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
    from datadog_api_client.v2.model.cost_anomalies_response_data_attributes import CostAnomaliesResponseDataAttributes
    from datadog_api_client.v2.model.cost_anomalies_response_data_type import CostAnomaliesResponseDataType


class CostAnomaliesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_anomalies_response_data_attributes import (
            CostAnomaliesResponseDataAttributes,
        )
        from datadog_api_client.v2.model.cost_anomalies_response_data_type import CostAnomaliesResponseDataType

        return {
            "attributes": (CostAnomaliesResponseDataAttributes,),
            "id": (str,),
            "type": (CostAnomaliesResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CostAnomaliesResponseDataAttributes, id: str, type: CostAnomaliesResponseDataType, **kwargs
    ):
        """
        Resource wrapper for the list of cost anomalies and aggregated totals.

        :param attributes: Cost anomaly results and aggregated totals for the queried window.
        :type attributes: CostAnomaliesResponseDataAttributes

        :param id: Static identifier of the cost anomalies collection resource.
        :type id: str

        :param type: Type of the cost anomalies collection resource. Must be ``anomalies``.
        :type type: CostAnomaliesResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
