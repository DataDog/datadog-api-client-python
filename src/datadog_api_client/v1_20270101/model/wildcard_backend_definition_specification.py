# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.wildcard_specification_type import WildcardSpecificationType


class WildcardBackendDefinitionSpecification(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.wildcard_specification_type import WildcardSpecificationType

        return {
            "contents": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "type": (WildcardSpecificationType,),
        }

    attribute_map = {
        "contents": "contents",
        "type": "type",
    }

    def __init__(self_, contents: Dict[str, Any], type: WildcardSpecificationType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param contents: Test-only generated schema for the dashboard versioning proof of concept.
        :type contents: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: WildcardSpecificationType
        """
        super().__init__(kwargs)

        self_.contents = contents
        self_.type = type
