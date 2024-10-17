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
    from datadog_api_client.v2.model.aws_account_patch_request_attributes import AWSAccountPatchRequestAttributes


class AWSAccountPatchRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_patch_request_attributes import AWSAccountPatchRequestAttributes

        return {
            "attributes": (AWSAccountPatchRequestAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AWSAccountPatchRequestAttributes, id: Union[str, UnsetType] = unset, **kwargs):
        """
        AWS Account Patch Request data

        :param attributes: The AWS Account Integration Config to be updated
        :type attributes: AWSAccountPatchRequestAttributes

        :param id: Unique Datadog ID of the AWS Account Integration Config
        :type id: str, optional

        :param type: AWS Account resource type.
        :type type: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
        type = kwargs.get("type", "account")

        self_.attributes = attributes
        self_.type = type
