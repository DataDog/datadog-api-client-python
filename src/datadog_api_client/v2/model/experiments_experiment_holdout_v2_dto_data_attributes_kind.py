# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentHoldoutV2DTODataAttributesKind(ModelSimple):
    """
    Whether Datadog serves the holdout. Datadog serves MANAGED holdouts. EXTERNAL holdouts record what your own feature flagging system holds back, and Datadog does not serve them.

    :param value: Must be one of ["MANAGED", "EXTERNAL", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "MANAGED",
        "EXTERNAL",
        "UNKNOWN",
    }
    MANAGED: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesKind"]
    EXTERNAL: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesKind"]
    UNKNOWN: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentHoldoutV2DTODataAttributesKind.MANAGED = ExperimentsExperimentHoldoutV2DTODataAttributesKind(
    "MANAGED"
)
ExperimentsExperimentHoldoutV2DTODataAttributesKind.EXTERNAL = ExperimentsExperimentHoldoutV2DTODataAttributesKind(
    "EXTERNAL"
)
ExperimentsExperimentHoldoutV2DTODataAttributesKind.UNKNOWN = ExperimentsExperimentHoldoutV2DTODataAttributesKind(
    "UNKNOWN"
)
