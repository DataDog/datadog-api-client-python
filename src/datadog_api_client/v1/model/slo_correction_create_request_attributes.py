# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory

    globals()["SLOCorrectionCategory"] = SLOCorrectionCategory


class SLOCorrectionCreateRequestAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "category": (SLOCorrectionCategory,),
            "description": (str,),
            "duration": (int,),
            "end": (int,),
            "rrule": (str,),
            "slo_id": (str,),
            "start": (int,),
            "timezone": (str,),
        }

    attribute_map = {
        "category": "category",
        "slo_id": "slo_id",
        "start": "start",
        "description": "description",
        "duration": "duration",
        "end": "end",
        "rrule": "rrule",
        "timezone": "timezone",
    }

    read_only_vars = {}

    def __init__(self, category, slo_id, start, *args, **kwargs):
        """SLOCorrectionCreateRequestAttributes - a model defined in OpenAPI

        Args:
            category (SLOCorrectionCategory):
            slo_id (str): ID of the SLO that this correction will be applied to.
            start (int): Starting time of the correction in epoch seconds.

        Keyword Args:
            description (str): [optional] Description of the correction being made.
            duration (int): [optional] Length of time (in seconds) for a specified `rrule` recurring SLO correction.
            end (int): [optional] Ending time of the correction in epoch seconds.
            rrule (str): [optional] The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT` and `UNTIL`.
            timezone (str): [optional] The timezone to display in the UI for the correction times (defaults to \"UTC\").
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.category = category
        self.slo_id = slo_id
        self.start = start

    @classmethod
    def _from_openapi_data(cls, category, slo_id, start, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionCreateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.category = category
        self.slo_id = slo_id
        self.start = start
        return self
