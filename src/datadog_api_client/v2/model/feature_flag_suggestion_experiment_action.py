# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class FeatureFlagSuggestionExperimentAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action": (str,),
            "experiment_id": (UUID,),
            "version": (int,),
        }

    attribute_map = {
        "action": "action",
        "experiment_id": "experiment_id",
        "version": "version",
    }

    def __init__(self_, action: str, experiment_id: UUID, version: int, **kwargs):
        """
        Server-generated reference to an experiment action requiring approval.

        :param action: The proposed experiment action.
        :type action: str

        :param experiment_id: The ID of the experiment.
        :type experiment_id: UUID

        :param version: The version of the experiment action reference.
        :type version: int
        """
        super().__init__(kwargs)

        self_.action = action
        self_.experiment_id = experiment_id
        self_.version = version
