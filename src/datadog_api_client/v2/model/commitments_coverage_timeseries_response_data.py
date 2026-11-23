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
    from datadog_api_client.v2.model.commitments_coverage_timeseries_response_attributes import (
        CommitmentsCoverageTimeseriesResponseAttributes,
    )
    from datadog_api_client.v2.model.commitments_coverage_timeseries_response_type import (
        CommitmentsCoverageTimeseriesResponseType,
    )


class CommitmentsCoverageTimeseriesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_coverage_timeseries_response_attributes import (
            CommitmentsCoverageTimeseriesResponseAttributes,
        )
        from datadog_api_client.v2.model.commitments_coverage_timeseries_response_type import (
            CommitmentsCoverageTimeseriesResponseType,
        )

        return {
            "attributes": (CommitmentsCoverageTimeseriesResponseAttributes,),
            "id": (str,),
            "type": (CommitmentsCoverageTimeseriesResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CommitmentsCoverageTimeseriesResponseAttributes,
        id: str,
        type: CommitmentsCoverageTimeseriesResponseType,
        **kwargs,
    ):
        """
        The timeseries coverage resource.

        :param attributes: Attributes of a timeseries coverage response.
        :type attributes: CommitmentsCoverageTimeseriesResponseAttributes

        :param id: The identifier of the timeseries coverage response.
        :type id: str

        :param type: Type of the timeseries coverage response resource.
        :type type: CommitmentsCoverageTimeseriesResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
