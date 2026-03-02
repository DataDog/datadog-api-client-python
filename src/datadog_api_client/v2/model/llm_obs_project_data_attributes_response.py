# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class LLMObsProjectDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str, none_type),
            "name": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "name": "name",
        "updated_at": "updated_at",
    }

    def __init__(
        self_, created_at: datetime, description: Union[str, none_type], name: str, updated_at: datetime, **kwargs
    ):
        """
        Attributes of an LLM Observability project.

        :param created_at: Timestamp when the project was created.
        :type created_at: datetime

        :param description: Description of the project.
        :type description: str, none_type

        :param name: Name of the project.
        :type name: str

        :param updated_at: Timestamp when the project was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.description = description
        self_.name = name
        self_.updated_at = updated_at
