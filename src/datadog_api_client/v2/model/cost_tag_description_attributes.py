# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_tag_description_source import CostTagDescriptionSource


class CostTagDescriptionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_description_source import CostTagDescriptionSource

        return {
            "cloud": (str,),
            "created_at": (str,),
            "description": (str,),
            "source": (CostTagDescriptionSource,),
            "tag_key": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "cloud": "cloud",
        "created_at": "created_at",
        "description": "description",
        "source": "source",
        "tag_key": "tag_key",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        cloud: str,
        created_at: str,
        description: str,
        source: CostTagDescriptionSource,
        tag_key: str,
        updated_at: str,
        **kwargs,
    ):
        """
        Human-readable description and metadata attached to a Cloud Cost Management tag key, optionally scoped to a single cloud provider.

        :param cloud: Cloud provider this description applies to (for example, ``aws`` ). Empty when the description is the cross-cloud default for the tag key.
        :type cloud: str

        :param created_at: Timestamp when the description was created, in RFC 3339 format.
        :type created_at: str

        :param description: The human-readable description for the tag key.
        :type description: str

        :param source: Origin of the description. ``human`` indicates the description was written by a user, ``ai_generated`` was produced by AI, and ``datadog`` is a default supplied by Datadog.
        :type source: CostTagDescriptionSource

        :param tag_key: The tag key this description applies to.
        :type tag_key: str

        :param updated_at: Timestamp when the description was last updated, in RFC 3339 format.
        :type updated_at: str
        """
        super().__init__(kwargs)

        self_.cloud = cloud
        self_.created_at = created_at
        self_.description = description
        self_.source = source
        self_.tag_key = tag_key
        self_.updated_at = updated_at
