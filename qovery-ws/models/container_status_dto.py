# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from qovery-ws.models.container_state_dto import ContainerStateDto
from qovery-ws.models.container_state_terminated_dto import ContainerStateTerminatedDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContainerStatusDto(BaseModel):
    """
    ContainerStatusDto
    """ # noqa: E501
    current_state: Optional[ContainerStateDto] = None
    image: StrictStr
    last_terminated_state: Optional[ContainerStateTerminatedDto] = None
    name: StrictStr
    restart_count: Annotated[int, Field(strict=True, ge=0)]
    __properties: ClassVar[List[str]] = ["current_state", "image", "last_terminated_state", "name", "restart_count"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ContainerStatusDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of current_state
        if self.current_state:
            _dict['current_state'] = self.current_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_terminated_state
        if self.last_terminated_state:
            _dict['last_terminated_state'] = self.last_terminated_state.to_dict()
        # set to None if current_state (nullable) is None
        # and model_fields_set contains the field
        if self.current_state is None and "current_state" in self.model_fields_set:
            _dict['current_state'] = None

        # set to None if last_terminated_state (nullable) is None
        # and model_fields_set contains the field
        if self.last_terminated_state is None and "last_terminated_state" in self.model_fields_set:
            _dict['last_terminated_state'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContainerStatusDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_state": ContainerStateDto.from_dict(obj.get("current_state")) if obj.get("current_state") is not None else None,
            "image": obj.get("image"),
            "last_terminated_state": ContainerStateTerminatedDto.from_dict(obj.get("last_terminated_state")) if obj.get("last_terminated_state") is not None else None,
            "name": obj.get("name"),
            "restart_count": obj.get("restart_count")
        })
        return _obj


