# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryTableTimestampFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["MMM dd yyyy HH:mm", "MMM dd yyyy HH:mm:ss", "MMM dd yyyy h:mm a", "MMM dd yyyy h:mm:ss a", "MMM d HH:mm", "MMM d HH:mm:ss", "MMM d h:mm a", "MMM d h:mm:ss a", "MMM d, yyyy HH:mm", "MMM d, yyyy HH:mm:ss", "MMM d, yyyy h:mm a", "MMM d, yyyy h:mm:ss a", "MM/dd/yyyy HH:mm", "MM/dd/yyyy HH:mm:ss", "MM/dd/yyyy h:mm a", "MM/dd/yyyy h:mm:ss a", "dd/MM/yyyy HH:mm", "dd/MM/yyyy HH:mm:ss", "dd/MM/yyyy h:mm a", "dd/MM/yyyy h:mm:ss a", "MMMM d, yyyy HH:mm", "MMMM d, yyyy HH:mm:ss", "MMMM d, yyyy h:mm a", "MMMM d, yyyy h:mm:ss a"].
    :type value: str
    """

    allowed_values = {
        "MMM dd yyyy HH:mm",
        "MMM dd yyyy HH:mm:ss",
        "MMM dd yyyy h:mm a",
        "MMM dd yyyy h:mm:ss a",
        "MMM d HH:mm",
        "MMM d HH:mm:ss",
        "MMM d h:mm a",
        "MMM d h:mm:ss a",
        "MMM d, yyyy HH:mm",
        "MMM d, yyyy HH:mm:ss",
        "MMM d, yyyy h:mm a",
        "MMM d, yyyy h:mm:ss a",
        "MM/dd/yyyy HH:mm",
        "MM/dd/yyyy HH:mm:ss",
        "MM/dd/yyyy h:mm a",
        "MM/dd/yyyy h:mm:ss a",
        "dd/MM/yyyy HH:mm",
        "dd/MM/yyyy HH:mm:ss",
        "dd/MM/yyyy h:mm a",
        "dd/MM/yyyy h:mm:ss a",
        "MMMM d, yyyy HH:mm",
        "MMMM d, yyyy HH:mm:ss",
        "MMMM d, yyyy h:mm a",
        "MMMM d, yyyy h:mm:ss a",
    }
    MMM_DD_YYYY_HH_MM: ClassVar["QueryTableTimestampFormat"]
    MMM_DD_YYYY_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    MMM_DD_YYYY_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    MMM_DD_YYYY_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]
    MMM_D_HH_MM: ClassVar["QueryTableTimestampFormat"]
    MMM_D_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    MMM_D_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    MMM_D_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]
    MMM_D__YYYY_HH_MM: ClassVar["QueryTableTimestampFormat"]
    MMM_D__YYYY_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    MMM_D__YYYY_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    MMM_D__YYYY_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]
    MM_DD_YYYY_HH_MM: ClassVar["QueryTableTimestampFormat"]
    MM_DD_YYYY_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    MM_DD_YYYY_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    MM_DD_YYYY_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]
    DD_MM_YYYY_HH_MM: ClassVar["QueryTableTimestampFormat"]
    DD_MM_YYYY_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    DD_MM_YYYY_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    DD_MM_YYYY_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]
    MMMM_D__YYYY_HH_MM: ClassVar["QueryTableTimestampFormat"]
    MMMM_D__YYYY_HH_MM_SS: ClassVar["QueryTableTimestampFormat"]
    MMMM_D__YYYY_H_MM_A: ClassVar["QueryTableTimestampFormat"]
    MMMM_D__YYYY_H_MM_SS_A: ClassVar["QueryTableTimestampFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryTableTimestampFormat.MMM_DD_YYYY_HH_MM = QueryTableTimestampFormat("MMM dd yyyy HH:mm")
QueryTableTimestampFormat.MMM_DD_YYYY_HH_MM_SS = QueryTableTimestampFormat("MMM dd yyyy HH:mm:ss")
QueryTableTimestampFormat.MMM_DD_YYYY_H_MM_A = QueryTableTimestampFormat("MMM dd yyyy h:mm a")
QueryTableTimestampFormat.MMM_DD_YYYY_H_MM_SS_A = QueryTableTimestampFormat("MMM dd yyyy h:mm:ss a")
QueryTableTimestampFormat.MMM_D_HH_MM = QueryTableTimestampFormat("MMM d HH:mm")
QueryTableTimestampFormat.MMM_D_HH_MM_SS = QueryTableTimestampFormat("MMM d HH:mm:ss")
QueryTableTimestampFormat.MMM_D_H_MM_A = QueryTableTimestampFormat("MMM d h:mm a")
QueryTableTimestampFormat.MMM_D_H_MM_SS_A = QueryTableTimestampFormat("MMM d h:mm:ss a")
QueryTableTimestampFormat.MMM_D__YYYY_HH_MM = QueryTableTimestampFormat("MMM d, yyyy HH:mm")
QueryTableTimestampFormat.MMM_D__YYYY_HH_MM_SS = QueryTableTimestampFormat("MMM d, yyyy HH:mm:ss")
QueryTableTimestampFormat.MMM_D__YYYY_H_MM_A = QueryTableTimestampFormat("MMM d, yyyy h:mm a")
QueryTableTimestampFormat.MMM_D__YYYY_H_MM_SS_A = QueryTableTimestampFormat("MMM d, yyyy h:mm:ss a")
QueryTableTimestampFormat.MM_DD_YYYY_HH_MM = QueryTableTimestampFormat("MM/dd/yyyy HH:mm")
QueryTableTimestampFormat.MM_DD_YYYY_HH_MM_SS = QueryTableTimestampFormat("MM/dd/yyyy HH:mm:ss")
QueryTableTimestampFormat.MM_DD_YYYY_H_MM_A = QueryTableTimestampFormat("MM/dd/yyyy h:mm a")
QueryTableTimestampFormat.MM_DD_YYYY_H_MM_SS_A = QueryTableTimestampFormat("MM/dd/yyyy h:mm:ss a")
QueryTableTimestampFormat.DD_MM_YYYY_HH_MM = QueryTableTimestampFormat("dd/MM/yyyy HH:mm")
QueryTableTimestampFormat.DD_MM_YYYY_HH_MM_SS = QueryTableTimestampFormat("dd/MM/yyyy HH:mm:ss")
QueryTableTimestampFormat.DD_MM_YYYY_H_MM_A = QueryTableTimestampFormat("dd/MM/yyyy h:mm a")
QueryTableTimestampFormat.DD_MM_YYYY_H_MM_SS_A = QueryTableTimestampFormat("dd/MM/yyyy h:mm:ss a")
QueryTableTimestampFormat.MMMM_D__YYYY_HH_MM = QueryTableTimestampFormat("MMMM d, yyyy HH:mm")
QueryTableTimestampFormat.MMMM_D__YYYY_HH_MM_SS = QueryTableTimestampFormat("MMMM d, yyyy HH:mm:ss")
QueryTableTimestampFormat.MMMM_D__YYYY_H_MM_A = QueryTableTimestampFormat("MMMM d, yyyy h:mm a")
QueryTableTimestampFormat.MMMM_D__YYYY_H_MM_SS_A = QueryTableTimestampFormat("MMMM d, yyyy h:mm:ss a")
