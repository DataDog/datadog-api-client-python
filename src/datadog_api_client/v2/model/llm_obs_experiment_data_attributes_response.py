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


class LLMObsExperimentDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "config": (
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
            "created_at": (datetime,),
            "dataset_id": (str,),
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
            "project_id": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "config": "config",
        "created_at": "created_at",
        "dataset_id": "dataset_id",
        "description": "description",
        "metadata": "metadata",
        "name": "name",
        "project_id": "project_id",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        config: Union[Dict[str, Any], none_type],
        created_at: datetime,
        dataset_id: str,
        description: Union[str, none_type],
        metadata: Union[Dict[str, Any], none_type],
        name: str,
        project_id: str,
        updated_at: datetime,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability experiment.

        :param config: Configuration parameters for the experiment.
        :type config: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param created_at: Timestamp when the experiment was created.
        :type created_at: datetime

        :param dataset_id: Identifier of the dataset used in this experiment.
        :type dataset_id: str

        :param description: Description of the experiment.
        :type description: str, none_type

        :param metadata: Arbitrary metadata associated with the experiment.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param name: Name of the experiment.
        :type name: str

        :param project_id: Identifier of the project this experiment belongs to.
        :type project_id: str

        :param updated_at: Timestamp when the experiment was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.config = config
        self_.created_at = created_at
        self_.dataset_id = dataset_id
        self_.description = description
        self_.metadata = metadata
        self_.name = name
        self_.project_id = project_id
        self_.updated_at = updated_at
