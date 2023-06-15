# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ip_allowlist_entry_data import IPAllowlistEntryData


@dataclass
class IPAllowlistEntryJSON:
    id: str
    cidr_block: Union[str, UnsetType] = unset
    created_at: Union[datetime, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    note: Union[str, UnsetType] = unset


class IPAllowlistEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ip_allowlist_entry_data import IPAllowlistEntryData

        return {
            "data": (IPAllowlistEntryData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IPAllowlistEntryJSON

    def __init__(self_, data: IPAllowlistEntryData, **kwargs):
        """
        IP allowlist entry object.

        :param data: Data of the IP allowlist entry object.
        :type data: IPAllowlistEntryData
        """
        super().__init__(kwargs)

        self_.data = data
