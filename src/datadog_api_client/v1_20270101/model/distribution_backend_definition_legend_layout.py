# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DistributionBackendDefinitionLegendLayout(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["vertical", "horizontal", "auto"].
    :type value: str
    """

    allowed_values = {
        "vertical",
        "horizontal",
        "auto",
    }
    VERTICAL: ClassVar["DistributionBackendDefinitionLegendLayout"]
    HORIZONTAL: ClassVar["DistributionBackendDefinitionLegendLayout"]
    AUTO: ClassVar["DistributionBackendDefinitionLegendLayout"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DistributionBackendDefinitionLegendLayout.VERTICAL = DistributionBackendDefinitionLegendLayout("vertical")
DistributionBackendDefinitionLegendLayout.HORIZONTAL = DistributionBackendDefinitionLegendLayout("horizontal")
DistributionBackendDefinitionLegendLayout.AUTO = DistributionBackendDefinitionLegendLayout("auto")
