# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOCorrectionUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory

        return {
            "category": (SLOCorrectionCategory,),
            "description": (str,),
            "duration": (int,),
            "end": (int,),
            "rrule": (str,),
            "start": (int,),
            "timezone": (str,),
        }

    attribute_map = {
        "category": "category",
        "description": "description",
        "duration": "duration",
        "end": "end",
        "rrule": "rrule",
        "start": "start",
        "timezone": "timezone",
    }

    def __init__(self, *args, **kwargs):
        """
        The attribute object associated with the SLO correction to be updated.

        :param category: Category the SLO correction belongs to.
        :type category: SLOCorrectionCategory, optional

        :param description: Description of the correction being made.
        :type description: str, optional

        :param duration: Length of time (in seconds) for a specified ``rrule`` recurring SLO correction.
        :type duration: int, optional

        :param end: Ending time of the correction in epoch seconds.
        :type end: int, optional

        :param rrule: The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections
            are ``FREQ`` , ``INTERVAL`` , ``COUNT`` , and ``UNTIL``.
        :type rrule: str, optional

        :param start: Starting time of the correction in epoch seconds.
        :type start: int, optional

        :param timezone: The timezone to display in the UI for the correction times (defaults to "UTC").
        :type timezone: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionUpdateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
