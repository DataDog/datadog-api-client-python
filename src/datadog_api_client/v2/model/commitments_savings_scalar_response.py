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
    from datadog_api_client.v2.model.commitments_savings_scalar_response_data import (
        CommitmentsSavingsScalarResponseData,
    )


class CommitmentsSavingsScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_savings_scalar_response_data import (
            CommitmentsSavingsScalarResponseData,
        )

        return {
            "data": (CommitmentsSavingsScalarResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CommitmentsSavingsScalarResponseData, **kwargs):
        """
        Response containing scalar savings metrics for cloud commitment programs.

        :param data: The scalar savings resource.
        :type data: CommitmentsSavingsScalarResponseData
        """
        super().__init__(kwargs)

        self_.data = data
