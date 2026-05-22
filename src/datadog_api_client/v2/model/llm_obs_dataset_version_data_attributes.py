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


class LLMObsDatasetVersionDataAttributes(ModelNormal):
    validations = {
        "version_number": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "dataset_id": (str,),
            "last_used": (datetime, none_type),
            "version_number": (int,),
        }

    attribute_map = {
        "dataset_id": "dataset_id",
        "last_used": "last_used",
        "version_number": "version_number",
    }

    def __init__(self_, dataset_id: str, last_used: Union[datetime, none_type], version_number: int, **kwargs):
        """
        Attributes of an LLM Observability dataset version.

        :param dataset_id: Unique identifier of the dataset this version belongs to.
        :type dataset_id: str

        :param last_used: Timestamp when this dataset version was last referenced. Null if the version has never been used.
        :type last_used: datetime, none_type

        :param version_number: Sequential version number for this dataset version.
        :type version_number: int
        """
        super().__init__(kwargs)

        self_.dataset_id = dataset_id
        self_.last_used = last_used
        self_.version_number = version_number
