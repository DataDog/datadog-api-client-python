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


from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry
from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry

if TYPE_CHECKING:
    from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData


@dataclass
class IPAllowlistUpdateRequestJSON:
    id: str
    enabled: Union[bool, UnsetType] = unset
    entries: Union[List[IPAllowlistEntry], UnsetType] = unset


class IPAllowlistUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData

        return {
            "data": (IPAllowlistData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IPAllowlistUpdateRequestJSON

    def __init__(self_, data: IPAllowlistData, **kwargs):
        """
        Update the IP allowlist.

        :param data: IP allowlist data.
        :type data: IPAllowlistData
        """
        super().__init__(kwargs)

        self_.data = data
