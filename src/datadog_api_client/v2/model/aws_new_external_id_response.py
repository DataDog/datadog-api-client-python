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
    from datadog_api_client.v2.model.aws_new_external_id_response_data import AWSNewExternalIDResponseData


class AWSNewExternalIDResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_new_external_id_response_data import AWSNewExternalIDResponseData

        return {
            "data": (AWSNewExternalIDResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSNewExternalIDResponseData, **kwargs):
        """
        AWS External ID response body.

        :param data: AWS External ID response body.
        :type data: AWSNewExternalIDResponseData
        """
        super().__init__(kwargs)

        self_.data = data
