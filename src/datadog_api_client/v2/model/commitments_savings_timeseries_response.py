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
    from datadog_api_client.v2.model.commitments_savings_timeseries_response_data import (
        CommitmentsSavingsTimeseriesResponseData,
    )


class CommitmentsSavingsTimeseriesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_savings_timeseries_response_data import (
            CommitmentsSavingsTimeseriesResponseData,
        )

        return {
            "data": (CommitmentsSavingsTimeseriesResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CommitmentsSavingsTimeseriesResponseData, **kwargs):
        """
        Response containing timeseries savings metrics for cloud commitment programs.

        :param data: The timeseries savings resource.
        :type data: CommitmentsSavingsTimeseriesResponseData
        """
        super().__init__(kwargs)

        self_.data = data
