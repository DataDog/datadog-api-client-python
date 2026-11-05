# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


class AiGatewayCaptureScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "tags": ({str: (str,)},),
            "team_id": (UUID,),
            "user_id": (UUID,),
        }

    attribute_map = {
        "tags": "tags",
        "team_id": "team_id",
        "user_id": "user_id",
    }

    def __init__(
        self_,
        tags: Union[Dict[str, str], UnsetType] = unset,
        team_id: Union[UUID, UnsetType] = unset,
        user_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        All selected filters combine with AND, with one value per filter. The ``model`` and ``provider`` tags apply to each actual direct or routed attempt, including fallback destinations. Routes are not selectable filters. At least one filter is required.
        If any matching override uses ``metadata_only`` , that mode applies. Otherwise, if any matching override uses ``full_capture`` , that mode applies. The organization default applies only when no override matches. Overrides have no priority or specificity ordering.

        :param tags: Exact-match request tags with lowercase keys. The reserved ``model`` tag is the canonical model ID, and the reserved ``provider`` tag is the configured connection slug. The server sets both. Custom tags come from ``x-dd-tag`` headers. Keys and values must not have leading or trailing white space. Values are case-sensitive.
        :type tags: {str: (str,)}, optional

        :param team_id: UUID of a Datadog team. Matches the authorized team selected by the ``x-ai-gateway-team`` request header. Requests without this header do not match team-scoped overrides. Open-membership teams cannot scope overrides.
        :type team_id: UUID, optional

        :param user_id: Authenticated Datadog user UUID in this organization.
        :type user_id: UUID, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)
