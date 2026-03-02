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


class LLMObsDatasetUpdateDataAttributesRequest(ModelNormal):
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
        description: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an LLM Observability dataset.

        :param description: Updated description of the dataset.
        :type description: str, optional

        :param metadata: Updated metadata associated with the dataset.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Updated name of the dataset.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
