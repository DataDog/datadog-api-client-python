# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReferenceTableSourceType(ModelSimple):
    """
    The source type for reference table data. Includes all possible source types that can appear in responses.

    :param value: Must be one of ["LOCAL_FILE", "S3", "GCS", "AZURE", "SERVICENOW", "SALESFORCE", "DATABRICKS", "SNOWFLAKE"].
    :type value: str
    """

    allowed_values = {
        "LOCAL_FILE",
        "S3",
        "GCS",
        "AZURE",
        "SERVICENOW",
        "SALESFORCE",
        "DATABRICKS",
        "SNOWFLAKE",
    }
    LOCAL_FILE: ClassVar["ReferenceTableSourceType"]
    S3: ClassVar["ReferenceTableSourceType"]
    GCS: ClassVar["ReferenceTableSourceType"]
    AZURE: ClassVar["ReferenceTableSourceType"]
    SERVICENOW: ClassVar["ReferenceTableSourceType"]
    SALESFORCE: ClassVar["ReferenceTableSourceType"]
    DATABRICKS: ClassVar["ReferenceTableSourceType"]
    SNOWFLAKE: ClassVar["ReferenceTableSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReferenceTableSourceType.LOCAL_FILE = ReferenceTableSourceType("LOCAL_FILE")
ReferenceTableSourceType.S3 = ReferenceTableSourceType("S3")
ReferenceTableSourceType.GCS = ReferenceTableSourceType("GCS")
ReferenceTableSourceType.AZURE = ReferenceTableSourceType("AZURE")
ReferenceTableSourceType.SERVICENOW = ReferenceTableSourceType("SERVICENOW")
ReferenceTableSourceType.SALESFORCE = ReferenceTableSourceType("SALESFORCE")
ReferenceTableSourceType.DATABRICKS = ReferenceTableSourceType("DATABRICKS")
ReferenceTableSourceType.SNOWFLAKE = ReferenceTableSourceType("SNOWFLAKE")
