# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.cloudflare_account_update_request_attributes import (
    CloudflareAccountUpdateRequestAttributes,
)

if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType


@dataclass
class CloudflareAccountUpdateRequestDataJSON:
    api_key: Union[str, UnsetType] = unset
    email: Union[str, UnsetType] = unset


class CloudflareAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType

        return {
            "attributes": (CloudflareAccountUpdateRequestAttributes,),
            "type": (CloudflareAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = CloudflareAccountUpdateRequestDataJSON

    def __init__(
        self_,
        attributes: Union[CloudflareAccountUpdateRequestAttributes, UnsetType] = unset,
        type: Union[CloudflareAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a Cloudflare account.

        :param attributes: Attributes object for updating a Cloudflare account.
        :type attributes: CloudflareAccountUpdateRequestAttributes, optional

        :param type: The JSON:API type for this API. Should always be ``cloudflare-accounts``.
        :type type: CloudflareAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
