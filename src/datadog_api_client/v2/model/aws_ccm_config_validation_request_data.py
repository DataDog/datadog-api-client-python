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
    from datadog_api_client.v2.model.aws_ccm_config_validation_request_attributes import (
        AWSCcmConfigValidationRequestAttributes,
    )
    from datadog_api_client.v2.model.aws_ccm_config_validation_type import AWSCcmConfigValidationType


class AWSCcmConfigValidationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_validation_request_attributes import (
            AWSCcmConfigValidationRequestAttributes,
        )
        from datadog_api_client.v2.model.aws_ccm_config_validation_type import AWSCcmConfigValidationType

        return {
            "attributes": (AWSCcmConfigValidationRequestAttributes,),
            "type": (AWSCcmConfigValidationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AWSCcmConfigValidationRequestAttributes, type: AWSCcmConfigValidationType, **kwargs
    ):
        """
        AWS CCM config validation request data.

        :param attributes: Attributes for an AWS CCM config validation request.
        :type attributes: AWSCcmConfigValidationRequestAttributes

        :param type: AWS CCM config validation resource type.
        :type type: AWSCcmConfigValidationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
