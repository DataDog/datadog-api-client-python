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
    from datadog_api_client.v2.model.rum_archive_sessions_search_attributes import RumArchiveSessionsSearchAttributes


class RumArchiveSessionsSearchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_sessions_search_attributes import (
            RumArchiveSessionsSearchAttributes,
        )

        return {
            "attributes": (RumArchiveSessionsSearchAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RumArchiveSessionsSearchAttributes,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource.

        :param attributes: Archived-session query. A window wider than configured archive retention is narrowed before searching.
        :type attributes: RumArchiveSessionsSearchAttributes

        :param id: Optional resource identifier.
        :type id: str, optional

        :param type: JSON:API resource type.
        :type type: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
