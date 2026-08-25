# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAccountDataflowHealth(ModelSimple):
    """
    Collection health of a single dataflow.

    :param value: Must be one of ["DATAFLOW_HEALTH_OK", "DATAFLOW_HEALTH_BROKEN", "DATAFLOW_HEALTH_UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "DATAFLOW_HEALTH_OK",
        "DATAFLOW_HEALTH_BROKEN",
        "DATAFLOW_HEALTH_UNKNOWN",
    }
    OK: ClassVar["IntegrationAccountDataflowHealth"]
    BROKEN: ClassVar["IntegrationAccountDataflowHealth"]
    UNKNOWN: ClassVar["IntegrationAccountDataflowHealth"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAccountDataflowHealth.OK = IntegrationAccountDataflowHealth("DATAFLOW_HEALTH_OK")
IntegrationAccountDataflowHealth.BROKEN = IntegrationAccountDataflowHealth("DATAFLOW_HEALTH_BROKEN")
IntegrationAccountDataflowHealth.UNKNOWN = IntegrationAccountDataflowHealth("DATAFLOW_HEALTH_UNKNOWN")
