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
    from datadog_api_client.v2.model.aws_ccm_config_validation_response_data import AWSCcmConfigValidationResponseData


class AWSCcmConfigValidationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_validation_response_data import (
            AWSCcmConfigValidationResponseData,
        )

        return {
            "data": (AWSCcmConfigValidationResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSCcmConfigValidationResponseData, **kwargs):
        """
        AWS CCM config validation response body.

        :param data: AWS CCM config validation response data.
        :type data: AWSCcmConfigValidationResponseData
        """
        super().__init__(kwargs)

        self_.data = data
