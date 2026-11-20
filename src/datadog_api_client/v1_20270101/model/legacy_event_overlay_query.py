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
    from datadog_api_client.v1_20270101.model.tags_execution import TagsExecution


class LegacyEventOverlayQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.tags_execution import TagsExecution

        return {
            "q": (str,),
            "tags_execution": (TagsExecution,),
        }

    attribute_map = {
        "q": "q",
        "tags_execution": "tags_execution",
    }

    def __init__(self_, q: str, tags_execution: Union[TagsExecution, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param tags_execution: Test-only generated schema for the dashboard versioning proof of concept.
        :type tags_execution: TagsExecution, optional
        """
        if tags_execution is not unset:
            kwargs["tags_execution"] = tags_execution
        super().__init__(kwargs)

        self_.q = q
