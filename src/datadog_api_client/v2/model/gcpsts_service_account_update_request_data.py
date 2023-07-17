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
    from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
    from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType


class GCPSTSServiceAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
        from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType

        return {
            "attributes": (GCPSTSServiceAccountAttributes,),
            "id": (str,),
            "type": (GCPServiceAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GCPSTSServiceAccountAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GCPServiceAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data on your service account.

        :param attributes: Attributes associated with your service account.
        :type attributes: GCPSTSServiceAccountAttributes, optional

        :param id: Your service account's unique ID.
        :type id: str, optional

        :param type: The type of account.
        :type type: GCPServiceAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
