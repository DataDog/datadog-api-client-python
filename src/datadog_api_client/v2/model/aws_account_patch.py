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
    from datadog_api_client.v2.model.aws_account_patch_attributes import AWSAccountPatchAttributes
    from datadog_api_client.v2.model.aws_account_type import AWSAccountType


class AWSAccountPatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_account_patch_attributes import AWSAccountPatchAttributes
        from datadog_api_client.v2.model.aws_account_type import AWSAccountType

        return {
            "attributes": (AWSAccountPatchAttributes,),
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
        attributes: Union[AWSAccountPatchAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AWSAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Account patch object

        :param attributes: AWS Account attributes for patching
        :type attributes: AWSAccountPatchAttributes, optional

        :param id: AWS Account ID
        :type id: str, optional

        :param type: AWS Account type
        :type type: AWSAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
