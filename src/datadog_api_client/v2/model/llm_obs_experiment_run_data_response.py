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


class LLMObsExperimentRunDataResponse(ModelNormal):
    validations = {
        "run_number": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "aggregate_data": (
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
            "experiment_id": (str,),
            "id": (str,),
            "run_number": (int,),
        }

    attribute_map = {
        "aggregate_data": "aggregate_data",
        "created_at": "created_at",
        "experiment_id": "experiment_id",
        "id": "id",
        "run_number": "run_number",
    }

    def __init__(
        self_,
        aggregate_data: Union[Dict[str, Any], none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        experiment_id: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        run_number: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for an LLM Observability experiment run.

        :param aggregate_data: Aggregated metric data for this run.
        :type aggregate_data: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param created_at: Timestamp when the run was created.
        :type created_at: datetime, optional

        :param experiment_id: Identifier of the experiment this run belongs to.
        :type experiment_id: str, optional

        :param id: Unique identifier of the experiment run.
        :type id: str, optional

        :param run_number: Sequential number of this run within the experiment.
        :type run_number: int, optional
        """
        if aggregate_data is not unset:
            kwargs["aggregate_data"] = aggregate_data
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if id is not unset:
            kwargs["id"] = id
        if run_number is not unset:
            kwargs["run_number"] = run_number
        super().__init__(kwargs)
