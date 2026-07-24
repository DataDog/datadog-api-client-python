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
    from datadog_api_client.v2.model.incident_on_call_page_target import IncidentOnCallPageTarget


class IncidentOnCallPageDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_on_call_page_target import IncidentOnCallPageTarget

        return {
            "key": (str,),
            "page_target": (IncidentOnCallPageTarget,),
            "team_id": (str,),
        }

    attribute_map = {
        "key": "key",
        "page_target": "page_target",
        "team_id": "team_id",
    }

    def __init__(
        self_,
        key: Union[str, UnsetType] = unset,
        page_target: Union[IncidentOnCallPageTarget, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for linking a page to an incident.

        :param key: The key of the on-call page.
        :type key: str, optional

        :param page_target: The target of an on-call page.
        :type page_target: IncidentOnCallPageTarget, optional

        :param team_id: The team ID associated with the page (deprecated, use page_target instead).
        :type team_id: str, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if page_target is not unset:
            kwargs["page_target"] = page_target
        if team_id is not unset:
            kwargs["team_id"] = team_id
        super().__init__(kwargs)
