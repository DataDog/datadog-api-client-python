# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatabricksIntegrationAccountOAuthAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "databricks-oauth". Must be one of ["databricks-oauth"].
    :type value: str
    """

    allowed_values = {
        "databricks-oauth",
    }
    DATABRICKS_OAUTH: ClassVar["DatabricksIntegrationAccountOAuthAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatabricksIntegrationAccountOAuthAuthType.DATABRICKS_OAUTH = DatabricksIntegrationAccountOAuthAuthType(
    "databricks-oauth"
)
