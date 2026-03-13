# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CycloneDXRating(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "score": (float,),
            "severity": (str,),
            "vector": (str,),
        }

    attribute_map = {
        "score": "score",
        "severity": "severity",
        "vector": "vector",
    }

    def __init__(
        self_,
        score: Union[float, UnsetType] = unset,
        severity: Union[str, UnsetType] = unset,
        vector: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Vulnerability rating information.

        :param score: The CVSS score.
        :type score: float, optional

        :param severity: The severity level.
        :type severity: str, optional

        :param vector: The CVSS vector string.
        :type vector: str, optional
        """
        if score is not unset:
            kwargs["score"] = score
        if severity is not unset:
            kwargs["severity"] = severity
        if vector is not unset:
            kwargs["vector"] = vector
        super().__init__(kwargs)
