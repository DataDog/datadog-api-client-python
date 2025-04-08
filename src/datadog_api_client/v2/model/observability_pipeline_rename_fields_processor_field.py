# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineRenameFieldsProcessorField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "destination": (str,),
            "preserve_source": (bool,),
            "source": (str,),
        }

    attribute_map = {
        "destination": "destination",
        "preserve_source": "preserve_source",
        "source": "source",
    }

    def __init__(self_, destination: str, preserve_source: bool, source: str, **kwargs):
        """
        Defines how to rename a field in log events.

        :param destination: The field name to assign the renamed value to.
        :type destination: str

        :param preserve_source: Indicates whether the original field, that is received from the source, should be kept ( ``true`` ) or removed ( ``false`` ) after renaming.
        :type preserve_source: bool

        :param source: The original field name in the log event that should be renamed.
        :type source: str
        """
        super().__init__(kwargs)

        self_.destination = destination
        self_.preserve_source = preserve_source
        self_.source = source
