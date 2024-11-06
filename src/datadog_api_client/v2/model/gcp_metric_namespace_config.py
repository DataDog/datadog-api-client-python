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


class GCPMetricNamespaceConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "id": (str,),
        }

    attribute_map = {
        "disabled": "disabled",
        "id": "id",
    }

    def __init__(self_, disabled: Union[bool, UnsetType] = unset, id: Union[str, UnsetType] = unset, **kwargs):
        """
        Configuration for a GCP metric namespace.

        :param disabled: When disabled, Datadog does not collect metrics that are related to this GCP metric namespace.
        :type disabled: bool, optional

        :param id: The id of the GCP metric namespace.
        :type id: str, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
