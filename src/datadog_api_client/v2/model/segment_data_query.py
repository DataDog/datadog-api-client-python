# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.segment_profile_store_block import SegmentProfileStoreBlock
    from datadog_api_client.v2.model.segment_event_platform_block import SegmentEventPlatformBlock
    from datadog_api_client.v2.model.segment_journey_block import SegmentJourneyBlock
    from datadog_api_client.v2.model.segment_reference_table_block import SegmentReferenceTableBlock
    from datadog_api_client.v2.model.segment_retention_block import SegmentRetentionBlock
    from datadog_api_client.v2.model.segment_static_block import SegmentStaticBlock
    from datadog_api_client.v2.model.segment_template_block import SegmentTemplateBlock


class SegmentDataQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_profile_store_block import SegmentProfileStoreBlock
        from datadog_api_client.v2.model.segment_event_platform_block import SegmentEventPlatformBlock
        from datadog_api_client.v2.model.segment_journey_block import SegmentJourneyBlock
        from datadog_api_client.v2.model.segment_reference_table_block import SegmentReferenceTableBlock
        from datadog_api_client.v2.model.segment_retention_block import SegmentRetentionBlock
        from datadog_api_client.v2.model.segment_static_block import SegmentStaticBlock
        from datadog_api_client.v2.model.segment_template_block import SegmentTemplateBlock

        return {
            "account_store": ([SegmentProfileStoreBlock],),
            "combination": (str,),
            "event_platform": ([SegmentEventPlatformBlock],),
            "journeys": ([SegmentJourneyBlock],),
            "reference_table": ([SegmentReferenceTableBlock],),
            "retentions": ([SegmentRetentionBlock],),
            "static": ([SegmentStaticBlock],),
            "templates": ([SegmentTemplateBlock],),
            "user_store": ([SegmentProfileStoreBlock],),
        }

    attribute_map = {
        "account_store": "account_store",
        "combination": "combination",
        "event_platform": "event_platform",
        "journeys": "journeys",
        "reference_table": "reference_table",
        "retentions": "retentions",
        "static": "static",
        "templates": "templates",
        "user_store": "user_store",
    }

    def __init__(
        self_,
        account_store: Union[List[SegmentProfileStoreBlock], UnsetType] = unset,
        combination: Union[str, UnsetType] = unset,
        event_platform: Union[List[SegmentEventPlatformBlock], UnsetType] = unset,
        journeys: Union[List[SegmentJourneyBlock], UnsetType] = unset,
        reference_table: Union[List[SegmentReferenceTableBlock], UnsetType] = unset,
        retentions: Union[List[SegmentRetentionBlock], UnsetType] = unset,
        static: Union[List[SegmentStaticBlock], UnsetType] = unset,
        templates: Union[List[SegmentTemplateBlock], UnsetType] = unset,
        user_store: Union[List[SegmentProfileStoreBlock], UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines who belongs to the segment. It contains one or more blocks, up to 20 in total.
        Use ``combination`` to combine named blocks with a boolean formula such as ``A AND NOT B``.

        :param account_store: Account profile blocks.
        :type account_store: [SegmentProfileStoreBlock], optional

        :param combination: Boolean formula that combines blocks by name.
        :type combination: str, optional

        :param event_platform: Event blocks.
        :type event_platform: [SegmentEventPlatformBlock], optional

        :param journeys: Funnel blocks.
        :type journeys: [SegmentJourneyBlock], optional

        :param reference_table: Reference table blocks.
        :type reference_table: [SegmentReferenceTableBlock], optional

        :param retentions: Retention blocks.
        :type retentions: [SegmentRetentionBlock], optional

        :param static: Uploaded list blocks.
        :type static: [SegmentStaticBlock], optional

        :param templates: Template blocks.
        :type templates: [SegmentTemplateBlock], optional

        :param user_store: User profile blocks.
        :type user_store: [SegmentProfileStoreBlock], optional
        """
        if account_store is not unset:
            kwargs["account_store"] = account_store
        if combination is not unset:
            kwargs["combination"] = combination
        if event_platform is not unset:
            kwargs["event_platform"] = event_platform
        if journeys is not unset:
            kwargs["journeys"] = journeys
        if reference_table is not unset:
            kwargs["reference_table"] = reference_table
        if retentions is not unset:
            kwargs["retentions"] = retentions
        if static is not unset:
            kwargs["static"] = static
        if templates is not unset:
            kwargs["templates"] = templates
        if user_store is not unset:
            kwargs["user_store"] = user_store
        super().__init__(kwargs)
