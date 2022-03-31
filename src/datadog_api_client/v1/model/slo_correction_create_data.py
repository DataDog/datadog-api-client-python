# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_correction_create_request_attributes import (
        SLOCorrectionCreateRequestAttributes,
    )
    from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

    globals()["SLOCorrectionCreateRequestAttributes"] = SLOCorrectionCreateRequestAttributes
    globals()["SLOCorrectionType"] = SLOCorrectionType


class SLOCorrectionCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "attributes": (SLOCorrectionCreateRequestAttributes,),
            "type": (SLOCorrectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        The data object associated with the SLO correction to be created.

        :param attributes: The attribute object associated with the SLO correction to be created.
        :type attributes: SLOCorrectionCreateRequestAttributes, optional

        :param type: SLO correction resource type.
        :type type: SLOCorrectionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
