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


class RUMIssueStreamQueryInvestigation(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "completed": (bool,),
        }

    attribute_map = {
        "completed": "completed",
    }

    def __init__(self_, completed: Union[bool, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param completed: Test-only generated schema for the dashboard versioning proof of concept.
        :type completed: bool, optional
        """
        if completed is not unset:
            kwargs["completed"] = completed
        super().__init__(kwargs)
