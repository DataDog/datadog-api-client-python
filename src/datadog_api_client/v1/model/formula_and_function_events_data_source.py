# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionEventsDataSource(ModelSimple):
    """
    Data source for event platform-based queries.

    :param value: Must be one of ["logs", "spans", "network", "rum", "security_signals", "profiles", "audit", "events", "ci_tests"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "LOGS": "logs",
            "SPANS": "spans",
            "NETWORK": "network",
            "RUM": "rum",
            "SECURITY_SIGNALS": "security_signals",
            "PROFILES": "profiles",
            "AUDIT": "audit",
            "EVENTS": "events",
            "CI_TESTS": "ci_tests",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
