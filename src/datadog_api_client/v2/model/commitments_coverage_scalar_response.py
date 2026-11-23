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
    from datadog_api_client.v2.model.commitments_coverage_scalar_response_data import (
        CommitmentsCoverageScalarResponseData,
    )


class CommitmentsCoverageScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_coverage_scalar_response_data import (
            CommitmentsCoverageScalarResponseData,
        )

        return {
            "data": (CommitmentsCoverageScalarResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CommitmentsCoverageScalarResponseData, **kwargs):
        """
        Response containing scalar coverage metrics for cloud commitment programs.

        :param data: The scalar coverage resource.
        :type data: CommitmentsCoverageScalarResponseData
        """
        super().__init__(kwargs)

        self_.data = data
