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
    from datadog_api_client.v1_20270101.model.events_data_extraction_extraction_type import (
        EventsDataExtractionExtractionType,
    )


class EventsDataExtractionExtraction(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_data_extraction_extraction_type import (
            EventsDataExtractionExtractionType,
        )

        return {
            "pattern": (str,),
            "type": (EventsDataExtractionExtractionType,),
        }

    attribute_map = {
        "pattern": "pattern",
        "type": "type",
    }

    def __init__(self_, pattern: str, type: EventsDataExtractionExtractionType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param pattern: Test-only generated schema for the dashboard versioning proof of concept.
        :type pattern: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: EventsDataExtractionExtractionType
        """
        super().__init__(kwargs)

        self_.pattern = pattern
        self_.type = type
