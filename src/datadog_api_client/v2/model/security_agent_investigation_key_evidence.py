# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityAgentInvestigationKeyEvidence(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "finding": (str,),
            "source_steps": ([str],),
        }

    attribute_map = {
        "category": "category",
        "finding": "finding",
        "source_steps": "source_steps",
    }

    def __init__(self_, category: str, finding: str, source_steps: Union[List[str], UnsetType] = unset, **kwargs):
        """
        A piece of evidence the verdict rests on.

        :param category: Category of the evidence.
        :type category: str

        :param finding: What the investigation found.
        :type finding: str

        :param source_steps: Names of the steps the evidence comes from.
        :type source_steps: [str], optional
        """
        if source_steps is not unset:
            kwargs["source_steps"] = source_steps
        super().__init__(kwargs)

        self_.category = category
        self_.finding = finding
