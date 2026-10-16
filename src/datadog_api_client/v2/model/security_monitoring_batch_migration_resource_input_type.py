# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationResourceInputType(ModelSimple):
    """
    The type of the source rule: `spl` for a Splunk SPL search or saved search definition,
        `natural_language` for a plain-English description of the behavior to detect, or `kql`
        for a Microsoft KQL query. SPL inputs must be self-contained, with search macros expanded.

    :param value: Must be one of ["natural_language", "spl", "kql"].
    :type value: str
    """

    allowed_values = {
        "natural_language",
        "spl",
        "kql",
    }
    NATURAL_LANGUAGE: ClassVar["SecurityMonitoringBatchMigrationResourceInputType"]
    SPL: ClassVar["SecurityMonitoringBatchMigrationResourceInputType"]
    KQL: ClassVar["SecurityMonitoringBatchMigrationResourceInputType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationResourceInputType.NATURAL_LANGUAGE = SecurityMonitoringBatchMigrationResourceInputType(
    "natural_language"
)
SecurityMonitoringBatchMigrationResourceInputType.SPL = SecurityMonitoringBatchMigrationResourceInputType("spl")
SecurityMonitoringBatchMigrationResourceInputType.KQL = SecurityMonitoringBatchMigrationResourceInputType("kql")
