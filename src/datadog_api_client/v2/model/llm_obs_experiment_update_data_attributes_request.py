# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.llm_obs_experiment_status import LLMObsExperimentStatus


class LLMObsExperimentUpdateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_status import LLMObsExperimentStatus

        return {
            "dataset_id": (str,),
            "description": (str,),
            "error": (str,),
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
            "status": (LLMObsExperimentStatus,),
        }

    attribute_map = {
        "dataset_id": "dataset_id",
        "description": "description",
        "error": "error",
        "metadata": "metadata",
        "name": "name",
        "status": "status",
    }

    def __init__(
        self_,
        dataset_id: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        error: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        status: Union[LLMObsExperimentStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an LLM Observability experiment.

        :param dataset_id: Updated identifier of the dataset used in this experiment.
        :type dataset_id: str, optional

        :param description: Updated description of the experiment.
        :type description: str, optional

        :param error: Error message describing why the experiment failed, if applicable.
        :type error: str, optional

        :param metadata: Updated arbitrary metadata associated with the experiment.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Updated name of the experiment.
        :type name: str, optional

        :param status: Execution status of an LLM Observability experiment.
        :type status: LLMObsExperimentStatus, optional
        """
        if dataset_id is not unset:
            kwargs["dataset_id"] = dataset_id
        if description is not unset:
            kwargs["description"] = description
        if error is not unset:
            kwargs["error"] = error
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
