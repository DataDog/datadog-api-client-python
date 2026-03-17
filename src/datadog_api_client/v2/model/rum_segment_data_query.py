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
    from datadog_api_client.v2.model.rum_segment_event_platform import RumSegmentEventPlatform
    from datadog_api_client.v2.model.rum_segment_journey import RumSegmentJourney
    from datadog_api_client.v2.model.rum_segment_reference_table import RumSegmentReferenceTable
    from datadog_api_client.v2.model.rum_segment_static_entry import RumSegmentStaticEntry
    from datadog_api_client.v2.model.rum_segment_template_instance import RumSegmentTemplateInstance


class RumSegmentDataQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_event_platform import RumSegmentEventPlatform
        from datadog_api_client.v2.model.rum_segment_journey import RumSegmentJourney
        from datadog_api_client.v2.model.rum_segment_reference_table import RumSegmentReferenceTable
        from datadog_api_client.v2.model.rum_segment_static_entry import RumSegmentStaticEntry
        from datadog_api_client.v2.model.rum_segment_template_instance import RumSegmentTemplateInstance

        return {
            "combination": (str,),
            "event_platforms": ([RumSegmentEventPlatform],),
            "journeys": ([RumSegmentJourney],),
            "reference_tables": ([RumSegmentReferenceTable],),
            "static": ([RumSegmentStaticEntry],),
            "templates": ([RumSegmentTemplateInstance],),
        }

    attribute_map = {
        "combination": "combination",
        "event_platforms": "event_platforms",
        "journeys": "journeys",
        "reference_tables": "reference_tables",
        "static": "static",
        "templates": "templates",
    }

    def __init__(
        self_,
        combination: Union[str, UnsetType] = unset,
        event_platforms: Union[List[RumSegmentEventPlatform], UnsetType] = unset,
        journeys: Union[List[RumSegmentJourney], UnsetType] = unset,
        reference_tables: Union[List[RumSegmentReferenceTable], UnsetType] = unset,
        static: Union[List[RumSegmentStaticEntry], UnsetType] = unset,
        templates: Union[List[RumSegmentTemplateInstance], UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for the segment. Contains one or more query blocks and an optional combination formula.

        :param combination: Boolean expression combining multiple query blocks.
        :type combination: str, optional

        :param event_platforms: List of event platform query blocks.
        :type event_platforms: [RumSegmentEventPlatform], optional

        :param journeys: List of journey-based query blocks.
        :type journeys: [RumSegmentJourney], optional

        :param reference_tables: List of reference table query blocks.
        :type reference_tables: [RumSegmentReferenceTable], optional

        :param static: List of static user list blocks.
        :type static: [RumSegmentStaticEntry], optional

        :param templates: List of template-based query blocks.
        :type templates: [RumSegmentTemplateInstance], optional
        """
        if combination is not unset:
            kwargs["combination"] = combination
        if event_platforms is not unset:
            kwargs["event_platforms"] = event_platforms
        if journeys is not unset:
            kwargs["journeys"] = journeys
        if reference_tables is not unset:
            kwargs["reference_tables"] = reference_tables
        if static is not unset:
            kwargs["static"] = static
        if templates is not unset:
            kwargs["templates"] = templates
        super().__init__(kwargs)
