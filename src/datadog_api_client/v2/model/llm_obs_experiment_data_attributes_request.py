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


class LLMObsExperimentDataAttributesRequest(ModelNormal):
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
            ),
            "dataset_id": (str,),
            "dataset_version": (int,),
            "description": (str,),
            "ensure_unique": (bool,),
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
            "project_id": (str,),
        }

    attribute_map = {
        "config": "config",
        "dataset_id": "dataset_id",
        "dataset_version": "dataset_version",
        "description": "description",
        "ensure_unique": "ensure_unique",
        "metadata": "metadata",
        "name": "name",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        dataset_id: str,
        name: str,
        project_id: str,
        config: Union[Dict[str, Any], UnsetType] = unset,
        dataset_version: Union[int, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        ensure_unique: Union[bool, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an LLM Observability experiment.

        :param config: Configuration parameters for the experiment.
        :type config: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param dataset_id: Identifier of the dataset used in this experiment.
        :type dataset_id: str

        :param dataset_version: Version of the dataset to use. Defaults to the current version if not specified.
        :type dataset_version: int, optional

        :param description: Description of the experiment.
        :type description: str, optional

        :param ensure_unique: Whether to ensure the experiment name is unique. Defaults to ``true``.
        :type ensure_unique: bool, optional

        :param metadata: Arbitrary metadata associated with the experiment.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Name of the experiment.
        :type name: str

        :param project_id: Identifier of the project this experiment belongs to.
        :type project_id: str
        """
        if config is not unset:
            kwargs["config"] = config
        if dataset_version is not unset:
            kwargs["dataset_version"] = dataset_version
        if description is not unset:
            kwargs["description"] = description
        if ensure_unique is not unset:
            kwargs["ensure_unique"] = ensure_unique
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.dataset_id = dataset_id
        self_.name = name
        self_.project_id = project_id
