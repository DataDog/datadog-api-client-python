# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IntegrationIncidentSeverityConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "priority_mapping": ({str: (str,)},),
        }

    attribute_map = {
        "priority_mapping": "priority_mapping",
    }

    def __init__(self_, priority_mapping: Union[Dict[str, str], UnsetType] = unset, **kwargs):
        """


        :param priority_mapping:
        :type priority_mapping: {str: (str,)}, optional
        """
        if priority_mapping is not unset:
            kwargs["priority_mapping"] = priority_mapping
        super().__init__(kwargs)
