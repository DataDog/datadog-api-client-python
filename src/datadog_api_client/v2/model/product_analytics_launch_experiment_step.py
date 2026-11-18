# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ProductAnalyticsLaunchExperimentStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "experiment_id": (str, none_type),
            "hypothesis": (str, none_type),
            "name": (str, none_type),
            "protocol_id": (str, none_type),
        }

    attribute_map = {
        "experiment_id": "experiment_id",
        "hypothesis": "hypothesis",
        "name": "name",
        "protocol_id": "protocol_id",
    }

    def __init__(
        self_,
        experiment_id: Union[str, none_type, UnsetType] = unset,
        hypothesis: Union[str, none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        protocol_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment linked to the launch. The draft fields are cleared when ``experiment_id`` is set.

        :param experiment_id: UUID of the linked experiment.
        :type experiment_id: str, none_type, optional

        :param hypothesis: Hypothesis of a draft experiment.
        :type hypothesis: str, none_type, optional

        :param name: Name of a draft experiment.
        :type name: str, none_type, optional

        :param protocol_id: Protocol ID of a draft experiment.
        :type protocol_id: str, none_type, optional
        """
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if hypothesis is not unset:
            kwargs["hypothesis"] = hypothesis
        if name is not unset:
            kwargs["name"] = name
        if protocol_id is not unset:
            kwargs["protocol_id"] = protocol_id
        super().__init__(kwargs)
