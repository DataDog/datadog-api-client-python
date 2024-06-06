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
    from datadog_api_client.v2.model.aws_account_attributes import AWSAccountAttributes
    from datadog_api_client.v2.model.aws_account_type import AWSAccountType


class AWSAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_attributes import AWSAccountAttributes
        from datadog_api_client.v2.model.aws_account_type import AWSAccountType

        return {
            "attributes": (AWSAccountAttributes,),
            "id": (str,),
            "type": (AWSAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AWSAccountAttributes, id: str, type: AWSAccountType, **kwargs):
        """
        AWS Account object

        :param attributes: AWS Account attributes
        :type attributes: AWSAccountAttributes

        :param id: AWS Account ID
        :type id: str

        :param type: AWS Account type
        :type type: AWSAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
