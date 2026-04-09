# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class LLMObsAnnotationItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "id": (str,),
            "interaction_id": (str,),
            "label_values": (
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
            "modified_at": (datetime,),
            "modified_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "id": "id",
        "interaction_id": "interaction_id",
        "label_values": "label_values",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        id: str,
        interaction_id: str,
        label_values: Dict[str, Any],
        modified_at: datetime,
        modified_by: str,
        **kwargs,
    ):
        """
        A single annotation on an interaction.

        :param created_at: Timestamp when the annotation was created.
        :type created_at: datetime

        :param created_by: Identifier of the user who created the annotation.
        :type created_by: str

        :param id: Unique identifier of the annotation.
        :type id: str

        :param interaction_id: Identifier of the interaction this annotation belongs to.
        :type interaction_id: str

        :param label_values: The label values for this annotation.
        :type label_values: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param modified_at: Timestamp when the annotation was last modified.
        :type modified_at: datetime

        :param modified_by: Identifier of the user who last modified the annotation.
        :type modified_by: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.id = id
        self_.interaction_id = interaction_id
        self_.label_values = label_values
        self_.modified_at = modified_at
        self_.modified_by = modified_by
