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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloudflare_account_update_request_data import CloudflareAccountUpdateRequestData


@dataclass
class CloudflareAccountUpdateRequestJSON:
    api_key: Union[str, UnsetType] = unset
    email: Union[str, UnsetType] = unset


class CloudflareAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_account_update_request_data import (
            CloudflareAccountUpdateRequestData,
        )

        return {
            "data": (CloudflareAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = CloudflareAccountUpdateRequestJSON

    def __init__(self_, data: CloudflareAccountUpdateRequestData, **kwargs):
        """
        Payload schema when updating a Cloudflare account.

        :param data: Data object for updating a Cloudflare account.
        :type data: CloudflareAccountUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
