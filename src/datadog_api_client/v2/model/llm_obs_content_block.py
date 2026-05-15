# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_content_block_llm_obs_trace_interaction_type import (
        LLMObsContentBlockLLMObsTraceInteractionType,
    )
    from datadog_api_client.v2.model.llm_obs_content_block_header_level import LLMObsContentBlockHeaderLevel
    from datadog_api_client.v2.model.llm_obs_content_block_time_frame import LLMObsContentBlockTimeFrame
    from datadog_api_client.v2.model.llm_obs_content_block_type import LLMObsContentBlockType


class LLMObsContentBlock(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_content_block_llm_obs_trace_interaction_type import (
            LLMObsContentBlockLLMObsTraceInteractionType,
        )
        from datadog_api_client.v2.model.llm_obs_content_block_header_level import LLMObsContentBlockHeaderLevel
        from datadog_api_client.v2.model.llm_obs_content_block_time_frame import LLMObsContentBlockTimeFrame
        from datadog_api_client.v2.model.llm_obs_content_block_type import LLMObsContentBlockType

        return {
            "alt": (str,),
            "content": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "height": (int,),
            "interaction_type": (LLMObsContentBlockLLMObsTraceInteractionType,),
            "label": (str,),
            "level": (LLMObsContentBlockHeaderLevel,),
            "tile_def": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "time_frame": (LLMObsContentBlockTimeFrame,),
            "trace_id": (str,),
            "type": (LLMObsContentBlockType,),
            "url": (str,),
        }

    attribute_map = {
        "alt": "alt",
        "content": "content",
        "height": "height",
        "interaction_type": "interactionType",
        "label": "label",
        "level": "level",
        "tile_def": "tileDef",
        "time_frame": "timeFrame",
        "trace_id": "traceId",
        "type": "type",
        "url": "url",
    }

    def __init__(
        self_,
        type: LLMObsContentBlockType,
        alt: Union[str, UnsetType] = unset,
        content: Union[Any, UnsetType] = unset,
        height: Union[int, UnsetType] = unset,
        interaction_type: Union[LLMObsContentBlockLLMObsTraceInteractionType, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        level: Union[LLMObsContentBlockHeaderLevel, UnsetType] = unset,
        tile_def: Union[Any, UnsetType] = unset,
        time_frame: Union[LLMObsContentBlockTimeFrame, UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single content block rendered inside a ``display_block`` interaction.
        ``type`` discriminates which other fields are meaningful:

        * ``markdown`` / ``text`` : ``content`` must be a string.
        * ``header`` : ``content`` must be a string; ``level`` , when set, must be one of ``sm`` , ``md`` , ``lg`` , ``xl``.
        * ``json`` : ``content`` must be a well-formed JSON value (object, array, or scalar).
        * ``image`` : ``url`` is required.
        * ``widget`` : ``tileDef`` is required (any well-formed JSON; the frontend owns the renderable schema).
        * ``llmobs_trace`` : ``traceId`` is required; ``interactionType`` , when set, must be ``trace`` or ``experiment_trace``.

        ``height`` , when set, must be positive.

        :param alt: Alternative text for an ``image`` block.
        :type alt: str, optional

        :param content: Block payload. A string for ``markdown`` , ``header`` , and ``text`` ; an
            arbitrary JSON value (object, array, or scalar) for ``json``. Omitted
            for ``image`` , ``widget`` , and ``llmobs_trace``.
        :type content: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param height: Optional rendered height. Must be positive when set.
        :type height: int, optional

        :param interaction_type: Upstream interaction type referenced by an ``llmobs_trace`` block.
            Restricted to ``trace`` or ``experiment_trace``.
        :type interaction_type: LLMObsContentBlockLLMObsTraceInteractionType, optional

        :param label: Optional label rendered alongside the block.
        :type label: str, optional

        :param level: Visual size for a ``header`` block.
        :type level: LLMObsContentBlockHeaderLevel, optional

        :param tile_def: Tile definition for a ``widget`` block. Required for ``widget``. The
            schema is owned by the frontend renderer.
        :type tile_def: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param time_frame: Unix-millis time range used by chart blocks.
        :type time_frame: LLMObsContentBlockTimeFrame, optional

        :param trace_id: Trace identifier. Required for ``llmobs_trace`` blocks.
        :type trace_id: str, optional

        :param type: Discriminator for a single ``display_block`` content block. Adding a
            variant requires coordinated changes in the frontend renderer.
        :type type: LLMObsContentBlockType

        :param url: URL of the image. Required for ``image`` blocks.
        :type url: str, optional
        """
        if alt is not unset:
            kwargs["alt"] = alt
        if content is not unset:
            kwargs["content"] = content
        if height is not unset:
            kwargs["height"] = height
        if interaction_type is not unset:
            kwargs["interaction_type"] = interaction_type
        if label is not unset:
            kwargs["label"] = label
        if level is not unset:
            kwargs["level"] = level
        if tile_def is not unset:
            kwargs["tile_def"] = tile_def
        if time_frame is not unset:
            kwargs["time_frame"] = time_frame
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)

        self_.type = type
