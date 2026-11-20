# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CheckStatusBackendDefinitionGrouping(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["check", "cluster"].
    :type value: str
    """

    allowed_values = {
        "check",
        "cluster",
    }
    CHECK: ClassVar["CheckStatusBackendDefinitionGrouping"]
    CLUSTER: ClassVar["CheckStatusBackendDefinitionGrouping"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CheckStatusBackendDefinitionGrouping.CHECK = CheckStatusBackendDefinitionGrouping("check")
CheckStatusBackendDefinitionGrouping.CLUSTER = CheckStatusBackendDefinitionGrouping("cluster")
