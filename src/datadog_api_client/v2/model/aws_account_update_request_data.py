# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_account_update_request_attributes import AWSAccountUpdateRequestAttributes
    from datadog_api_client.v2.model.aws_account_type import AWSAccountType


class AWSAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_update_request_attributes import AWSAccountUpdateRequestAttributes
        from datadog_api_client.v2.model.aws_account_type import AWSAccountType

        return {
            "attributes": (AWSAccountUpdateRequestAttributes,),
            "id": (str,),
            "type": (AWSAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AWSAccountUpdateRequestAttributes,
        type: AWSAccountType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Account Update Request data.

        :param attributes: The AWS Account Integration Config to be updated.
        :type attributes: AWSAccountUpdateRequestAttributes

        :param id: Unique Datadog ID of the AWS Account Integration Config.
            To get the config ID for an account, use the `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_
            endpoint and query by AWS Account ID.
        :type id: str, optional

        :param type: AWS Account resource type.
        :type type: AWSAccountType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
