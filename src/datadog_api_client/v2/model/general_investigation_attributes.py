# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GeneralInvestigationAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        Attributes for a general investigation, not tied to a specific monitor alert.

        :param description: A free-form description of what to investigate, up to 4,096 characters.
        :type description: str

        :param tags: Tags that scope the investigation.
        :type tags: [str], optional

        :param end_time: The end of the investigation window, in Unix milliseconds.
        :type end_time: int

        :param start_time: The start of the investigation window, in Unix milliseconds.
        :type start_time: int
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.general_investigation_attributes_without_time_bounds import (
            GeneralInvestigationAttributesWithoutTimeBounds,
        )
        from datadog_api_client.v2.model.general_investigation_attributes_with_time_bounds import (
            GeneralInvestigationAttributesWithTimeBounds,
        )

        return {
            "oneOf": [
                GeneralInvestigationAttributesWithoutTimeBounds,
                GeneralInvestigationAttributesWithTimeBounds,
            ],
        }
