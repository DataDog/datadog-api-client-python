# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup import (
        ObservabilityPipelineOcsfMappingCustomLookup,
    )


class ObservabilityPipelineOcsfMappingCustomFieldMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup import (
            ObservabilityPipelineOcsfMappingCustomLookup,
        )

        return {
            "default": (
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
            ),
            "dest": (str,),
            "lookup": (ObservabilityPipelineOcsfMappingCustomLookup,),
            "source": (
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
            ),
            "sources": (
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
            ),
            "value": (
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
            ),
        }

    attribute_map = {
        "default": "default",
        "dest": "dest",
        "lookup": "lookup",
        "source": "source",
        "sources": "sources",
        "value": "value",
    }

    def __init__(
        self_,
        dest: str,
        default: Union[Any, UnsetType] = unset,
        lookup: Union[ObservabilityPipelineOcsfMappingCustomLookup, UnsetType] = unset,
        source: Union[Any, UnsetType] = unset,
        sources: Union[Any, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a single field mapping rule for transforming a source field to an OCSF destination field.

        :param default: The default value to use if the source field is missing or empty.
        :type default: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param dest: The destination OCSF field path.
        :type dest: str

        :param lookup: Lookup table configuration for mapping source values to destination values.
        :type lookup: ObservabilityPipelineOcsfMappingCustomLookup, optional

        :param source: The source field path from the log event.
        :type source: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param sources: Multiple source field paths for combined mapping.
        :type sources: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param value: A static value to use for the destination field.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if default is not unset:
            kwargs["default"] = default
        if lookup is not unset:
            kwargs["lookup"] = lookup
        if source is not unset:
            kwargs["source"] = source
        if sources is not unset:
            kwargs["sources"] = sources
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.dest = dest
