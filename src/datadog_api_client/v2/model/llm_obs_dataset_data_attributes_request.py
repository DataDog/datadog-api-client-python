# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

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


class LLMObsDatasetDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "metadata": (
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
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "metadata": "metadata",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        description: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an LLM Observability dataset.

        :param description: Description of the dataset.
        :type description: str, optional

        :param metadata: Arbitrary metadata associated with the dataset.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Name of the dataset.
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.name = name
