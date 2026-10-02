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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_structured_metadata_items_field_type import (
        ExperimentsPatchExperimentV2ResponseDataAttributesStructuredMetadataItemsFieldType,
    )


class ExperimentsStructuredMetadataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_structured_metadata_items_field_type import (
            ExperimentsPatchExperimentV2ResponseDataAttributesStructuredMetadataItemsFieldType,
        )

        return {
            "enum_values": ([str],),
            "field_display_name": (str,),
            "field_key": (str,),
            "field_type": (ExperimentsPatchExperimentV2ResponseDataAttributesStructuredMetadataItemsFieldType,),
            "freetext_value": (str,),
        }

    attribute_map = {
        "enum_values": "enum_values",
        "field_display_name": "field_display_name",
        "field_key": "field_key",
        "field_type": "field_type",
        "freetext_value": "freetext_value",
    }

    def __init__(
        self_,
        field_key: str,
        enum_values: Union[List[str], UnsetType] = unset,
        field_display_name: Union[str, UnsetType] = unset,
        field_type: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesStructuredMetadataItemsFieldType, UnsetType
        ] = unset,
        freetext_value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata field values with their display name and type.

        :param enum_values: Selected values for an enumerated metadata field.
        :type enum_values: [str], optional

        :param field_display_name: Display name of the metadata field.
        :type field_display_name: str, optional

        :param field_key: Key that identifies the metadata field.
        :type field_key: str

        :param field_type: Type of value stored in the structured metadata field.
        :type field_type: ExperimentsPatchExperimentV2ResponseDataAttributesStructuredMetadataItemsFieldType, optional

        :param freetext_value: Text value for a free-text metadata field.
        :type freetext_value: str, optional
        """
        if enum_values is not unset:
            kwargs["enum_values"] = enum_values
        if field_display_name is not unset:
            kwargs["field_display_name"] = field_display_name
        if field_type is not unset:
            kwargs["field_type"] = field_type
        if freetext_value is not unset:
            kwargs["freetext_value"] = freetext_value
        super().__init__(kwargs)

        self_.field_key = field_key
