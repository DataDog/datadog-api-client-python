# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.process_summary_attributes import ProcessSummaryAttributes
        from datadog_api_client.v2.model.process_summary_type import ProcessSummaryType

        return {
            "attributes": (ProcessSummaryAttributes,),
            "id": (str,),
            "type": (ProcessSummaryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Process summary object.

        :param attributes: Attributes for a process summary.
        :type attributes: ProcessSummaryAttributes, optional

        :param id: Process ID.
        :type id: str, optional

        :param type: Type of process summary.
        :type type: ProcessSummaryType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ProcessSummary, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
