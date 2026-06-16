# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class TagIndexingRuleExemptionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by_handle": (str,),
            "kind": (str,),
            "reason": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "kind": "kind",
        "reason": "reason",
    }
    read_only_vars = {
        "created_at",
        "created_by_handle",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        kind: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a tag indexing rule exemption.

        :param created_at: Timestamp when the exemption was created.
        :type created_at: datetime, optional

        :param created_by_handle: Handle of the user who created the exemption.
        :type created_by_handle: str, optional

        :param kind: Discriminates between an explicit exemption ( ``exemption`` ) and a pre-existing legacy tag configuration acting as an implicit exclusion ( ``legacy_tag_configuration`` ).
        :type kind: str, optional

        :param reason: The reason the metric is exempt from tag indexing rules.
        :type reason: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if kind is not unset:
            kwargs["kind"] = kind
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)
