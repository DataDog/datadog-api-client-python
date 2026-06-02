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
    from datadog_api_client.v2.model.aggregated_signals_problems_response_attributes import (
        AggregatedSignalsProblemsResponseAttributes,
    )
    from datadog_api_client.v2.model.aggregated_signals_problems_request_type import (
        AggregatedSignalsProblemsRequestType,
    )


class AggregatedSignalsProblemsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_signals_problems_response_attributes import (
            AggregatedSignalsProblemsResponseAttributes,
        )
        from datadog_api_client.v2.model.aggregated_signals_problems_request_type import (
            AggregatedSignalsProblemsRequestType,
        )

        return {
            "attributes": (AggregatedSignalsProblemsResponseAttributes,),
            "id": (str,),
            "type": (AggregatedSignalsProblemsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AggregatedSignalsProblemsResponseAttributes,
        id: str,
        type: AggregatedSignalsProblemsRequestType,
        **kwargs,
    ):
        """
        Data envelope for an aggregated signals and problems response.

        :param attributes: Attributes of an aggregated signals and problems response.
        :type attributes: AggregatedSignalsProblemsResponseAttributes

        :param id: Hash-based unique identifier for this aggregation.
        :type id: str

        :param type: The JSON:API type for aggregated signals and problems requests.
        :type type: AggregatedSignalsProblemsRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
