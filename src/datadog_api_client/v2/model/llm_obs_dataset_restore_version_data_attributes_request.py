# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDatasetRestoreVersionDataAttributesRequest(ModelNormal):
    validations = {
        "dataset_version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "dataset_version": (int,),
        }

    attribute_map = {
        "dataset_version": "dataset_version",
    }

    def __init__(self_, dataset_version: int, **kwargs):
        """
        Attributes for restoring an LLM Observability dataset to a previous version.

        :param dataset_version: Version number of the dataset to restore. Must be between 0 and the current version of the dataset, inclusive.
        :type dataset_version: int
        """
        super().__init__(kwargs)

        self_.dataset_version = dataset_version
