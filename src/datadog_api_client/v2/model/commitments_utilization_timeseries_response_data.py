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
    from datadog_api_client.v2.model.commitments_utilization_timeseries_response_attributes import (
        CommitmentsUtilizationTimeseriesResponseAttributes,
    )
    from datadog_api_client.v2.model.commitments_utilization_timeseries_response_type import (
        CommitmentsUtilizationTimeseriesResponseType,
    )


class CommitmentsUtilizationTimeseriesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_utilization_timeseries_response_attributes import (
            CommitmentsUtilizationTimeseriesResponseAttributes,
        )
        from datadog_api_client.v2.model.commitments_utilization_timeseries_response_type import (
            CommitmentsUtilizationTimeseriesResponseType,
        )

        return {
            "attributes": (CommitmentsUtilizationTimeseriesResponseAttributes,),
            "id": (str,),
            "type": (CommitmentsUtilizationTimeseriesResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CommitmentsUtilizationTimeseriesResponseAttributes,
        id: str,
        type: CommitmentsUtilizationTimeseriesResponseType,
        **kwargs,
    ):
        """
        The timeseries utilization resource.

        :param attributes: Attributes of a timeseries utilization response.
        :type attributes: CommitmentsUtilizationTimeseriesResponseAttributes

        :param id: The identifier of the timeseries utilization response.
        :type id: str

        :param type: Type of the timeseries utilization response resource.
        :type type: CommitmentsUtilizationTimeseriesResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
