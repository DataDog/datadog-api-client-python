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
    from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes


class AWSAccountCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes

        return {
            "attributes": (AWSAccountCreateRequestAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AWSAccountCreateRequestAttributes,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Account Create Request data

        :param attributes: The AWS Account Integration Config to be created
        :type attributes: AWSAccountCreateRequestAttributes

        :param id: AWS Account ID
        :type id: str, optional

        :param type: Request or response type
        :type type: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
