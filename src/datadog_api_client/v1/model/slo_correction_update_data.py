# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOCorrectionUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction_update_request_attributes import (
            SLOCorrectionUpdateRequestAttributes,
        )
        from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

        return {
            "attributes": (SLOCorrectionUpdateRequestAttributes,),
            "type": (SLOCorrectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The data object associated with the SLO correction to be updated.

        :param attributes: The attribute object associated with the SLO correction to be updated.
        :type attributes: SLOCorrectionUpdateRequestAttributes, optional

        :param type: SLO correction resource type.
        :type type: SLOCorrectionType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
