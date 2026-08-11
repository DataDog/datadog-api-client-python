# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class STIXIngestResponseType(ModelSimple):
    """
    The STIX ingestion resource type.

    :param value: If omitted defaults to "threat-intel-stix-ingest". Must be one of ["threat-intel-stix-ingest"].
    :type value: str
    """

    allowed_values = {
        "threat-intel-stix-ingest",
    }
    THREAT_INTEL_STIX_INGEST: ClassVar["STIXIngestResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


STIXIngestResponseType.THREAT_INTEL_STIX_INGEST = STIXIngestResponseType("threat-intel-stix-ingest")
