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
    from datadog_api_client.v2.model.aws_account_create_attributes import AWSAccountCreateAttributes
    from datadog_api_client.v2.model.aws_account_type import AWSAccountType


class AWSAccountCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_create_attributes import AWSAccountCreateAttributes
        from datadog_api_client.v2.model.aws_account_type import AWSAccountType

        return {
            "attributes": (AWSAccountCreateAttributes,),
            "type": (AWSAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AWSAccountCreateAttributes, type: AWSAccountType, **kwargs):
        """
        AWS Account creation object

        :param attributes: AWS Account attributes for creation
        :type attributes: AWSAccountCreateAttributes

        :param type: AWS Account type
        :type type: AWSAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
