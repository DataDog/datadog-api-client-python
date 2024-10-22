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
    from datadog_api_client.v2.model.aws_account_patch_request_data import AWSAccountPatchRequestData


class AWSAccountPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_patch_request_data import AWSAccountPatchRequestData

        return {
            "data": (AWSAccountPatchRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSAccountPatchRequestData, **kwargs):
        """
        AWS Account Patch Request body

        :param data: AWS Account Patch Request data
        :type data: AWSAccountPatchRequestData
        """
        super().__init__(kwargs)

        self_.data = data
