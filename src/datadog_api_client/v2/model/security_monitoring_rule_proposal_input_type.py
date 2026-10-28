# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleProposalInputType(ModelSimple):
    """
    The type of input to generate the proposed rule from: `natural_language` for a
        plain-English description of the behavior to detect, `spl` for a Splunk SPL search or
        saved search definition, or `kql` for a Microsoft KQL query. SPL inputs must be
        self-contained, with search macros expanded.

    :param value: Must be one of ["natural_language", "spl", "kql"].
    :type value: str
    """

    allowed_values = {
        "natural_language",
        "spl",
        "kql",
    }
    NATURAL_LANGUAGE: ClassVar["SecurityMonitoringRuleProposalInputType"]
    SPL: ClassVar["SecurityMonitoringRuleProposalInputType"]
    KQL: ClassVar["SecurityMonitoringRuleProposalInputType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleProposalInputType.NATURAL_LANGUAGE = SecurityMonitoringRuleProposalInputType("natural_language")
SecurityMonitoringRuleProposalInputType.SPL = SecurityMonitoringRuleProposalInputType("spl")
SecurityMonitoringRuleProposalInputType.KQL = SecurityMonitoringRuleProposalInputType("kql")
