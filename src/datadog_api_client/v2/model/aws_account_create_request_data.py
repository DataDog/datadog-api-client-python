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
    from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
    from datadog_api_client.v2.model.aws_account_type import AWSAccountType


class AWSAccountCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
        from datadog_api_client.v2.model.aws_account_type import AWSAccountType

        return {
            "attributes": (AWSAccountCreateRequestAttributes,),
            "type": (AWSAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AWSAccountCreateRequestAttributes, type: AWSAccountType, **kwargs):
        """
        AWS Account Create Request data.

        :param attributes: The AWS Account Integration Config to be created.
        :type attributes: AWSAccountCreateRequestAttributes

        :param type: AWS Account resource type.
        :type type: AWSAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
