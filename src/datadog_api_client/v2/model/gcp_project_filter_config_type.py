# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPProjectFilterConfigType(ModelSimple):
    """
    The GCP project field that the filters are matched against.

    :param value: Must be one of ["project_id", "project_label"].
    :type value: str
    """

    allowed_values = {
        "project_id",
        "project_label",
    }
    PROJECT_ID: ClassVar["GCPProjectFilterConfigType"]
    PROJECT_LABEL: ClassVar["GCPProjectFilterConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPProjectFilterConfigType.PROJECT_ID = GCPProjectFilterConfigType("project_id")
GCPProjectFilterConfigType.PROJECT_LABEL = GCPProjectFilterConfigType("project_label")
