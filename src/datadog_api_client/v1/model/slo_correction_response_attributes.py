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
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
    from datadog_api_client.v1.model.slo_correction_response_attributes_modifier import (
        SLOCorrectionResponseAttributesModifier,
    )

    globals()["Creator"] = Creator
    globals()["SLOCorrectionCategory"] = SLOCorrectionCategory
    globals()["SLOCorrectionResponseAttributesModifier"] = SLOCorrectionResponseAttributesModifier


class SLOCorrectionResponseAttributes(ModelNormal):
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
            "created_at": (int,),
            "creator": (Creator,),
            "description": (str,),
            "duration": (
                int,
                none_type,
            ),
            "end": (int,),
            "modified_at": (int,),
            "modifier": (SLOCorrectionResponseAttributesModifier,),
            "rrule": (
                str,
                none_type,
            ),
            "slo_id": (str,),
            "start": (int,),
            "timezone": (str,),
        }

    attribute_map = {
        "category": "category",
        "created_at": "created_at",
        "creator": "creator",
        "description": "description",
        "duration": "duration",
        "end": "end",
        "modified_at": "modified_at",
        "modifier": "modifier",
        "rrule": "rrule",
        "slo_id": "slo_id",
        "start": "start",
        "timezone": "timezone",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SLOCorrectionResponseAttributes - a model defined in OpenAPI

        Keyword Args:
            category (SLOCorrectionCategory): [optional]
            created_at (int): [optional] The epoch timestamp of when the correction was created at
            creator (Creator): [optional]
            description (str): [optional] Description of the correction being made.
            duration (int, none_type): [optional] Length of time (in seconds) for a specified `rrule` recurring SLO correction.
            end (int): [optional] Ending time of the correction in epoch seconds.
            modified_at (int): [optional] The epoch timestamp of when the correction was modified at
            modifier (SLOCorrectionResponseAttributesModifier): [optional]
            rrule (str, none_type): [optional] The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT` and `UNTIL`.
            slo_id (str): [optional] ID of the SLO that this correction will be applied to.
            start (int): [optional] Starting time of the correction in epoch seconds.
            timezone (str): [optional] The timezone to display in the UI for the correction times (defaults to \"UTC\").
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionResponseAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
