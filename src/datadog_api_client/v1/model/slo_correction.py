# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOCorrection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction_response_attributes import SLOCorrectionResponseAttributes
        from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

        return {
            "attributes": (SLOCorrectionResponseAttributes,),
            "id": (str,),
            "type": (SLOCorrectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The response object of a list of SLO corrections.

        :param attributes: The attribute object associated with the SLO correction.
        :type attributes: SLOCorrectionResponseAttributes, optional

        :param id: The ID of the SLO correction.
        :type id: str, optional

        :param type: SLO correction resource type.
        :type type: SLOCorrectionType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrection, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
