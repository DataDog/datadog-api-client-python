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
    UUID,
)


class LLMObsDatasetDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "current_version": (int,),
            "description": (str, none_type),
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
                none_type,
            ),
            "name": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "current_version": "current_version",
        "description": "description",
        "metadata": "metadata",
        "name": "name",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        current_version: int,
        description: Union[str, none_type],
        metadata: Union[Dict[str, Any], none_type],
        name: str,
        updated_at: datetime,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability dataset.

        :param created_at: Timestamp when the dataset was created.
        :type created_at: datetime

        :param current_version: Current version number of the dataset.
        :type current_version: int

        :param description: Description of the dataset.
        :type description: str, none_type

        :param metadata: Arbitrary metadata associated with the dataset.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param name: Name of the dataset.
        :type name: str

        :param updated_at: Timestamp when the dataset was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.current_version = current_version
        self_.description = description
        self_.metadata = metadata
        self_.name = name
        self_.updated_at = updated_at
