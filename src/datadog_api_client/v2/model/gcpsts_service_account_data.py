# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType


@dataclass
class GCPSTSServiceAccountDataJSON:
    automute: Union[bool, UnsetType] = unset
    client_email: Union[str, UnsetType] = unset
    host_filters: Union[List[str], UnsetType] = unset
    is_cspm_enabled: Union[bool, UnsetType] = unset


class GCPSTSServiceAccountData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType

        return {
            "attributes": (GCPSTSServiceAccountAttributes,),
            "type": (GCPServiceAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = GCPSTSServiceAccountDataJSON

    def __init__(
        self_,
        attributes: Union[GCPSTSServiceAccountAttributes, UnsetType] = unset,
        type: Union[GCPServiceAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional metadata on your generated service account.

        :param attributes: Attributes associated with your service account.
        :type attributes: GCPSTSServiceAccountAttributes, optional

        :param type: The type of account.
        :type type: GCPServiceAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
