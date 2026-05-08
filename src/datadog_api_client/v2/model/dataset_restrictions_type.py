# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatasetRestrictionsType(ModelSimple):
    """
    JSON:API resource type for dataset restrictions.

    :param value: If omitted defaults to "dataset_restrictions". Must be one of ["dataset_restrictions"].
    :type value: str
    """

    allowed_values = {
        "dataset_restrictions",
    }
    DATASET_RESTRICTIONS: ClassVar["DatasetRestrictionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatasetRestrictionsType.DATASET_RESTRICTIONS = DatasetRestrictionsType("dataset_restrictions")
