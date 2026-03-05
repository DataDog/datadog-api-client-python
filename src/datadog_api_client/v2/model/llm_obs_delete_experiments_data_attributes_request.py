# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteExperimentsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "experiment_ids": ([str],),
        }

    attribute_map = {
        "experiment_ids": "experiment_ids",
    }

    def __init__(self_, experiment_ids: List[str], **kwargs):
        """
        Attributes for deleting LLM Observability experiments.

        :param experiment_ids: List of experiment IDs to delete.
        :type experiment_ids: [str]
        """
        super().__init__(kwargs)

        self_.experiment_ids = experiment_ids
