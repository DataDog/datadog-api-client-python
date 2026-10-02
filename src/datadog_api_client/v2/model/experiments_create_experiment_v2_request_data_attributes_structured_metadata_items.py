# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enum_values": ([str],),
            "field_key": (str,),
            "freetext_value": (str,),
        }

    attribute_map = {
        "enum_values": "enum_values",
        "field_key": "field_key",
        "freetext_value": "freetext_value",
    }

    def __init__(
        self_,
        field_key: str,
        enum_values: Union[List[str], UnsetType] = unset,
        freetext_value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata field key and values to set on the experiment.

        :param enum_values: Selected values for an enumerated metadata field.
        :type enum_values: [str], optional

        :param field_key: Key that identifies the metadata field.
        :type field_key: str

        :param freetext_value: Text value for a free-text metadata field.
        :type freetext_value: str, optional
        """
        if enum_values is not unset:
            kwargs["enum_values"] = enum_values
        if freetext_value is not unset:
            kwargs["freetext_value"] = freetext_value
        super().__init__(kwargs)

        self_.field_key = field_key
