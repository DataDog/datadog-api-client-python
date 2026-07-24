# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ConfluencePostmortemSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "parent_id": (str, none_type),
            "space_id": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "parent_id": "parent_id",
        "space_id": "space_id",
    }

    def __init__(self_, account_id: str, space_id: str, parent_id: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Settings for a postmortem template stored in Confluence. Required when ``location`` is ``confluence``.

        :param account_id: The ID of the Confluence integration account.
        :type account_id: str

        :param parent_id: The ID of the parent Confluence page under which postmortems are created.
        :type parent_id: str, none_type, optional

        :param space_id: The ID of the Confluence space where postmortems are created.
        :type space_id: str
        """
        if parent_id is not unset:
            kwargs["parent_id"] = parent_id
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.space_id = space_id
