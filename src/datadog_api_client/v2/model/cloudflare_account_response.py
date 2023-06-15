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
    from datadog_api_client.v2.model.cloudflare_account_response_data import CloudflareAccountResponseData


@dataclass
class CloudflareAccountResponseJSON:
    id: str
    email: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset


class CloudflareAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_account_response_data import CloudflareAccountResponseData

        return {
            "data": (CloudflareAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = CloudflareAccountResponseJSON

    def __init__(self_, data: Union[CloudflareAccountResponseData, UnsetType] = unset, **kwargs):
        """
        The expected response schema when getting a Cloudflare account.

        :param data: Data object of a Cloudflare account.
        :type data: CloudflareAccountResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
