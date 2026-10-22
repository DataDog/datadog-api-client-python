# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_volume_status import (
        TagIndexingRuleExemptionVolumeStatus,
    )


class TagIndexingRuleExemptionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_volume_status import (
            TagIndexingRuleExemptionVolumeStatus,
        )

        return {
            "created_at": (datetime,),
            "created_by_handle": (str,),
            "estimated_change_in_volume": (int, none_type),
            "kind": (str,),
            "missing_indexed_tags": ([str],),
            "reason": (str,),
            "volume_status": (TagIndexingRuleExemptionVolumeStatus,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "estimated_change_in_volume": "estimated_change_in_volume",
        "kind": "kind",
        "missing_indexed_tags": "missing_indexed_tags",
        "reason": "reason",
        "volume_status": "volume_status",
    }
    read_only_vars = {
        "created_at",
        "created_by_handle",
        "estimated_change_in_volume",
        "missing_indexed_tags",
        "volume_status",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        estimated_change_in_volume: Union[int, none_type, UnsetType] = unset,
        kind: Union[str, UnsetType] = unset,
        missing_indexed_tags: Union[List[str], UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        volume_status: Union[TagIndexingRuleExemptionVolumeStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a tag indexing rule exemption.

        :param created_at: Timestamp when the exemption was created.
        :type created_at: datetime, optional

        :param created_by_handle: Handle of the user who created the exemption.
        :type created_by_handle: str, optional

        :param estimated_change_in_volume: Estimated change in indexed cardinality or points if the exemption is removed and the matching tag indexing
            rule applies to the metric. A negative value indicates a reduction in indexed volume, a positive value
            indicates an increase, and zero indicates no change. A ``null`` value indicates that the estimate is unavailable.
        :type estimated_change_in_volume: int, none_type, optional

        :param kind: Discriminates between an explicit exemption ( ``exemption`` ) and a pre-existing legacy tag configuration acting as an implicit exclusion ( ``legacy_tag_configuration`` ).
        :type kind: str, optional

        :param missing_indexed_tags: Tag keys used to query this metric in monitors, dashboards, notebooks, and SLOs that the matching rule would
            remove or not include if the exemption is removed.
        :type missing_indexed_tags: [str], optional

        :param reason: The reason the metric is exempt from tag indexing rules.
        :type reason: str, optional

        :param volume_status: Indicates whether ``estimated_change_in_volume`` is available and, if not, why. ``ok`` indicates a fresh estimate.
            ``unindexed_tags`` indicates that the matching rule uses tags that are not indexed for the metric.
            ``unavailable`` indicates that the estimate is stale, was not computed, or could not be retrieved.
        :type volume_status: TagIndexingRuleExemptionVolumeStatus, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if estimated_change_in_volume is not unset:
            kwargs["estimated_change_in_volume"] = estimated_change_in_volume
        if kind is not unset:
            kwargs["kind"] = kind
        if missing_indexed_tags is not unset:
            kwargs["missing_indexed_tags"] = missing_indexed_tags
        if reason is not unset:
            kwargs["reason"] = reason
        if volume_status is not unset:
            kwargs["volume_status"] = volume_status
        super().__init__(kwargs)
