# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_correction_update_data import SLOCorrectionUpdateData

    globals()["SLOCorrectionUpdateData"] = SLOCorrectionUpdateData


class SLOCorrectionUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": (SLOCorrectionUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        An object that defines a correction to be applied to an SLO.

        :param data: The data object associated with the SLO correction to be updated.
        :type data: SLOCorrectionUpdateData, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
