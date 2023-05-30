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
    from datadog_api_client.v2.model.gcpsts_delegate_account_attributes import GCPSTSDelegateAccountAttributes
    from datadog_api_client.v2.model.gcpsts_delegate_account_type import GCPSTSDelegateAccountType


class GCPSTSDelegateAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcpsts_delegate_account_attributes import GCPSTSDelegateAccountAttributes
        from datadog_api_client.v2.model.gcpsts_delegate_account_type import GCPSTSDelegateAccountType

        return {
            "attributes": (GCPSTSDelegateAccountAttributes,),
            "id": (str,),
            "type": (GCPSTSDelegateAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GCPSTSDelegateAccountAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GCPSTSDelegateAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog principal service account info.

        :param attributes: Your delegate account attributes.
        :type attributes: GCPSTSDelegateAccountAttributes, optional

        :param id: The ID of the delegate service account.
        :type id: str, optional

        :param type: The type of account.
        :type type: GCPSTSDelegateAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
