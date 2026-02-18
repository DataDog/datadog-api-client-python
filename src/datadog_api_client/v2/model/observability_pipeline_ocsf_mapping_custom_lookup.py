# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup_table_entry import (
        ObservabilityPipelineOcsfMappingCustomLookupTableEntry,
    )


class ObservabilityPipelineOcsfMappingCustomLookup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup_table_entry import (
            ObservabilityPipelineOcsfMappingCustomLookupTableEntry,
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
            "table": ([ObservabilityPipelineOcsfMappingCustomLookupTableEntry],),
        }

    attribute_map = {
        "default": "default",
        "table": "table",
    }

    def __init__(
        self_,
        default: Union[Any, UnsetType] = unset,
        table: Union[List[ObservabilityPipelineOcsfMappingCustomLookupTableEntry], UnsetType] = unset,
        **kwargs,
    ):
        """
        Lookup table configuration for mapping source values to destination values.

        :param default: The default value to use if no lookup match is found.
        :type default: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param table: A list of lookup table entries for value transformation.
        :type table: [ObservabilityPipelineOcsfMappingCustomLookupTableEntry], optional
        """
        if default is not unset:
            kwargs["default"] = default
        if table is not unset:
            kwargs["table"] = table
        super().__init__(kwargs)
